# 審稿前的程式檢查：python3 tools/check_batches.py <年> <批號> [<批號> …]   例：python3 tools/check_batches.py 2017 b005 b006 b007 b008
# 2026-10-31 建立，2026-11-07 加檢查。把能機械判斷的先掃完，產出 work/out/y<年>/checks/check_<批號們>.md，Opus 驗收時只要重點看被標的件＋抽查事實。
# 只讀不改。檢查：筆數與 id 順序、【得獎】開頭與是否等於 in 檔 official.award_line、資料來源、`**`、空【爭議】、
# （--dir <資料夾> 可指定 in／out 所在資料夾）
# 一句話字數／連續中文／寫到得獎、標籤前 8 個、疑似成效句、uncertain、note 搜尋摘要、敏感字、
# 圖片（HEAD：image/*、<5MB、http／redirect／過期 CDN）、有 case board 候選卻沒用、資料來源網址（404／網域不存在）。
# 2026-11-07 加（2017 檢討）：note 沒有「已搜爭議」紀錄、一句話只寫「一系列平面／海報」、圖片尺寸太小或疑似全黑、
# 暫存資料夾 tmp_<批號>/ 裡的腳本有自加 User-Agent 或刪檔指令（違規）。
import json, os, re, sys, glob, collections, datetime, urllib.request, concurrent.futures as cf
here = os.path.dirname(os.path.abspath(__file__)); W = here + '/..'
sys.path.insert(0, here)
from imgprobe import probe
av = sys.argv[1:]; D = av.pop(av.index('--dir') + 1) if '--dir' in av else None
if '--dir' in av: av.remove('--dir')
if not av or av[0] in ('-h', '--help') or not re.fullmatch(r'\d{4}', av[0]) or not all(re.fullmatch(r'b\d{3}', b) for b in av[1:]):
    sys.exit('用法：python3 tools/check_batches.py <年> <批號> [<批號> …]   例：python3 tools/check_batches.py 2017 b005 b006（瀏覽器標頭已內建，直接跑就好）')
Y = av[0]; BS = av[1:]; O = D or f'{W}/years/y{Y}'   # --dir：指定別的資料夾（測試用）
HEAD8 = ['得獎創意案例', '坎城獅子獎', f'坎城獅子獎 {Y}', '坎城', '坎城創意節', 'Cannes Lions', '坎城案例', '坎城廣告獎']
EFFECT = re.compile(r'[^。\n]*(收聽了|觀看次數|觀看超過|播放超過|點閱|造訪|曝光|分享超過|成長\s*\d|增加了?\s*\d|銷量|市占|萬次|億次|大量報導|媒體報導|拿下|獲得.{0,12}獎|Epica|El Ojo|Eurobest|One Show|D&AD|Clio|Effie|Spikes)[^。\n]*。')
SENS = [(r'AIza[0-9A-Za-z_-]{20,}', 'API key'), (r'sk-[A-Za-z0-9]{20,}', 'API key'), (r'xox[bap]-', 'Slack token'),
        (r'[\w.+-]+@[\w-]+\.[\w.]+', 'email')] + ([(os.environ['CANNES_SENS'], '內部字樣')] if os.environ.get('CANNES_SENS') else [])  # 內部字樣清單不放公開專案，本機上線前的 dryrun 會再掃
UA = {'User-Agent': 'Mozilla/5.0'}
SERIES = re.compile(r'一系列|系列(平面|海報|廣告|印刷|作品|插畫|圖像)')
BAD = [(re.compile(r'User-Agent|user_agent|--user-agent|(^|\s)-A\s|Mozilla/\d'), '自己加瀏覽器標頭（User-Agent）'),
       (re.compile(r'(^|[\s;&|(`])(rm|rmdir|unlink|trash)\s|os\.(remove|unlink|rmdir)\(|shutil\.rmtree|\.unlink\(|find\s.*-delete'), '刪檔指令')]

def scan_tmp(b):
    out = []
    for p in glob.glob(f'{O}/tmp_{b}/**/*', recursive=True):
        if not re.search(r'\.(py|sh|js|mjs|bash|zsh|command)$', p) or os.path.getsize(p) > 500000: continue
        try: t = open(p, encoding='utf-8', errors='ignore').read()
        except Exception: continue
        for rx, why in BAD:
            m = rx.search(t)
            if m: out.append(f'違規：{why}（{os.path.relpath(p, O)}：{m.group(0).strip()[:30]}）')
    return out

def head(u, img=False):
    for m in ('HEAD', 'GET'):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, method=m, headers=UA), timeout=20) as r:
                ct = r.headers.get('Content-Type', ''); n = int(r.headers.get('Content-Length') or 0)
                if img and not ct.startswith('image/'): return f'不是圖檔（{ct}）'
                if img and n > 5 * 1024 * 1024: return f'圖檔過大 {n / 1048576:.1f}MB'
                return None
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 406, 429) and m == 'HEAD': continue
            if e.code in (404, 410): return f'{e.code}'
            if e.code in (401, 403, 406, 429, 451): return None if not img else f'HTTP {e.code}（擋爬蟲或限流，再試）'
            err = f'HTTP {e.code}'
        except Exception as e: err = str(e)[:60]
    return f'打不開（{err}）'

def main():
    flags = collections.defaultdict(list); urls = []; imgs = []; total = 0
    for b in BS:
        o = json.load(open(f'{O}/{b}_out.json')); i = json.load(open(f'{O}/{b}_in.json')); im = {x['id']: x for x in i}
        if [x['id'] for x in o] != [x['id'] for x in i]: flags[(b, '整批')].append('筆數或 id 順序跟 in 不同')
        flags[(b, '整批')] += scan_tmp(b)
        for x in o:
            k = (b, x['id'] + ' ' + (x.get('title') or '')); total += 1
            if x.get('decision', '收') != '收': flags[k].append(f'decision＝{x.get("decision")}'); continue
            ft = x.get('full_text') or ''; body = ft.split('資料來源')[0]; ol = x.get('idea_one_liner') or ''
            line = ft.split('\n')[0]; off = (im.get(x['id']) or {}).get('official') or {}
            if not ft.startswith('【得獎】'): flags[k].append('讀稿不是【得獎】開頭')
            elif off.get('award_line') and line != off['award_line']: flags[k].append('【得獎】行跟官方預填不同（確認是有意改的）')
            if '資料來源' not in ft: flags[k].append('沒有資料來源')
            if '**' in ft: flags[k].append('讀稿有 **')
            if re.search(r'【爭議】\s*(無|查過後沒有|未發現)', ft): flags[k].append('空【爭議】段')
            if len(ol) > 65: flags[k].append(f'一句話 {len(ol)} 字')
            run = max((len(m) for m in re.findall(r'[一-鿿]+', ol)), default=0)
            if run > 15: flags[k].append(f'一句話連續中文 {run} 字')
            if re.search(r'獅|得獎|全場大獎', ol): flags[k].append('一句話可能寫到得獎')
            if SERIES.search(ol): flags[k].append('一句話只說「一系列…」：要講出這組作品的巧思（找不到說明就看畫面判斷，看不出就標 uncertain）')
            if not re.search(r'爭議', (x.get('note') or '') + ft): flags[k].append('note 沒有「已搜爭議」紀錄')
            if [t.strip() for t in (x.get('tags') or '').split(',')][:8] != HEAD8: flags[k].append('標籤前 8 個不對')
            for m in EFFECT.finditer(body):
                s = m.group(0).strip()
                if not s.startswith('【得獎】'): flags[k].append('疑似成效／其他獎：' + s[:70])
            if x.get('uncertain'): flags[k].append('uncertain：' + (x.get('note') or '')[-80:])
            n = x.get('note') or ''
            for m in re.finditer('搜尋摘要', n):
                if not re.search(r'未寫入|不寫|未採用|沒採用|不採用|未用|沒用', re.split(r'[。；]', n[m.end():], maxsplit=1)[0]) and not re.search(r'[未沒不非無]', n[max(0, m.start() - 6):m.start()]):
                    flags[k].append('note 說用了搜尋摘要')
            for pat, why in SENS:
                for fld in (ol, ft, x.get('tags') or ''):
                    mm = re.search(pat, fld)
                    if mm: flags[k].append(f'敏感掃描：{why}（{mm.group(0)[:30]}）'); break
            refs = x.get('references') or []
            if len(refs) < 2: flags[k].append(f'資料來源只有 {len(refs)} 個')
            u = x.get('image_url') or ''
            cand = [c for c in ((im.get(x['id']) or {}).get('image_candidates') or []) if '/conversion/' in c]
            if not u: flags[k].append('沒有圖')
            else:
                if re.search(r'^http://|redirect|oe=|x-expires|fbcdn|cdninstagram|tiktok', u): flags[k].append('圖片網址有風險：' + u[:80])
                imgs.append((k, u))
            if cand and u and not any(c.split('?')[0] in u for c in cand): flags[k].append('有官方 case board 沒用：' + cand[0])
            urls += [(k, r) for r in refs]
    flags = {k: v for k, v in flags.items() if v}; flags = collections.defaultdict(list, flags)
    with cf.ThreadPoolExecutor(8) as ex:
        for (k, u), e in zip(imgs, ex.map(lambda t: head(t[1], True), imgs)):
            if e: flags[k].append('圖片：' + e)
        for (k, u), (ps, info) in zip(imgs, ex.map(lambda t: probe(t[1]), imgs)):
            for q in ps:
                if q.startswith(('太小', '檔案極小', '幾乎單色', '是預留圖')): flags[k].append(f'圖片{q}')
        for (k, u), e in zip(urls, ex.map(lambda t: head(t[1]), urls)):
            if e and (e in ('404', '410') or '打不開' in e): flags[k].append(f'資料來源壞掉（{e}）：{u[:80]}')
    os.makedirs(f'{O}/checks', exist_ok=True)
    p = f'{O}/checks/check_{"_".join(BS)}.md'
    with open(p, 'w', encoding='utf-8') as f:
        f.write(f'# {Y} 程式檢查 {" ".join(BS)}（{datetime.datetime.now():%Y-%m-%d %H:%M}）\n\n共 {total} 件，被標 {len([k for k in flags])} 件。'
                '「疑似成效」是關鍵字比對，背景數字也會被標，要人判斷。\n\n')
        for (b, name), fs in sorted(flags.items()):
            f.write(f'## {b} {name}\n' + ''.join(f'- {s}\n' for s in fs) + '\n')
    print(f'{" ".join(BS)}：共 {total} 件，被標 {len(flags)} 件 → {p}')

if __name__ == '__main__': main()
