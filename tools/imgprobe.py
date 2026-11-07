# 圖片體檢（2026-11-07 建立）：下載一張圖，回報尺寸與「看起來不能用」的原因。check_images.py 與 check_batches.py 共用。
# 不需要 PIL：從檔頭讀 PNG／JPEG／GIF／WebP 的尺寸；有 PIL 就順便看是不是幾乎全黑或單色。
import io, re, struct, urllib.request

UA = {'User-Agent': 'Mozilla/5.0'}  # 跟 check_batches 同一個內建標頭（工具內建，寫手不要自己加）
MIN_SIDE = 600          # 長邊小於這個就太小
MAX_BYTES = 5 * 1024 * 1024


def _size(b):
    if b[:8] == b'\x89PNG\r\n\x1a\n' and len(b) >= 24:
        return struct.unpack('>II', b[16:24])
    if b[:6] in (b'GIF87a', b'GIF89a'):
        return struct.unpack('<HH', b[6:10])
    if b[:4] == b'RIFF' and b[8:12] == b'WEBP':
        c = b[12:16]
        if c == b'VP8X': return (int.from_bytes(b[24:27], 'little') + 1, int.from_bytes(b[27:30], 'little') + 1)
        if c == b'VP8 ': return (struct.unpack('<H', b[26:28])[0] & 0x3fff, struct.unpack('<H', b[28:30])[0] & 0x3fff)
        if c == b'VP8L':
            v = int.from_bytes(b[21:25], 'little'); return ((v & 0x3fff) + 1, ((v >> 14) & 0x3fff) + 1)
    if b[:2] == b'\xff\xd8':
        i = 2
        while i + 9 < len(b):
            if b[i] != 0xff: i += 1; continue
            m = b[i + 1]
            if m in (0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf):
                h, w = struct.unpack('>HH', b[i + 5:i + 9]); return (w, h)
            if m in (0xd8, 0x01) or 0xd0 <= m <= 0xd7: i += 2; continue
            i += 2 + struct.unpack('>H', b[i + 2:i + 4])[0]
    return None


def probe(url, timeout=25):
    """回傳 (問題列表, 資訊字串)。問題列表空＝看起來可用（仍要人眼確認是不是這件作品）。"""
    if re.search(r'\.svg(\?|$)|placeholder', url, re.I): return (['是預留圖或 SVG 圖示'], '')
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            ct = r.headers.get('Content-Type', ''); b = r.read(MAX_BYTES + 1)
    except Exception as e:
        return ([f'下載失敗（{str(e)[:50]}）'], '')
    probs = []
    if len(b) > MAX_BYTES: probs.append('超過 5MB')
    wh = _size(b)
    if not wh:
        probs.append(f'讀不出圖片尺寸（{ct or "未知格式"}）')
        return (probs, f'{len(b) // 1024}KB')
    w, h = wh; info = f'{w}×{h}，{len(b) // 1024}KB'
    if not ct.startswith('image/'): probs.append(f'主機回 {ct or "沒有格式"}（可用 weserv 轉 JPEG）')
    if max(w, h) < MIN_SIDE: probs.append(f'太小（{w}×{h}）')
    if w * h and len(b) / (w * h) < 0.02: probs.append('檔案極小、疑似全黑或單色')
    try:
        from PIL import Image, ImageStat
        im = Image.open(io.BytesIO(b)).convert('L'); im.thumbnail((200, 200)); st = ImageStat.Stat(im)
        if st.stddev[0] < 6: probs.append('幾乎單色（疑似全黑／全白）')
    except Exception:
        pass
    return (probs, info)
