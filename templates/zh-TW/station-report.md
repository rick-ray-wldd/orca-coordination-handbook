# 站台回報（範本）

> writer 與總控在「開始實質工作、重要成果、阻塞、決策變化、待驗收、交付」時使用。一般問答不必回報。只回報自己的站台。

```
【站台】<S-EXAMPLE-X>（<工作區>／<代理種類>）
【任務】<T-EXAMPLE0000>
【上次 revision】<n>（從 brief 或上次回報取得；衝突時先重讀）
【狀態】<inbox|planned|working|blocked|waiting_user|review|done|paused|cancelled>
【摘要】<本輪完成的具體成果；數字優先，例如「48 個測試通過」>
【下一步】<下一個可執行的具體步驟，例如「請 B 核對 receipts/xxx/（sha256=...）」>
【證據】<路徑1>；<路徑2>　← review／done 必填
【阻塞】<具體原因與需要誰做什麼>　← blocked 必填
【範圍外發現】<列出，不自行修改>
【驗收】未驗收（站台回報一律未驗收）
```

## 好與壞的例子

| 欄位 | 不好 | 好 |
|---|---|---|
| 摘要 | 已完成 | 活動區塊改為三場；新增 2 個測試；48/48 通過 |
| 下一步 | 繼續處理 | 請 B 核對 receipts/web-a-events-2099-01/REPORT.md（commit def5678） |
| 證據 | 已測試 | receipts/web-a-events-2099-01/test-output.txt |
| 阻塞 | 有問題 | events.csv 第 3 列缺日期，需要 User 提供 |
