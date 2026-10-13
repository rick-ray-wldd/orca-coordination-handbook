# 第 8 章　從零開始採用

[English](../en/08-adoption.md) | [繁體中文](../zh-TW/08-adoption.md) | [Home](../../README.md)

不需要一次做完。建議分四級，每一級都能單獨運作。

## 第 0 級：準備（半小時）

本公開版可先用 Python 3.10+ 從 repo 根目錄執行：

```sh
python3 scripts/init_workspace.py --dest ../my-assistant --language zh-TW
```

目的地必須尚不存在，工具拒絕覆寫。只複製規則、契約、路由、13 份模板並建立私人任務表；不啟動 Orca、模型、排程或帳號連線。英文用 `--language en`。使用前先替換佔位字。無 Python 也可依下一節手動複製。


1. 安裝並開啟 Orca，確認 CLI 可用：

   ```
   orca --version
   orca status --json
   orca skills list
   orca skills get orca-cli
   orca skills get orchestration
   ```

   本手冊核對的是 macOS 上的 1.4.220 版；你的版本若不同，**以你自己的 `--help` 與 `skills get` 輸出為準**。其他平台或開發版的可執行檔名稱可能不同（例如開發版、WSL、遠端環境），請依該版本 skill 文件的說明找出正確的 Orca CLI；在 Linux 上，裸的 `orca` 也可能是同名的其他程式（例如螢幕閱讀器），不要直接照貼。

2. 建一個個人總控工作區 `HUB_ROOT`（一般資料夾即可，不必是 git），結構建議：

   ```
   HUB_ROOT/
     AGENTS.md            ← 總控規則（Codex 讀）
     CLAUDE.md            ← 同內容（Claude 讀；可以是同一份檔案的連結）
     coordination/
       CONTRACT.md        ← 共同契約
       routing.json       ← 路由表
     receipts/            ← 交付證據、交接、審查報告（私人）
     tasks.md             ← 沒有自製 CLI 時的任務表
   ```

3. 決定兩位總控：例如一個 Claude Code 聊天室、一個 Codex CLI 聊天室，都開在 `HUB_ROOT`。

## 第 1 級：純文件流程（第一天）

不寫任何程式，只用模板。

1. 複製 `templates/zh-TW/AGENTS.example.md` 成 `HUB_ROOT/AGENTS.md` 與 `CLAUDE.md`，把 `<...>` 佔位字換成你的設定。
2. 複製 `templates/zh-TW/CONTRACT.example.md` 成 `HUB_ROOT/coordination/CONTRACT.md`。
3. 複製 `templates/zh-TW/routing.example.json`，列出你自己的領域（建議一開始 3–5 個），每個領域指定 primary 與 reviewer。
4. 在 `tasks.md` 用 `templates/zh-TW/task-card.md` 的格式登記任務。
5. 每次派工用 `templates/zh-TW/dispatch-message.md`；每次交付要求 writer 用 `templates/zh-TW/station-report.md` 回報。
6. 每次判斷在 `receipts/dispatch-log.md` 加一行。

這一級所有能力都是〔規約〕。它已經能帶來最大的好處：**宣告判斷、單一 writer、證據、獨立審查、User 驗收分開記錄**。

## 第 2 級：用 Orca 原生功能補強（第一週）

1. **看板**：請每個專案聊天室在檢查點寫卡片 comment，交付時把卡片移到 in-review：

   ```
   orca worktree set --worktree active --comment "<一句話進度>" --json
   orca worktree set --worktree active --workspace-status in-review --json
   ```

2. **派工送出要確認**：

   先看輸入框是否空、聊天室是否閒置，再送出（`<...>` 都要換成實際值）：

   ```
   orca terminal list --json
   orca terminal read --terminal <handle> --json
   orca terminal send --terminal <handle> --text "<派工訊息>" --enter --wait-submit 10 --json
   ```

   看回執的 `turn_started`，而不是只看 `accepted`。沒有回應時**不要重送**；傳輸失敗不確定時，用回執給的 `--retry-request <id>` 重試同一個請求〔程式・原生〕。

3. **需要隔離的程式修改**用新 worktree：

   ```
   orca worktree create --name <任務名> --no-parent --agent codex --prompt "<派工訊息>" --json
   ```

4. **需要監督、等結果的多工作者任務**，改用原生 orchestration 監督迴圈（`run-create`、`worker-start`、`check --wait`、`worker_done`、`gate-create` 決策關卡）。每位總控保持一個長駐 Run、每案一個 Task，每批投遞都要 ack，並要求 `worker_done --report-path`（第 14 章）。細節請讀你自己版本的 `orca skills get orchestration`。

5. **定時工作**：Orca 有原生排程（`orca automations create --trigger <preset|cron|rrule> ...`），可用來做唯讀巡檢。參考部署用的是作業系統排程＋自製腳本，兩種方式本手冊都沒有替你設定〔未知：原生 automations 是否適合你的巡檢需求〕。

## 第 3 級：自製助理層（有需要再做）

當任務超過幾十件、純文件開始難追時，可以自己寫一個小 CLI。最小可行版本只需要：

| 功能 | 最小實作建議 |
|---|---|
| 資料庫 | 一個本機 SQLite 檔，加檔案鎖與 transaction；寫入前比對 revision |
| 共同契約確認 | 計算 `CONTRACT.md` 的 sha256；`join` 必須提供完全相同的 hash |
| 站台回報 | 每站一列；`review`／`done` 必附 evidence；`blocked` 必附 blocker |
| 任務 | `done` 必附 evidence ＋ review-note ＋ reviewer（只允許 `coordinator_review`／`user_confirmed`） |
| 路由 | 讀 `routing.json`，依第 4.4 節的先中先贏順序回傳領域與督導；寫入時加鎖、備份、版本號加一、changelog、驗證 |
| 看板同步 | 讀任務與回報，算出每張卡的欄位與 comment，只對有變化的卡呼叫 `orca worktree set`；預設試算 |
| 巡檢 | 一般程式收集事實 → 用不給工具的模型寫短摘要 → 寫 `LATEST.md` |
| 去敏 | 存進資料庫前把看起來像金鑰的字串遮掉 |

開發時注意：

- 收集程式**唯讀**各專案來源；不讀 `.env`、金鑰、完整對話；不追 symlink；不執行來源文字。
- 產生的彙整檔（看板、摘要）標明是產生檔，不手改。
- 每個寫入路徑都要有自動測試；改資料儲存方式時驗證 transaction、既有資料保留、來源唯讀。

## 第 4 級：雙總控分工穩定運作

- 每週一次跑路由 `audit`（或人工檢查）：未分類、超量、失衡、過期的逐任務指定。
- 每月回顧派工紀錄：有多少行動型請求被總控自己做掉？①–⑤ 的比例合理嗎？
- 規則有改時，按第 7.6 節通知另一位總控重讀。

## 採用檢查清單

- [ ] `orca --version` 與 `orca skills get orca-cli` 能跑
- [ ] `HUB_ROOT` 有 AGENTS.md／CLAUDE.md／CONTRACT.md／routing.json
- [ ] 每個領域都有 primary 與（不同的）reviewer
- [ ] 兩位總控都在回覆第一行宣告判斷
- [ ] 派工訊息都含五項必含內容
- [ ] 交付都有證據，review 與 done 分開
- [ ] `user_confirmed` 只在 User 真的確認時記錄
- [ ] 對外動作都有 User 對該次的明確授權
- [ ] 恢復斷線只由一位負責，只用原 UUID
- [ ] 每位總控一個長駐 Run；投遞都有 ack；worker 報告連回帳本
- [ ] 秘密只放 keychain 或 stdin；代理不代填卡號、不建帳號、不繞過權限
- [ ] 同時活躍的聊天室數量在你的機器負荷內
