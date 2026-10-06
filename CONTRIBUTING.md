# Contributing

English is the primary edition. Traditional Chinese is a complete companion, not a summary. Preserve matching filenames across locales, update counterparts together, and state any translation gaps honestly in your pull request. See [translation policy](TRANSLATIONS.md).

1. Create a branch in your fork/template copy.
2. Edit Markdown or SVG source, not generated PDFs.
3. Keep examples fictional; never attach private receipts, real transcripts or credentials.
4. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.
5. For visual changes, rebuild and inspect both locales. Describe exactly what you checked.
6. Submit a focused pull request with problem, change, validation and limitations.

Native command claims need a version and primary evidence: installed Orca help or the guide returned by `orca skills get`. Do not label a convention as enforced. Preserve applicable user authorization and do not add unnecessary repeated approval steps.

Do not add external fonts, analytics or CDNs to the offline reader. Tool changes should remain small, portable, local and dependency-light. No unattended agents, account setup or private assistant automation is included here.

## 繁體中文

請以英文主版與繁中對照一起更新，保留相同檔名；修改 Markdown／SVG 正本，不直接改 PDF。PR 說明問題、變更、實際驗證和限制。範例皆用虛構內容，不上傳私人回執、對話或金鑰。命令與功能需標版本及原始依據，規約不能寫成程式保證。執行上列驗證與測試，版面變更則重新檢視兩種語言。離線閱讀器不加入追蹤、CDN 或外部字型。
