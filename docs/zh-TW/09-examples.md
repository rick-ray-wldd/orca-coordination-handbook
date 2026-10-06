# 第 9 章　日常實例：網站A 與 研究B

[English](../en/09-examples.md) | [繁體中文](../zh-TW/09-examples.md) | [Home](../../README.md)

以下兩個案例完全虛構，用來示範一件事如何走完整條鏈。所有 ID、路徑、網址都是人造的。

設定：

- 總控 A（Claude Code）督導 `web_sites`、`infra_ops`；總控 B（Codex CLI）督導 `research`、`triage`。
- 每個領域的 reviewer 是另一位總控。
- 網站A 是一個 git repo（`PROJECT_ROOT_A`），有一個平常負責文案的聊天室「網站A-主」。
- 研究B 還不存在。

---

## 案例一：網站A 的首頁改版

### 1. User 提出

> 「幫我把網站A 首頁的活動區塊換成下個月的三場活動，資料在 events.csv。改好給我看，先不要上線。」

### 2. 總控 A 判斷並宣告

路由：專案規則命中「網站A → web_sites」，督導是 A、核對是 B。

A 查聊天室狀態：「網站A-主」閒置、輸入框空、預覽沒有錯誤；但這次要改程式碼，且另一個 worktree 正在做導覽列重構。

```
判斷：④ 開新 worktree｜網站A｜要改首頁程式碼，且導覽列重構正在另一個 worktree 進行，需要隔離
```

### 3. 登記任務

```
T-EXAMPLE0101｜網站A 首頁活動區塊改版｜owner: S-EXAMPLE-WEBA-2｜priority 2｜due 2099-01-15 (target)
next: writer 依 events.csv 改活動區塊並附截圖與測試輸出
source: User 當日請求
```

### 4. 派工（節錄，完整格式見 `templates/zh-TW/dispatch-message.md`）

```
【User 原始需求】幫我把網站A 首頁的活動區塊換成下個月的三場活動，資料在 events.csv。改好給我看，先不要上線。
【成功條件】首頁活動區塊顯示 events.csv 中的三場；手機與桌面寬度都不跑版；既有測試全過。
【可讀】PROJECT_ROOT_A 全部
【可寫】PROJECT_ROOT_A 的新 worktree 內 src/sections/events/ 與 receipts/web-a-events-2099-01/
【禁止】部署、push 到遠端、合併主分支、寄信、公開分享、付款、建帳號、改其他專案
【代理與終端】不可開新終端、不可啟動其他代理；最大併發 1；只用既有訂閱
【交付證據】測試輸出、手機與桌面截圖、改動檔案清單與 SHA-256
【完成後】回報自己的站台，狀態 review
```

A 使用：

```
orca worktree create --name web-a-events --no-parent --agent claude --prompt "<上面的派工訊息>" --json
```

並把回傳的 worktree id 與 terminal handle 記在任務的 next。

### 5. writer 製作與回報

writer 完成後寫卡片 comment，並回報：

```
狀態：review
摘要：活動區塊改為三場；新增 2 個元件測試；全部 48 個測試通過
下一步：請核對 receipts/web-a-events-2099-01/
證據：receipts/web-a-events-2099-01/REPORT.md（含截圖、測試輸出、檔案 hash）
```

### 6. 獨立審查（總控 B）

A 更新任務 next：「請 B 核對 receipts/web-a-events-2099-01/，版本 commit abc1234」。

B 用 `templates/zh-TW/review-request.md` 派一個**唯讀**審查（或自己唯讀核對），報告：

```
審查對象：commit abc1234
問題 1｜中｜src/sections/events/Card.tsx 第 40 行｜日期用了 UTC，活動當天晚上會顯示成隔天｜建議改用本地時區格式化
其餘：無問題
```

A 抽樣確認問題 1 屬實，交回**原 writer** 修改（不另開 writer）。修改後產生新 commit def5678，B 對差異重審，結論：無問題。

A 記錄：

```
task-update T-EXAMPLE0101 --state review --evidence receipts/web-a-events-2099-01/REPORT.md
  --next "等 User 看預覽；已由 B 對 def5678 核對"
```

### 7. User 驗收

A 把本機預覽方式與截圖給 User。User 說：「內容可以。上線時間我再決定。」

A 記錄 `done`、`reviewer=user_confirmed`、review-note「User 於當日在對話中確認內容（commit def5678）；上線另案」。並另登記一個任務「網站A 活動區塊上線」，狀態 `waiting_user`，因為**上線是對外動作**，目前還沒有授權。

> 對照：如果 User 當時說的是「可以，下週一上午把 def5678 上線」，那就是範圍、版本、時間都明確的授權。A 應把上線任務記為「已授權、排定下週一上午執行」，到時照做並回報，**不需要再問一次**；只有當版本變了、時間不明或範圍擴大時，才回頭確認缺少的那一項。

---

## 案例二：研究B（全新主題）

### 1. User 提出

> 「我想研究一下『小型團隊用的離線同步方案』，整理比較表，下週要用。」

### 2. 總控判斷

收件的是總控 A。路由查詢：沒有專案規則命中；關鍵字「研究」命中 `research` 領域 → 督導是 **B**。

A 不自己做，也不直接對任何聊天室送輸入（不是它的領域）。A 回覆 User：

```
判斷：⑤ 開新專案｜研究B（由 B 督導）｜全新主題，現有專案都對應不上；已轉交 B
```

並用 `templates/zh-TW/handoff.md` 寫一份簡短交接放進 `receipts/research-b-intake-2099-01/`，通知 B。

### 3. 總控 B 接手

B 讀完交接檔後才接手，建新專案資料夾 `PROJECT_ROOT_B`（非 git，一般資料夾），在路由表登記「研究B → research」，然後：

```
判斷：③ 在原專案開新聊天室｜研究B｜新專案尚無聊天室
```

派工訊息重點：

- 可寫只有 `PROJECT_ROOT_B/`
- 只能用公開資料；**不得**把 User 的私人筆記或帳號資訊交給第三方模型 API
- 可以開瀏覽器查公開文件；不可註冊任何服務、不可下載付費報告
- 交付：比較表 Markdown ＋ 每一列的來源連結 ＋ 「未能核實」清單

### 4. 中途需要 User 決定

writer 發現兩種範圍定義差很多，回報 `waiting_user`。B 用 `templates/zh-TW/decision-record.md` 整理：

```
決策 D-EXAMPLE-07｜比較範圍
選項 1：只比開源方案（較快，約 6 項）
選項 2：含商用方案（較完整，約 12 項，部分需要試用帳號 → 需你另行授權）
建議：選項 1，商用另案
```

卡片顯示「⚠等你」。User 選 1。B 記錄決定與時間，任務回到 `working`。

### 5. 總控暫停時

隔天總控 B 額度用完，User 說「B 今天休息」。路由設定 B 不可用、附回來時間；查詢時 `research` 的代理督導變成 A。A 只做督導必要的事（回答 writer 的問題、整理證據），不改 B 的分工設計。B 回來後，A 用交接模板把當天狀態交回。

### 6. writer 聊天室斷線

writer 聊天室顯示重連失敗。負責恢復的是**維運領域督導 A**（不論研究B 歸誰）。A 照 `templates/zh-TW/resume-recovery-checklist.md`：確認閒置 → 保存畫面到私人收據 → 用原 session UUID 恢復、保留原模型與權限 → 重新取 handle → 通知 B。

### 7. 交付與審查

writer 交付比較表，B 請 A 審查（A 是 `research` 的 reviewer）。A 只讀核對：抽查 3 個來源連結、確認「未能核實」清單完整。結論綁定檔案 SHA-256。B 記 `coordinator_review`，交給 User。User 看過說可以 → `user_confirmed`。

---

## 兩個案例的共同點

1. 第一行永遠是判斷宣告。
2. 只有一個 writer；問題交回原 writer。
3. 審查綁定版本，版本變了就重審。
4. User 確認與對外動作是兩件事。
5. 不屬於自己領域的事，轉給該領域督導，而不是自己去送輸入。
