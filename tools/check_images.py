# 寫稿前的圖片體檢：python3 tools/check_images.py <年> [<批號> …]   例：python3 tools/check_images.py 2016 b015 b016
# 2026-11-07 建立（2017 檢討第 4 點：官方 case board 常是別件作品、全黑、太小或只是圖示，寫手每件重找很費工）。
# 只讀 in 檔、不改。把每件 image_candidates 下載體檢，結果寫到 years/y<年>/checks/images_<批號>.md。
# 寫手開工先看這份：標「不能用」的候選直接跳過，整件都沒可用候選的要自己找圖；看起來可用的仍要打開確認是這件作品。
# 不給批號＝這一年所有還沒有 out 檔的批。
import json, os, re, sys, glob, datetime, concurrent.futures as cf
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from imgprobe import probe

av = sys.argv[1:]
if not av or not re.fullmatch(r'\d{4}', av[0]) or not all(re.fullmatch(r'b\d{3}', b) for b in av[1:]):
    sys.exit('用法：python3 tools/check_images.py <年> [<批號> …]')
Y = av[0]; O = f'{here}/../years/y{Y}'
BS = av[1:] or sorted(os.path.basename(p)[:4] for p in glob.glob(f'{O}/b???_in.json') if not os.path.exists(p.replace('_in', '_out')))


def one(b):
    items = json.load(open(f'{O}/{b}_in.json'))
    jobs = [(x, u) for x in items for u in (x.get('image_candidates') or [])]
    with cf.ThreadPoolExecutor(8) as ex:
        res = dict(zip([u for _, u in jobs], ex.map(lambda t: probe(t[1]), jobs)))
    lines = [f'# {Y} {b} 圖片體檢（{datetime.datetime.now():%Y-%m-%d %H:%M}）', '',
             '「可用？」只代表檔案本身沒問題，還是要打開看是不是這件作品、看不看得出點子。', '']
    none_ok = 0
    for x in items:
        cs = x.get('image_candidates') or []
        ok = [u for u in cs if not res[u][0]]
        if not ok: none_ok += 1
        lines.append(f'## {x["id"]} {x.get("title") or ""}' + ('　**沒有可用的候選圖，要自己找**' if not ok else ''))
        for u in cs:
            p, info = res[u]
            lines.append(f'- {"✗ " + "；".join(p) if p else "○ 可用？"}（{info}）{"〔官方 case board〕" if "/conversion/" in u else ""} {u}')
        if not cs: lines.append('- 沒有候選圖')
        lines.append('')
    os.makedirs(f'{O}/checks', exist_ok=True)
    open(f'{O}/checks/images_{b}.md', 'w', encoding='utf-8').write('\n'.join(lines))
    return f'{b}：{len(items)} 件，{none_ok} 件沒有可用候選圖'


for b in BS: print(one(b))
