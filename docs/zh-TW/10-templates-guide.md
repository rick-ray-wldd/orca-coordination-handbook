# 第 10 章　模板索引與用法

[English](../en/10-templates-guide.md) | [繁體中文](../zh-TW/10-templates-guide.md) | [Home](../../README.md)

所有模板都在 `templates/zh-TW/` 資料夾，純文字，可以直接複製。`<尖括號>` 是要替換的佔位字。離線 HTML 版與 PDF 版的附錄也收錄了全文。

| 檔案 | 用途 | 誰用 | 何時 |
|---|---|---|---|
| [AGENTS.example.md](../../templates/zh-TW/AGENTS.example.md) | 總控與專案聊天室的規則檔範本 | 放在 `HUB_ROOT` 與各專案根目錄 | 採用第 1 級時 |
| [CONTRACT.example.md](../../templates/zh-TW/CONTRACT.example.md) | 兩位總控與所有站台共用的契約 | 所有代理在新對話開始時讀 | 採用第 1 級時；改版時通知重讀 |
| [routing.example.json](../../templates/zh-TW/routing.example.json) | 匿名路由表：領域、優先序、派工政策、資料界線 | 總控查詢；User 調整 | 採用第 1 級時 |
| [task-card.md](../../templates/zh-TW/task-card.md) | 任務登記格式（沒有自製 CLI 時用） | 總控 | 收件時 |
| [dispatch-message.md](../../templates/zh-TW/dispatch-message.md) | 派工訊息，含五項必含內容 | 督導總控 | 每次 ②③④⑤ |
| [station-report.md](../../templates/zh-TW/station-report.md) | 站台回報格式 | writer、總控 | 開始實質工作、重要成果、阻塞、交付 |
| [handoff.md](../../templates/zh-TW/handoff.md) | 跨總控或跨聊天室交接 | 交出方 | 換人接手時 |
| [review-request.md](../../templates/zh-TW/review-request.md) | 審查派工（只讀、綁版本） | 督導或核對總控 | 交付後 |
| [review-report.md](../../templates/zh-TW/review-report.md) | 審查報告（結構化、標嚴重度） | 審查者 | 審查完成時 |
| [decision-record.md](../../templates/zh-TW/decision-record.md) | 需要 User 決定的事 | 總控 | 出現 `waiting_user` 時 |
| [resume-recovery-checklist.md](../../templates/zh-TW/resume-recovery-checklist.md) | 斷線恢復步驟 | 維運領域督導 | 聊天室失效時 |
| [delivery-receipt.md](../../templates/zh-TW/delivery-receipt.md) | 收據資料夾的說明檔 | writer | 交付時 |
| [pre-share-checklist.md](../../templates/zh-TW/pre-share-checklist.md) | 分享前去識別化清單 | 任何要把文件給別人的人 | 分享前 |

## 使用要點

- **不要刪掉「禁止事項」欄**，即使這次看起來用不到。空著代表沒想過，寫「無對外動作」代表想過了。
- **證據欄要寫路徑**，不要寫「已測試」。
- **模板是起點**。你的領域、上限、模型分層都應該改成自己的。
- 改過的模板如果要分享給別人，先過第 12 章的檢查。

專屬頻道設計另用 [channel-intake-record.md](../../templates/zh-TW/channel-intake-record.md)：操作者填寫匿名綁定、收件與投遞證據，不可執行、不是 gateway 設定檔（第 16 章）。
