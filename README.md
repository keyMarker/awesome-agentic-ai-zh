# awesome-agentic-ai-zh

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Status](https://img.shields.io/badge/status-WIP%20%C2%B7%20Phase%201-orange)](#phase-1-現況)
[![Language](https://img.shields.io/badge/語言-繁體中文-red)](README.md) [![EN](https://img.shields.io/badge/lang-English-blue)](README.en.md)

> **AI agent 學習路線圖（繁體中文）** — 從第一次呼叫 LLM API 到 ship 多 agent 生產系統的完整路徑。**結構化 7 階段**，不是平鋪 awesome list；每個階段都有 hello-X 必跑 demo、必修閱讀、精選 project。

[English version](README.en.md)

---

## 為什麼有這個 repo

大多數 AI agent 的 awesome 清單都是**平鋪型 catalog** — 你已經知道在找什麼時很有用，但**剛入門想知道下一步學什麼**時就無從下手。

這個 repo 是**結構化學習路線圖**：

- 7 個階段、從 prerequisite 到 production
- 每階段有「**必跑 hello-X demos**」（光讀沒用、必須動手）
- Curated projects 按階段 + audience 分類
- **繁體中文 canonical**，引用的中文資源以 zh-CN（Datawhale、jjyaoao、KimYx0207）為主，會逐步補 zh-TW 原生資源
- 誠實時間估算（主幹**最少 14-19 週、現實上 5-6 個月**）

如果你是剛起步、想避免迷失在 noise 裡的學習者 — 這份路線圖就是給你的。

---

## 7 階段學習地圖

```
Stage 0  基礎準備           (Python · CLI · git · API · JSON)         1-2 週
Stage 1  LLM 入門           (token · API · 各家 LLM 比較)             1 週
Stage 2  Prompt 設計        (系統 prompt · few-shot · CoT)             1-2 週
Stage 3  Tool Use & Hello Agent ⭐ (function calling · ReAct · 5 hello-X) 2-3 週
Stage 4  Agent 框架         (LangGraph · AutoGen · CrewAI 等)          2-3 週
Stage 5  Claude Code 生態 ⭐⭐ (MCP · Skills · Plugins)                3-4 週
Stage 6  Memory · RAG · 進階 (vector DB · long-term memory)             2 週
Stage 7  Multi-Agent · Production (orchestration · eval · deploy · SDK) 2-4 週
```

**主幹總時數：最少 14-19 週、現實上 5-6 個月**，每週 5-8 hr 兼職進度。下限假設你跳過 Stage 0 且不會卡在框架安裝。

走完主幹後可以選 specialized branch：
- 🔬 [研究人員 path](branches/for-researcher.md)
- 💻 [開發者 path](branches/for-developer.md)
- 🎓 [教師 path](branches/for-teacher.md) — *目前最薄、特別歡迎社群貢獻*
- 📊 [知識工作者 path](branches/for-knowledge-worker.md)

---

## 自我引用聲明

整個 catalog 約六分之一（~12 個 entry）是這個 repo 作者（`WenyuChiou/...`）自己維護的 repo。納入是因為它們示範**特定 pattern**（multi-plugin marketplace、single-plugin bundle、single-skill plugin、sub-CLI delegation、governance layer）— 每個 entry 的 notes 都會解釋它教什麼 pattern。如果有非自有的 repo 教同樣 pattern 教得更好、歡迎開 PR — 見 CONTRIBUTING.md。

---

## 各階段速查

| 階段 | 標題 | 核心問題 | 詳細頁面 |
|---|---|---|---|
| 0 | 基礎準備 | 我有基本能力嗎？ | [stages/00-foundations.md](stages/00-foundations.md) |
| 1 | LLM 入門 | 什麼是 LLM？ | [stages/01-llm-basics.md](stages/01-llm-basics.md) |
| 2 | Prompt 設計 | 怎麼讓 LLM 照我意思跑？ | [stages/02-prompt-engineering.md](stages/02-prompt-engineering.md) |
| 3 | Tool Use & Hello Agent ⭐ | 怎麼建第一個 agent？ | [stages/03-tool-use-and-hello-agent.md](stages/03-tool-use-and-hello-agent.md) |
| 4 | Agent 框架 | 該學哪個框架？ | [stages/04-agent-frameworks.md](stages/04-agent-frameworks.md) |
| 5 | Claude Code 生態 ⭐⭐ | 怎麼擴充 Claude Code？ | [stages/05-claude-code-ecosystem.md](stages/05-claude-code-ecosystem.md) |
| 6 | Memory · RAG | Agent 怎麼記憶？ | [stages/06-memory-rag.md](stages/06-memory-rag.md) |
| 7 | Multi-Agent · Production | 怎麼 ship 到 production？ | [stages/07-multi-agent-production.md](stages/07-multi-agent-production.md) |

> **目前各 stage 詳細頁面為英文版**（用作 reference），繁中翻譯為 Phase 2 工作。

---

## 怎麼用這個 repo

1. **看上面 7 個階段、找到你目前位置**
2. **點進對應 stage 頁面**，每個頁面都有：
   - Learning goals（讀完能做什麼）
   - Entry conditions（前置條件）
   - 必修閱讀（3-5 個連結）
   - 必跑 Hello-X projects
   - Curated case-study projects（含我的 notes）
   - Self-check 進下一階段
3. **不要跳過 Stage 3 Hello Agent** — 5 個 hello-X 沒實際跑過 = 浪費時間
4. **Stage 5 通常會花最多時間**，正常的

---

## Curation 標準

每個列入的 project 都通過以下檢核：

- **持續維護**（最近 6 個月有 commit）
- **文件品質**（README 清楚、hello-world 可重現）
- **教育價值**（有沒有教到可推廣的概念？）
- **License 明確**（避開沒 license 的 repo）
- **可信度**（known maintainer 或 org）

推薦星等（⭐ 到 ⭐⭐⭐⭐⭐）：
- ⭐⭐⭐⭐⭐ — 該階段必讀
- ⭐⭐⭐⭐ — 強推、值得深入
- ⭐⭐⭐ — 紮實範例、值得跑跑看
- ⭐⭐ — 參考用、有興趣再看
- ⭐ — Niche / 進階 / 為了完整列表

---

## 相關 awesome 清單

這個 repo 不取代平鋪型 awesome 清單。已知道在找什麼時、用這些：

- [**hesreallyhim/awesome-claude-code**](https://github.com/hesreallyhim/awesome-claude-code) — Claude Code 廣泛資源 catalog（重整中）
- [**wong2/awesome-mcp-servers**](https://github.com/wong2/awesome-mcp-servers) — 平鋪 MCP server 清單
- [**punkpeye/awesome-mcp-servers**](https://github.com/punkpeye/awesome-mcp-servers) — 另一個 MCP 清單
- [**travisvn/awesome-claude-skills**](https://github.com/travisvn/awesome-claude-skills) — Claude Skills catalog
- [**modelcontextprotocol/servers**](https://github.com/modelcontextprotocol/servers) — 官方 MCP reference servers
- [**datawhalechina/hello-agents**](https://github.com/datawhalechina/hello-agents) — Datawhale 中文教程（zh-CN）

---

## Phase 1 現況

目前是 Phase 1 — 7 階段骨架 + anchor curation（~80 個 project）。Phase 2 工作：

- 8 個 stage 頁面 + 4 個 branch 頁面**完整繁中翻譯**
- 補到 100+ curated projects
- 隨社群貢獻、降低自我引用比例
- Stage 5 stack-at-a-glance SVG 升級版
- `resources/style-guide.md` 術語一致性

---

## Contributing

歡迎 PR。詳見 [CONTRIBUTING.md](CONTRIBUTING.md)。最有價值的貢獻：

- 新增 project 到對應 stage、附上「為什麼這 project 教那個 stage」說明
- **將 stage 頁面翻譯成繁中**（最緊迫）
- Flag 失維護或過期的 project

---

## License

MIT。Maintained by [@WenyuChiou](https://github.com/WenyuChiou)。
