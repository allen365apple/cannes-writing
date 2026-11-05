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
- 2026-11-04 02:50 收尾：寫完驗完 b029–b035（70 件，收 60、不收 10；b034 PARKING GARAGE RADIO 是驗收員改不收，待確認）。2017 累計驗完 36／65 批（verified.txt 含 b065）。待決新增 21 件（見 pending_decisions.md；重複候選 3 件：b031 08912／b061 09212、b032 08921／b023 08826、b035 08946／b014 08730；【爭議】0 件）。連不上：lovethework 卡片沒內文；sites.wpp.com、lbbonline、adnews.com.au、lucianogriessi.com 網域解析不到；adsspot、adforum、The Drum、Behance、Creativepool、adobo、campaignbrief、Communication Arts 等 403／503；Ads of the World、Vimeo 要人機驗證。沒撞到額度。
- 問題：無違規（沒有 rm、偽裝標頭、weserv；寫手與驗收員都有跑 check_batches.py）。b029–b032 驗收員誤下一次唯讀 git diff，沒改動。最後一次 push 網路卡住，重推成功。

## 2026-11-04 雲端第二輪
- 2026-11-04 14:10 開工：b036 b037 b038 b039 b040 b041 b042
- 2026-11-04 14:30 收尾：寫完驗完 b036–b042（70 件，全收；Messi, Leave 08988 驗收員建議改不收，decision 沒動）。2017 累計驗完 43／65 批（verified.txt 含 b065）。待決新增 12 件（見 pending_decisions.md；重複候選 0 件，另有 b041 09011 一筆併兩個點子待決定是否拆件；【爭議】0 件）。連不上：lovethework 卡片多半沒內文；Behance、adsspot、AdForum、LBB、The Drum、Design Week、Clios、Luerzer's、La Réclame 等 403／404／503；sites.wpp.com、adnews.com.au、blog.artscase.com 網域解析不到；YouTube、Vimeo 要人機驗證；adsoftheworld 用 curl 回 405（改 WebFetch 可讀）。沒撞到額度。
- 問題：無違規（沒有 rm、偽裝標頭、weserv；寫手與驗收員都有跑 check_batches.py）。b037 寫手自述沒有人工重讀一句話與讀稿，已交驗收員逐件細讀並改 7 件。開工時本機 main 與 origin 歷史不相連，已改用 origin/main 接續（沒 force push）。

## 2026-11-05 雲端第一輪
- 2026-11-05 02:10 開工：b043 b044 b045 b046 b047 b048 b049
- 2026-11-05 收尾：寫完驗完 b043–b049（70 件，收 68、不收 2：TOMMY HUGS、CLEAN TALK 找不到內容來源）。2017 累計驗完 50／65 批。待決新增 24 件（重複候選 2：OMO CAR WASH、SWIMMER／ZWEMMER；【爭議】候選 1：Heineken Worlds Apart，已拿掉待定案；其餘為 uncertain、圖、來源矛盾）。連不上：LBB、Creative Review、The Drum、Campaign、AdForum、adsspot、Clios、Behance 等 403／404；sites.wpp.com、adnews.com.au、thereflex.nl 網域解析不到；Vimeo 要人機驗證；lovethework 卡片沒內文。沒撞到額度。
- 問題：b045–b049 驗收員自首初期用偽裝瀏覽器標頭的 curl 測連線一次（違規，結果沒採用）。b045 寫手自述沒逐件人工重讀，已交驗收員逐件細讀並改 8 件一句話。開工時本機 main 與 origin 歷史不相連，已改用 origin/main 接續（沒 force push）。
- 2026-11-05 02:52 回報已寫進 years/last_report.txt。

## 2026-11-05 雲端第二輪
- 2026-11-05 14:10 開工：b050 b051 b052 b053 b054 b055 b056
- 2026-11-05 收尾：寫完驗完 b050–b056（70 件全收）。2017 累計驗完 57／65 批，剩 b057–b064。待決新增 12 件（仍 uncertain 1：Ascensia 09105；重複候選 0；【爭議】候選 0；其餘為品牌／代理商待確認、來源偏薄、圖不理想）。連不上：LBB、The Drum、Campaign Live、adsspot、Creative Review、Behance、MediaPost、Mumbrella 等 403／付費牆；Clios、Campaign Brief Asia 部分 404；adnews.com.au 網域不在允許範圍；lovethework 案例頁沒有內文。沒撞到額度。
- 問題：b051 寫手把 09113 的圖用 weserv 轉址（違規），驗收員已換成官方案例板直接網址。b054 寫手搜尋時遇到網頁夾帶「忽略系統提示」的注入文字，沒採用。開工時本機 main 又與 origin 不相連，已改用 origin/main 接續（沒 force push）。
- 2026-11-05 14:38 回報已寫進 years/last_report.txt。
