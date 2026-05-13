# Testing Plan — T3+ Verification Log

> Updated 2026-05-13. Verification is **done**; this doc is now a historical log.
> The branch `t3-stage-4-6-7-unverified` referenced in earlier versions has been
> fully merged into `main` and deleted.

## ✅ Final state (everything on `main`)

| Batch | What | How verified | Bugs fixed |
|---|---|---|---|
| Phase 3 — Stage 1 + 3 folder renames (6 folders) | `starter.py` (Ollama) / `starter_anthropic.py` / both test suites | `python test.py` + `python test_anthropic.py` per folder | 0 |
| Phase A — `stages/03-tool-use-and-hello-agent.md` inline `<details>` (練習 2-6) | 5 simplified inline blocks + zh-Hans drift | `wc -l` parity, `grep` no residual Trad chars | 0 |
| Phase B — `examples/stage-5/tool-calling-tutor/` skill | SKILL.md + 3 references + evals + trilingual READMEs | YAML frontmatter parses; evals.json valid JSON | 0 (live skill-install test still pending) |
| Phase C — cross-references | stages/03 + stages/05 + CLAUDE.md links | `grep -c` confirms 10 references across 7 files | 0 |
| **Stage 4 (5 ex)** | LangGraph + CrewAI + LangGraph workflow + Smolagents + Pydantic AI | 8/8 test suites verified green; ex2 CrewAI install-blocked on Python 3.14 (tiktoken/regex wheels) — code shipped unmodified | 3 (i18n key mismatch in ex3 + Smolagents docstring `Args:` requirement in ex4 + Pydantic AI version fallback in ex5 test) |
| **Stage 6 (5 ex)** | embeddings + ChromaDB + chunking + full RAG + long-term memory | 10/10 test suites verified green | 2 (ChromaDB `kb` collection name too short for Chroma 1.0+; `EphemeralClient` state leak across test fixtures) |
| **Stage 7 (5 ex)** | multi-agent debate + eval + observability + streaming/caching + FastAPI deploy | 10/10 test suites verified green | 1 (operator precedence: `and` binds tighter than `or` in fake_agent dispatcher) |

**Total: 28/30 test files run green** + 1 install caveat (CrewAI on Python 3.14) + 1 pending live test (skill auto-load).

**Total bugs fixed**: 6 — all in commit [`50c3bf8`](https://github.com/WenyuChiou/awesome-agentic-ai-zh/commit/50c3bf8).

## 🟢 Pedagogy v1 also shipped (2026-05-13)

Recognized late in the session: every `starter.py` is a **complete solution**, not a TODO skeleton. A learner who clones and runs `python test.py` passes without writing any code.

v1 fix (doc-only, no code rename):
- `docs/HOW_TO_USE.md` — full active-vs-passive learning method (~200 lines, zh-TW)
- 22 exercise READMEs — 🎓 callout pointing to `mv starter.py starter_reference.py` shortcut + link to HOW_TO_USE
- Main README × 3 langs — surface the meta-instruction at the top-level

Shipped in commits [`d598e37`](https://github.com/WenyuChiou/awesome-agentic-ai-zh/commit/d598e37) + [`2cf99fe`](https://github.com/WenyuChiou/awesome-agentic-ai-zh/commit/2cf99fe).

## ⚠ Known caveats still on `main`

1. **CrewAI exercise (Stage 4 ex2)** not tested on Python 3.14 — tiktoken + regex don't have wheels yet. Code shipped unchanged; users on Python 3.11/3.12/3.13 should be fine. Document at top of `examples/stage-4/02-multi-agent-roles/README.md` if needed for future learners.

2. **tool-calling-tutor skill** not live-tested in Claude Code — only structural validation (YAML frontmatter parse + JSON evals validate). Manual install test: `cp -r examples/stage-5/tool-calling-tutor/{SKILL.md,references,evals} ~/.claude/skills/tool-calling-tutor/`, restart Claude Code, prompt 「為什麼 LLM 不呼叫我的 tool」.

3. **starter.py = complete solution pedagogy gap** — flagged in `docs/HOW_TO_USE.md`. v2 would split into `starter_template.py` (TODO) + `starter_reference.py` (solution); v1 is doc-only meta-instruction.

4. **Trilingual mirror of 🎓 callout incomplete** — v1 only added the 學習模式 callout to zh-TW READMEs. en + zh-Hans exercise READMEs still need the same callout. Low priority since most learners use zh-TW.

5. **Pilot exercise drift** (pre-session, still open) — `examples/stage-3/03-react-from-scratch/README.en.md` + `.zh-Hans.md` are pre-dual-path; the zh-TW canonical is current. Stage 3 polish pass should fix.

## 🔵 Stage 5 + Track A — still pending

23 exercises remaining (Stage 5 sub-§ 5.1-5.4 + Track A1-A3 CLI-1 through CLI-12). **Not started.** Different shape — they're mostly bash / MCP / markdown / SKILL.md authoring, not Python SDK code. The Ollama-vs-Anthropic dual-path framing doesn't apply directly.

Framing decisions needed before writing:

| Stage 5 sub-§ | Likely framing |
|---|---|
| 5.1 Claude Code 基礎 | CLI walkthrough only, no dual-path |
| 5.2 MCP | Python MCP SDK example (single path) |
| 5.3 Skills | SKILL.md authoring tutorial; the `tool-calling-tutor` we shipped is the canonical example |
| 5.4 Plugins | plugin.json + marketplace.json walkthrough |

| Track A | Likely framing |
|---|---|
| A1 CLI intro | Compare 7 CLIs (Claude Code / Codex / OpenCode / Gemini CLI / goose / Aider / Hermes) — already structured in the outline |
| A2 CLI workflow | `CLAUDE.md` authoring + slash command + portable prompt patterns |
| A3 CLI production | MCP + GitHub Actions + cost tracking + plugin sharing |

These should be scoped in a follow-up session.

## v2 path (deferred)

Per `docs/HOW_TO_USE.md` § "給維護者：v2 path":
- Split each `starter.py` → `starter_template.py` (TODO skeleton) + `starter_reference.py` (solution)
- Make `test.py` behavioral (input → output contract) instead of implementation-bound
- ~20 folders × 3 file changes = ~60 file changes
- Probably needs its own session

## Historical: what was on the unverified branch

Before verification, Stage 4 + 6 + 7 commits sat on branch `t3-stage-4-6-7-unverified` (rationale: framework deps not pip-installed at write time, API drift risk). After actual verification on 2026-05-13:

```
50c3bf8 fix(examples): 6 bugs found while verifying Stage 4/6/7 tests
9f60759 Stage 7 練習 5 (FastAPI deploy)
1a8ba16 Stage 7 練習 4 (streaming + caching)
128ca7a Stage 7 練習 3 (observability)
8119de0 Stage 7 練習 2 (eval)
5ff3ce3 Stage 7 練習 1 (multi-agent debate)
8150881 Stage 6 練習 5 (long-term memory)
7633874 Stage 6 練習 4 (full RAG pipeline)
7a8af9b Stage 6 練習 3 (chunking comparison)
b83a5e5 Stage 6 練習 2 (vector DB)
7d2c1b7 Stage 6 練習 1 (embeddings)
ab6d358 Stage 4 練習 5 (Pydantic AI)
6316d83 Stage 4 練習 4 (Smolagents CodeAct)
ea9c14a Stage 4 練習 3 (LangGraph branching)
dbe7c91 Stage 4 練習 2 (CrewAI multi-agent)
8051861 Stage 4 練習 1 (LangGraph + CrewAI)
```

All merged into `main` via [`cdb0ae3`](https://github.com/WenyuChiou/awesome-agentic-ai-zh/commit/cdb0ae3). Branch deleted from origin after merge.
