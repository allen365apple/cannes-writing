# cannes-writing：坎城得獎案例的雲端寫稿區

這個專案只做「寫稿＋驗收」。整理的是網路上公開的坎城獅子獎得獎作品資料，用繁體中文寫成創意案例稿。
上線到資料庫、同步圖書館不在這裡做，由維護者的電腦把 years/ 的稿收回去處理。

## 結構
- rules/writer_rules_card.md：寫稿規則（唯一要讀的規則）
- briefs/sonnet_write.md：寫手派工說明；briefs/opus_verify.md：驗收員派工說明；briefs/cloud_daily.md：每天的流程
- tools/check_batches.py：驗收前的程式檢查
- examples/b030_out.json：範本
- years/y<年>/：bNNN_in.json（輸入）、bNNN_out.json（稿）、verified.txt（驗完的批號，一行一個）、cloud_log.md（每天紀錄）、pending_decisions.md（待決事項）

## 鐵則
- 全程繁體中文。
- 不用 rm 或任何刪檔指令；用不到的檔搬到 tmp_ 資料夾。
- tmp_*／ 不上傳（.gitignore 已排除）。
- 不改 bNNN_in.json，不改別年的檔；不在 Slack、Email 發訊息；不寫 Google。
- 推送：只 commit years/、不 force push。
