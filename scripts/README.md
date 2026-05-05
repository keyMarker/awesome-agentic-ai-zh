# scripts/

維護用的工具腳本。

## `check-links.py` — 檢查連結是否失效

掃描所有 markdown 檔案中的 URL，回報 4xx / 5xx / timeout。

```bash
# 一次性檢查全部
python scripts/check-links.py

# 只查 GitHub repos（最容易 404 的）
python scripts/check-links.py --fast

# 只印失敗，不印 OK
python scripts/check-links.py --quiet
```

退出 code：失敗時 = 1，全部 OK = 0。可以接 CI。

依賴：`pip install requests`

## `refresh-stars.py` — 比對 markdown 內標註的 stars 跟實際

```bash
# 列出所有差距 ≥ 10% 的 entry
python scripts/refresh-stars.py

# 設定門檻（譬如 ≥ 20%）
python scripts/refresh-stars.py --threshold 20

# CI 模式（差距超過門檻就退 code 1）
python scripts/refresh-stars.py --check
```

依賴：`pip install requests` + `gh` CLI（`gh auth login`）

## 建議的維護節奏

- **每月**：跑一次 `check-links.py --fast` 看 GitHub repo 連結有沒有 404
- **每季**：跑一次 `refresh-stars.py` 看大幅成長 / 衰退的 repo
- **每半年**：跑一次完整 `check-links.py`（包含非 GitHub 連結）

可以接到 GitHub Actions 自動跑（見未來 Phase 6 的 CI 設定）。
