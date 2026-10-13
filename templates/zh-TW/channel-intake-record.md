# 專屬頻道綁定與收據紀錄表

這是不可執行的設計示意，不是 gateway 設定、schema 或已安裝服務。所有 EXAMPLE 值皆為虛構。填寫後的紀錄留在私人環境，公開副本不得加入憑證或原始對話。

## 操作者維護的綁定（聊天不可修改）

- 綁定版本：EXAMPLE-REVISION
- 平台／profile：Discord／預設個人入口
- 允許的伺服器／頻道：SERVER-EXAMPLE / CHANNEL-EXAMPLE
- 已驗證擁有者：OWNER-EXAMPLE（拒絕其他成員、bot、webhook 與系統訊息）
- 原生專案 ID：NATIVE-PROJECT-EXAMPLE
- 獨立的私人帳本專案 ID：P-EXAMPLE-PROJECT
- 核准工作區：PROJECT_ROOT
- 固定來源：STATUS.md；NOTES.md（示意；操作者須核對實際檔案與新鮮度）
- 督導路由：COORDINATOR-EXAMPLE；目前 mailbox／terminal 綁定驗證：UNKNOWN
- 初始 writer owner：UNASSIGNED（之後指定的站台必須屬於帳本專案）
- 支援輸入：伺服器頻道中直接發文字，不必 mention；不支援討論串／斜線指令
- 跨專案輸入：引導擁有者到正確頻道，不自動轉送
- 附件政策：僅安全 metadata；擴充不讀取／執行內容或交給模型；上游 adapter 仍可能快取

## 一則來源訊息，一筆收件紀錄

- 收據：RECEIPT-EXAMPLE
- 穩定來源 key：PLATFORM-EXAMPLE / CHANNEL-EXAMPLE / MESSAGE-EXAMPLE
- 穩定任務 key：INTAKE-EXAMPLE（恢復時沿用）
- 清理後的需求摘要與私人來源參照：TO-BE-RECORDED
- 行動意圖判斷：簡單規則／關鍵字；總控必須閱讀真正意圖
- 暫停／不要執行：YES；明確變更前保留
- 帳本任務回執：NOT-YET-CREATED
- 通知：PENDING（尚未送出）；原生 mailbox 回執：NONE
- 對話回覆投遞：NOT-ATTEMPTED（與通知分開）
- 總控已讀／接單證據：NONE / NONE
- 原生執行 Run / Task / Dispatch：NONE / NONE / NONE
- writer 結果／固定版本審查／User 驗收：NONE / NONE / NONE
- 對外動作：NONE；需要限定範圍的授權與有權的執行者

## 恢復與驗證

待滿足前提：TO-BE-RECORDED。送出結果若變成 UNKNOWN，重試前先核對該筆傳輸回執，不要求重送訊息或重建任務。總控 session 替換後重新驗證綁定。督導路由與專案 writer 歸屬分開。

重載前：檢查進行中工作、回覆、待處理訊息、arrival spool 與 lock。正常重載後：驗證載入 hash、連線與無關 LINE profile 仍保留。合成測試、真實模型呼叫、真人問答、操作者恢復、全新端到端交辦各自記錄證據；未知層級保持未知。
