# 斷線恢復清單（範本）

> 只由「維運領域」的督導執行，不論該聊天室屬於哪個領域。命令以你的 Orca 版本 `--help` 為準。

## 0. 判斷是否需要恢復

- [ ] 聊天室顯示重連失敗／無法還原／代理迴圈結束，或已退回 shell 提示字元
- [ ] 或 Orca 重啟後 handle 失效
- [ ] **不是**「只是一段時間沒輸出」——沒有回應不等於已結束

## 1. 確認可以動

- [ ] `orca terminal list --json` 找到該聊天室
- [ ] `orca terminal read --terminal <handle> --json`：確認不在工作中、User 沒有正在輸入
- [ ] 不是另一位總控自己的聊天室

## 2. 保存現況

- [ ] 把 `terminal read` 的輸出存到**私人**收據資料夾 `HUB_ROOT/receipts/recovery-<日期>/`（這是私人資料，不得分享）
- [ ] 記下原本的：session UUID、代理種類、模型、推理強度、權限模式、工作目錄

## 3. 恢復

- [ ] 確認該 session UUID 沒有在其他終端被恢復（避免兩個 writer）
- [ ] 用該代理 CLI 自己的 resume 功能，**只用原 UUID**，保留原模型／推理強度／權限
- [ ] 若需要新終端：`orca terminal create --worktree <selector> --command '<代理 resume 命令>' --json`
- [ ] `orca terminal wait --terminal <新handle> --for tui-idle --timeout-ms 60000 --json`，確認 `satisfied: true`

## 4. 收尾

- [ ] `orca terminal list --json` 取得新 handle；之後只用新 handle
- [ ] 確認聊天室記得原本的任務（必要時請它讀交接檔，而不是重貼整段歷史）
- [ ] 在收據資料夾寫一段：時間、原因、做了什麼、結果
- [ ] 通知該領域的督導（不要直接對該聊天室送新任務，除非你就是該領域督導）

## 不要做

- 不重開一個新 session 取代原 session（除非 User 同意且原 session 確定無法恢復）
- 不替聊天室送出它輸入框裡未送出的草稿
- 不升級或重啟 Orca
- 想之後再接著用的工作區，用 Orca 的休眠，不要關閉終端（關閉會移除恢復紀錄）
