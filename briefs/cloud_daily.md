# 每天的雲端流程（2026-11-01 建立）
# 雲端排程每天跑兩輪（台北 02:00、14:00）照這份做：每輪寫 7 批、驗完、推回 GitHub。所有路徑相對於本專案根目錄。全程繁體中文。

## 1. 開工
- `git pull`。years/current.txt 一行一個年份（由新到舊排隊，例 2017 再 2016）。由上往下找第一個「還有沒寫完批次」的年份 Y，O=years/y{Y}。沒寫完＝有 bNNN_in.json，但沒有 out、或 out 筆數比 in 少。
- 從 Y 由小到大取最多 7 批；Y 不夠 7 批就接著取下一個排隊年份的批次（每年各自照下面流程驗、各自記 cloud_log）。所有排隊年份都寫完 → 在最後一年的 O/cloud_log.md 記一行「全部寫完，等本機收尾／交下一年」，commit、push 後結束。
- 開工前先看 git log：若最近 3 小時內有別輪的「寫完驗完」commit 而且那輪的批次還沒全部進 verified.txt，代表上一輪可能還在跑——只取它沒碰的批次（cloud_log 最後一行會寫上一輪拿了哪些批）。開工時先在 cloud_log.md 記一行「<時間> 開工：<批號們>」並 commit＋push，讓下一輪看得到。

## 2. 寫
- 每批派一個 Sonnet 5.5 subagent，prompt＝「先完整讀 briefs/sonnet_write.md，照它寫 {Y} 的 <批號>（說明裡 {Y}＝{Y}、{B}＝<批號>），寫完照說明回報」。同時最多 4 個，有人寫完再補下一批。

## 3. 驗
- 每累積 3～4 批寫完，確認那幾批的寫手都已結束，跑 `python3 tools/check_batches.py {Y} <批號們>`，再派一個 Opus 5.5 subagent 照 briefs/opus_verify.md 驗這幾批（把 {Y}、{BATCHES} 換好）。同時進行的 subagent 總數不超過 5。
- 驗完把批號加進 O/verified.txt（一行一個），把寫手、驗收員回報裡的待決事項（補不起來的 uncertain、重複候選、【爭議】候選、圖不理想、違規）加進 O/pending_decisions.md（註明批號、id、建議）。不要自己改 decision。
- **每驗完一組就 commit＋push 一次**（只 add years/），訊息「{Y} <批號們> 寫完驗完」。push 被拒先 `git pull --rebase` 再推。

## 4. 結尾
- 在 O/cloud_log.md 記一行：日期、寫完／驗完哪些批、待決新增幾件、連不上的網站、撞到額度與否。commit＋push。
- 撞到額度上限就停在原處（寫一半的 out 檔也 commit 上去，下一輪接續）。
- 最後照排程指示發一則 Slack 私訊回報（對象寫在排程裡，不在本專案）。5 行內：年份、今天寫完／驗完哪些批（幾件）、該年累計幾批／總批數、待決新增幾件、出了什麼問題（沒有就寫「無」）。只發這一則，不發到頻道。

## 鐵則
- 不刪任何檔（subagent 也一樣）；只改 years/y{Y}；不改 bNNN_in.json。
- 除了結尾那一則 Slack 私訊，不發任何 Slack／Email；不寫 Google、不 force push。
