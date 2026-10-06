# 任務卡（範本）

> 沒有自製 CLI 時，在 `HUB_ROOT/tasks.md` 用這個格式登記。只登記需要跨回合追蹤的事。

```
## <T-EXAMPLE0000>｜<一句話標題>
- 專案：<P-EXAMPLE-XXX>　領域：<domain>　督導：<A/B>　核對：<B/A>
- owner（站台）：<S-EXAMPLE-X>
- 狀態：<inbox|planned|working|blocked|waiting_user|review|done|paused|cancelled>　revision：<n>
- 優先序：<1|2|3>
- 期限：<YYYY-MM-DD>（<target|confirmed_deadline|source_unverified>）
- 來源：<User 何時哪句話／哪份文件>
- next：<下一個可執行的具體步驟>
- 阻塞：<無／具體原因>
- 決策：<無／D-EXAMPLE-00>
- 證據：<路徑；review/done 必填>
- 審查：<無／review-note：…；reviewer：coordinator_review|user_confirmed>
- 歷史：
  - <YYYY-MM-DD> 建立（inbox）
  - <YYYY-MM-DD> 派給 <工作區/聊天室>（working）
```

## 狀態轉換規則

| 轉到 | 需要 |
|---|---|
| review | 證據路徑 |
| done | 證據 ＋ review-note ＋ reviewer；`user_confirmed` 只在 User 真的確認後 |
| blocked | 具體阻塞 |
| waiting_user | 決策紀錄或明確寫出要 User 做什麼 |
| paused → 其他 | 只有 User 說可以恢復 |

每次修改把 revision 加 1；修改前確認你讀到的是最新 revision。
