# 2016 雲端／本機紀錄

## 2026-11-06 本機
- 2026-11-06 01:00 本機認領：b055 b056 b057 b058 b059 b060 b061 b062 b063 b064（GPT 從後面往前寫，雲端從 b001 往後）
- 2026-11-06 01:20 本機認領：b047 b048 b049 b050 b051 b052 b053 b054（Sonnet）
- 2026-11-06 01:50 本機認領：b039 b040 b041 b042 b043 b044 b045 b046（GPT 第三線）
- 問題：b053 Sonnet 寫手試圖用 weserv 轉址放圖（被系統擋下，沒寫進稿）
- 2026-11-06 01:35 GPT 額度用完（out of credits），GPT 完成 b057 b058 b059 b061 b062 b063 b064；b060 b056 b055 b046–b039 仍由本機認領，改派 Sonnet
- 問題：b043 Sonnet 寫手一次用 curl 偽裝瀏覽器標頭抓 lovethework（只拿圖片網址核對，內容沒採用），已記在該件 note

## 2026-11-06 雲端第 1 輪
- 2026-11-06 02:10 開工：b001 b002 b003 b004 b005 b006 b007（雲端從 b001 往後；b039–b064 本機認領不碰）
- 更正：b042 那張是超過 5MB，已改用官方 CDN ?resize；b063 那張主機回 octet-stream，照規則卡用 weserv 是允許的（規則禁止的是用 weserv 抓被擋的網頁）。
- 2026-11-06 雲端第 1 輪收尾：寫完並驗完 b001–b007（7 批 70 件全收）；待決新增 16 件（【爭議】候選 4：Coop、Legally Bride、Cubetto、FALTER；不算爭議待確認 3；重複判斷 1；仍 uncertain 3：KFC、Dove、GASCALE；品牌待確認 1；圖不理想 4）。連不上：LBB、Campaign、The Drum、MediaPost、AdsSpot、Shots、Springwise 等 403，sites.wpp.com、adnews 不在允許網域。沒撞額度。寫手、驗收員無違規（沒 rm、沒偽裝標頭、沒 weserv）。合併時與本機推送的 verified.txt 衝突一次，兩邊都保留。

## 2026-11-06 雲端第 2 輪
- 2026-11-06 14:10 開工：b008 b009 b010 b011 b012 b013 b014（b039–b064 本機認領不碰）
- 2026-11-06 雲端第 2 輪收尾：寫完並驗完 b008–b014（7 批 70 件全收）。2016 累計驗完 37／64 批，剩 b015–b038（雲端）與 b039–b041（本機認領）。待決新增 17 件（重複候選 3：PARTY／TRIP／HAGGLERS、ROCKET CAR／WHALE 2016、NEVER ALONE 兩版；【爭議】候選 0；不算爭議待確認 2；品牌欄待確認 3；仍 uncertain 9），另有圖不理想數件。連不上：LBB、Campaign、The Drum、Adweek、MediaPost、Luerzer's、Shots 部分頁等 403，Brand Buffet 403，bigchop.co.uk 503，clios.com 失效，adnews 不在允許網域；lovethework 官方頁沒有內文。沒撞額度。
- 問題：b012–b014 驗收員自首曾一次用 curl 加瀏覽器 User-Agent 標頭（被權限系統擋下、沒送出，違規未遂），另跑過一次唯讀的 git diff --stat（違反「不要 git」）。b012 寫手遇到搜尋結果夾帶注入指令，沒照做。開工時本機 main 分支停在舊歷史、HEAD 是分離狀態，第一次推送被拒；已把 main 對齊 origin/main 後正常推送（沒 force push）。
- 2026-11-06 14:38 回報已寫進 years/last_report.txt。
- 2026-11-06 本機收尾：本機認領的 b039–b064 全部寫完驗完（其中 GPT 寫 7 批、Sonnet 寫 19 批，Opus 全驗）。b001–b038 留給雲端。
- 2026-11-06 柏文決定新規則（有爭議照收標【爭議】、只有坎城撤獎不收；重疊只收一筆），已改 out 檔與規則卡。雲端寫 b015、b033 時：WHALE 2016（08093）設 `重複`＋same_as ltwm-08052；TRIP（08274）設 `重複`＋same_as ltwm-08046，獎項併進保留那筆。
- 2026-11-07 02:10 開工：b015 b016 b017 b018 b019 b020 b021（雲端 2026-11-07 第 1 輪）
- 2026-11-07 雲端第 3 輪收尾：寫完並驗完 b015–b021（7 批 70 件，收 69、重複 1：WHALE 2016 併入 b011 ROCKET CAR，獎項已併）。2016 累計驗完 47／64 批，剩 b022–b038（雲端）。待決新增 18 件（重複候選 2：Clorox BIG BANG／GRAVITY、Geico 兩筆同系列；【爭議】1：Sainsbury's 1914 聖誕休戰；仍 uncertain 12；品牌／代理商欄待確認 2；in 檔連結錯 1）。連不上：sites.wpp.com、lbb.lbbonline.com、duvalguillaume.com、bestofogilvy.asia 網域無法解析；LBB、Campaign、The Drum、Adweek、Ad Age、AdForum、Luerzer's、La Réclame、adsspot、Behance 等 403；Clios 404；commarts 503；adnews 不在允許網域；lovethework 官方頁沒有內文。沒撞額度。
- 問題：b020 寫手曾一次嘗試用 weserv 轉址抓圖（被權限系統擋下、沒成功，違規未遂）。驗收員重跑 check_batches 覆寫報告（屬正常）。
- 2026-11-07 02:45 回報已寫進 years/last_report.txt。
- 2026-11-07 14:09 開工：b022 b023 b024 b025 b026 b027 b028（雲端 2026-11-07 第 2 輪）
- 2026-11-07 雲端第 4 輪收尾：寫完並驗完 b022–b028（7 批 70 件，收 68、不收 2：08170 GAME OF THRONES "SHAME"、08197 MOM AT 40 兩件廣播找不到內容來源）。2016 累計驗完 54／64 批，剩 b029–b038。待決新增 16 件（重複候選 3：HINTS／SPARE THE ACT、Give Extra 與官方 Sarah & Juan 卡片、Fabogesic MOVING／BREAK UP；不收待決 2；仍 uncertain 8；標題欄 1；圖 2 組）。【爭議】0、撤獎 0。連不上：sites.wpp.com、lbb.lbbonline.com、patrickbaron.com、kirano.me 網域無法解析；LBB、Campaign、The Drum、MediaPost、Behance、AdsSpot、Clios、Adweek 部分頁等 403／404；adnews 不在允許網域；Vimeo 要人機驗證；lovethework 官方頁沒有內文。沒撞額度。
- 問題：b024 寫手自首跑過一次唯讀的 git status（違反「不要 git」，沒改檔）。其餘寫手、驗收員沒用 rm、沒偽裝標頭、沒用 weserv。第一組 commit 時 b026–b028 尚未驗的稿一併被提交，驗完已再提交更新版。開工時本機是分離 HEAD，已把 main 對齊 origin/main（沒 force push）。
- 2026-11-07 11/07 14:36 回報已寫進 years/last_report.txt。
