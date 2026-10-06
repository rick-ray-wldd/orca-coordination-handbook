# Translation policy

**Primary: English (`en`). Complete companion: Traditional Chinese (`zh-TW`).**

`locales.json` is the locale directory manifest. Keep machine identifiers, JSON keys, state names, commands and filenames unchanged. Translate prose, labels, example descriptions and SVG text/accessible titles. Illustrative keyword lists may be localized; domain assignments and policy meaning must agree.

Every chapter links to the matching chapter in the other edition. Offline HTML switches between sibling files and preserves chapter anchors. PDFs are language-specific. The build includes every locale in the manifest.

## Add a language

1. Add its BCP 47 tag, native label and directories to `locales.json`.
2. Copy the English chapter/template/diagram file structure into those directories.
3. Translate **all** chapters, templates and diagrams; keep 52 capability rows and the authorization/evidence limitations intact.
4. Add chapter language links and a README entry; update the reader labels in `scripts/build.py` if needed.
5. Run validation and visually inspect the generated edition. Do not advertise a complete locale before its full review.

English revisions and translations should ship in the same release. If they cannot, disclose the mismatch before publishing instead of silently serving a stale translation. Editorial prose may differ; the workflow's promises, boundaries and examples must remain equivalent.

## 繁體中文

英文為主、繁體中文為完整對照。機器識別字、JSON key、狀態、命令與檔名不翻譯；翻譯說明、標籤與 SVG 文字／無障礙標題。關鍵字範例可在地化，路由與政策含義要一致。每章可切到對應語言；HTML 保留章節錨點，PDF 各自獨立。

新增語言時更新 locales.json，完整複製並翻譯章節／模板／圖，保留 52 項能力對照與授權、證據、限制說明，補 README 入口並跑驗證、檢查排版。未完整完成前不要標示為完整支援；若翻譯落後，發布前明確揭露。
