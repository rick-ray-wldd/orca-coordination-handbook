# 附錄 A　能力標記總表

[English](../en/13-capability-matrix.md) | [繁體中文](../zh-TW/13-capability-matrix.md) | [Home](../../README.md)

撰寫日核對方式說明：

- **原生**：在 Orca CLI 1.4.220 執行 `orca --help`、各子命令 `--help`、`orca skills get orca-cli`、`orca skills get orchestration` 核對。
- **自製**：閱讀參考部署腳本的 `--help` 與實作原始碼、執行其內附單元測試（全數通過）、讀取系統排程設定（只看頻率與命令名稱，不讀任何秘密）。**這些腳本未隨附本包。**
- **規約**：出自參考部署的規則文件；沒有程式強制。
- **未知**：未核實，或隨版本變動。

| # | 能力 | 標記 | 核實方式／備註 |
|---|---|---|---|
| 1 | 建立工作區並在第一個終端啟動代理、送初始任務 | 程式・原生 | `orca worktree create --agent <id> --prompt <text>` |
| 2 | 列出、讀取（游標分頁）、等待、送入終端 | 程式・原生 | `orca terminal list/read/wait/send --help` |
| 3 | 送入回執分階段（input_accepted → turn_started）、`--wait-submit`、`--retry-request` | 程式・原生 | `orca terminal send --help`、orca-cli skill |
| 4 | 工作區看板欄位（預設四欄）與卡片 comment | 程式・原生 | `orca worktree set --help` |
| 5 | 一個工作區一張看板卡 | 程式・原生（觀察） | 參考部署觀察；版本可能改變 |
| 6 | orchestration Run／Task／Dispatch／訊息／決策關卡／受監督工作者 | 程式・原生 | `orca --help` Orchestration 段、orchestration skill |
| 7 | 訊息送出成功只代表持久排入，不代表已讀 | 程式・原生 | orchestration skill |
| 8 | 只填終端 handle 的收件人會被警告不保證持久送達 | 程式・原生（觀察） | 觀察自一次送出回執的 warning |
| 9 | 公開分享 artifacts 預設關閉、只有人能在 UI 打開 | 程式・原生 | orca-cli skill 的 Artifacts 段落 |
| 10 | 工作區休眠保留終端與代理恢復紀錄；關閉會移除 | 程式・原生 | orca-cli skill 的 Terminal rules |
| 11 | 原生排程 automations | 程式・原生 | `orca automations create --help`；是否適合當巡檢〔未知〕 |
| 12 | Agent Dashboard（逐聊天室狀態） | 未知 | 實驗功能，未核實 |
| 13 | 手機版介面能看到什麼 | 未知 | 未核實 |
| 14 | 用原 UUID 恢復對話 | 程式・原生（代理 CLI） | 具體旗標依你安裝版本的 `--help`〔細節未知〕 |
| 15 | 共同契約確認需提供完全相同的 sha256 | 程式・自製 | 實作讀過 |
| 16 | 未確認目前契約不能回報 | 程式・自製 | 實作讀過 |
| 17 | review／done 必附 evidence；blocked 必附 blocker | 程式・自製 | 實作讀過 |
| 18 | 任務 done 必附 review-note 與 reviewer（兩種之一） | 程式・自製 | 實作讀過 |
| 19 | revision 樂觀鎖、相同內容 no-op | 程式・自製 | 實作讀過 |
| 20 | 站台回報一律標「未驗收」 | 程式・自製 | 實作讀過 |
| 21 | 若提供任務 owner，必須屬於同專案（owner 可省略） | 程式・自製 | 實作讀過；「每個任務都有 owner」是規約 |
| 22 | 寫入前遮蔽像金鑰的字串 | 程式・自製 | 實作讀過 |
| 23 | 路由先中先贏（逐任務 → 專案 → 關鍵字 → 預設） | 程式・自製 | 實作讀過、單元測試 |
| 24 | 總控不可用時查詢結果改為核對者代理，到期自動恢復 | 程式・自製 | 實作讀過 |
| 25 | 路由寫入加鎖、備份、版本號、changelog、驗證失敗拒寫、expect-version | 程式・自製 | 實作讀過 |
| 26 | 派工建議 ①–⑤（關鍵字啟發式） | 程式・自製 | 實作讀過；只是建議 |
| 27 | 派工判斷記錄到 JSONL、巡檢統計並點名總控自己做 | 程式・自製 | 實作讀過；前提是有記錄 |
| 28 | 超量（max_working）、失衡比例警告 | 程式・自製 | 只警告 |
| 29 | 每 60 秒背景收集與看板同步 | 程式・自製 | 系統排程設定核實 |
| 30 | 看板同步預設試算、只寫有變化的卡、尊重手動拖動、不自動移入 completed | 程式・自製 | 實作讀過 |
| 31 | 每日 3 次唯讀巡檢，模型呼叫停用所有工具、有花費上限 | 程式・自製 | 排程設定與實作核實 |
| 32 | 每 30 分鐘健康檢查，超門檻才通知，3 小時冷卻 | 程式・自製 | 排程設定與實作核實 |
| 33 | 第一行宣告判斷 | 規約 | |
| 34 | 總控只能親自做三種事 | 規約 | |
| 35 | 派工訊息五項必含 | 規約 | 自製 triage 會產生骨架，但不檢查實際訊息 |
| 36 | 只有領域督導能對聊天室送輸入 | 規約 | Orca 不限制 |
| 37 | 斷線恢復集中由維運領域督導 | 規約 | |
| 38 | 同一 session 不得兩個 writer | 規約 | 用原生監督迴圈時有 Dispatch 權威可輔助 |
| 39 | 對外動作需 User 對該次的明確授權 | 規約 | |
| 40 | 代理文字、完全存取模式不新增授權 | 規約 | |
| 41 | 私人資料不交第三方模型 API | 規約 | |
| 42 | 審查只讀、結構化、標嚴重度、無問題直說 | 規約 | |
| 43 | 審查綁定產物 hash | 規約 | 無程式強制 |
| 44 | `user_confirmed` 不得代填 | 規約 | 程式只檢查欄位存在 |
| 45 | 規則更新後通知另一位總控重讀 | 規約＋原生 mailbox | 持久 status 訊息與閒置提醒；確認回覆是規約 |
| 46 | 不開無限輪詢 | 規約 | |
| 47 | 開工前先讀巡檢摘要 | 規約 | |
| 48 | 站台身份只做歸屬檢查（工作區、代理種類），不是防冒用的身份驗證 | 程式・自製（限制） | 實作讀過 |
| 49 | 背景同步加 `--ensure-rules` 時寫入／更新已登記工作區的規則入口檔（先備份） | 程式・自製 | 排程命令與實作核實 |
| 50 | 「尚未交叉核對」提醒只涵蓋一個指定領域、最高優先序、waiting_user／review 狀態 | 程式・自製 | 路由設定與實作核實；其他領域靠規約 |
| 51 | evidence 只檢查欄位非空，不驗證內容 | 程式・自製（限制） | 實作讀過 |
| 52 | 助理任務與原生 Run／Task／Dispatch 的對應 | 規約（無程式綁定，缺口） | evidence 附報告路徑與 run／task／dispatch ID；沒有程式綁定 |
| 53 | 一位總控只綁一個 Run；換綁會 fence 未 ack 的投遞 | 程式・原生 | 原始碼 `db/runs/run-binding.ts`、`db/messages/role-mailbox-delivery.ts` |
| 54 | mailbox 至少投遞一次；未 ack 的一批會重播 | 程式・原生 | `check --ack`；原始碼 `role-mailbox-delivery.ts` |
| 55 | 只在收件窗格閒置時打一行提醒 | 程式・原生 | 原始碼 `mailbox-pointer-delivery.ts`；沒綁 Run 時的行為未知 |
| 56 | `worker-start` 觀察到這一輪開始才回 ready | 程式・原生 | 否則回 `start_unknown`；原始碼 `worker-start-readiness-settlement.ts` |
| 57 | `worker_done` 附報告路徑／改動檔案；release 保存 transcript；`worker-read` | 程式・原生 | send help；原始碼 `worker-terminal-archive.ts` |
| 58 | 現行模型的 heartbeat 過期自動警告 | 程式・原生（缺口） | 只存在已退役的舊迴圈；參考部署用 30 分鐘檢查清單 |
| 59 | 每位總控一個長駐 Run、每案一個 Task | 規約 | 參考部署 2026-10 起的規則 |
| 60 | 秘密只經 keychain 或 stdin；不代填卡號、不建帳號、不繞過權限 | 規約 | 代理仍可能被誤用；憑證要放在它拿不到的地方 |
| 61 | 客戶訊息入口：驗簽＋allowlist 身份、零工具回覆、唯一只出預覽的提議工具 | 程式・自製 | 私人實作；離線測試斷言對外送出為零；未隨附 |
| 62 | 外部桌面代理（「dots」）只做非敏感工作 | 未知 | 評估中；尚未試辦；未上線 |

第 53–58 項另外對照同版 tag 的 Orca 開源原始碼（MIT）核對；路徑相對於該 repo。發布工具（`init_workspace.py`、驗證、文件建置與 release 打包）不在這 62 項之內，它們隨本 repo 附帶並有測試，但不實作私人助理層。
