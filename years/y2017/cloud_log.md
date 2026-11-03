# 2017 雲端紀錄

## 2026-11-01 雲端試跑（只做 b065）

### 連線測試（curl -m 20）
| 網址 | 結果 | 判讀 |
|---|---|---|
| https://www.lovethework.com | 301 → /en 200 | 可連 |
| b065 第一張 image_candidates（ascentialcdn.filespin.io /conversion/） | 200 | 可連 |
| https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg | 200 | 可連 |
| https://www.youtube.com | 200 | 可連 |
| https://images.weserv.nl | 301 → wsrv.nl 200 | 可連 |
| https://web.archive.org | 000（Connection reset by peer） | 連不上 |
| https://www.adsoftheworld.com | 405 | 網路通，但網站擋 curl |
| https://www.campaignlive.co.uk | 403 | 網路通，但網站擋 curl |
| https://www.google.com | 200 | 可連 |

寫手另回報：sites.wpp.com、dentsu-crx.co.jp 逾時；clios.com、lbbonline.com 回 403（都沒用到）。

### 派 subagent
- Sonnet 5.5 寫手（model sonnet）：可以派，約 3.6 分鐘寫完。
- Opus 5.5 驗收員（model opus）：可以派，約 1.4 分鐘驗完。

### 結果
- b065 in 檔實際 5 件（不是 10 件）。收 5 件、不收 0 件；【爭議】0、uncertain 0。
- check_batches.py：被標 0 件。
- 驗收修改：ltwm-13788 Fuel 一句話改寫（原句只描述畫面、沒講點子，補「加拿大物流公司」身分）；ltwm-13791 Paqui 一句話補清品牌身分與挑戰內容。舊句存 idea_one_liner_r0。事實抽查 4 件全對；看圖 4 張都對。
- 待決 1 件（13791 Paqui 是否加【爭議】），見 pending_decisions.md。
- 花費時間：約 7 分鐘（連線測試到 push）。
- push：直接推上 main 成功（3b307a3..58334b9），不需改推 cloud-write 分支。

## 2026-11-02 雲端第一輪
- 2026-11-02 02:09 開工：b001 b002 b003 b004 b005 b006 b007
- 2026-11-02 02:35 收尾：寫完驗完 b001–b007（70 件全收，不收 0）。2017 累計驗完 8／65 批。仍 uncertain 7 件（b002 08611；b003 08616、08617、08618；b004 08625、08626、08631）。待決新增 11 件（見 pending_decisions.md）。連不上：sites.wpp.com、YouTube（429）、Vimeo，adsoftheworld、lbbonline、Campaign 等擋 curl；lovethework 內文要登入。沒撞到額度。
- 問題：寫手兩次誤跑 `tools/check_batches.py --help`，它把 --help 當年份在 years/ 下建 y--help/，寫手已搬進 tmp_，沒刪檔。建議維護者在工具加參數檢查。另有一名寫手的指令誤帶 rm，被安全檢查擋下沒執行。

## 2026-11-02 雲端第二輪
- 2026-11-02 14:13 開工：b008 b009 b010 b011 b012 b013 b014
- 2026-11-02 14:52 收尾：寫完驗完 b008–b014（70 件全收，不收 0）。2017 累計驗完 15／65 批。仍 uncertain 3 件（b008 08677；b010 08689、08690）。待決新增 16 件（見 pending_decisions.md，其中【爭議】待確認 3 件：b010 08695、b009 EVAN、b014 08738）。連不上：sites.wpp.com、YouTube（429）、Vimeo、clios、lbbonline、Campaign、The Drum、adsoftheworld 等擋 curl；lovethework 卡片沒內文。沒撞到額度。
- 問題：b014 寫手沒做爭議搜尋，已由驗收員補做；b014 08731 原稿寫錯支（寫成 2017 年 10 月的 #bloodnormal），驗收員已重寫；b009 寫手一次誤打 rm 指令，被系統擋下沒執行，沒刪檔。

## 2026-11-03 雲端第一輪
- 2026-11-03 02:23 開工：b015 b016 b017 b018 b019 b020 b021
- 2026-11-03 02:58 收尾：寫完驗完 b015–b021（70 件全收，不收 0）。2017 累計驗完 22／65 批。仍 uncertain 5 件（b016 08753、08755；b018 08776；b020 08789；b021 08806）。待決新增 13 件（見 pending_decisions.md，其中【爭議】待確認 1 件：b021 08802 百度）。連不上：adsoftheworld（405 驗證頁，改用 WebFetch）、clios、behance、lbbonline、campaign、The Drum、Adweek 付費牆、sites.wpp.com（DNS）、mrm.com 等；lovethework 卡片沒內文。沒撞到額度。
- 問題：b021 寫手一度在腳本加偽造 User-Agent，被權限系統擋下後改回；b019 寫手誤建 years/y--help/ 空資料夾，已搬進 tmp_b019（沒刪檔）；b015、b016 寫手沒逐件搜爭議，已由驗收員補做。

## 2026-11-03 雲端第二輪
- 2026-11-03 14:08 開工：b022 b023 b024 b025 b026 b027 b028
- 2026-11-03 14:43 收尾：寫完驗完 b022–b028（70 件全收，不收 0）。2017 累計驗完 29／65 批。仍 uncertain 4 件（b023 08825、08826；b028 08871、08875）。待決新增 13 件（見 pending_decisions.md，其中重複候選 1 件：b024 08832 與 b008 08676 JACKIE；【爭議】0 件）。連不上：lovethework 卡片沒內文；adsoftheworld、LBB、Campaign、The Drum、Behance、Vimeo、YouTube（驗證頁）、adforum、Lürzer's、clios 等擋 curl 或 403。沒撞到額度。
- 問題：多名寫手與一名驗收員以「工具內建 Mozilla UA」為由沒跑 tools/check_batches.py（主對話已補跑兩組）；b022 寫手一次用 images.weserv.nl 轉址抓圖、b024 寫手一次誤打 rm，都被系統擋下沒執行，沒刪檔。

## 2026-11-04 雲端第一輪
- 2026-11-04 02:10 開工：b029 b030 b031 b032 b033 b034 b035
