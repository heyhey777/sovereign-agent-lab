"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No venue in the current dataset can accommodate 300 people; even removing the vegan requirement still returned no venue with capacity 300 or more."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
When I changed The Albanach's status from available to full and reran the MCP client, Query 1 changed immediately: the search result dropped from two matches to one, so only The Haymarket Vaults remained. The best final answer stayed The Haymarket Vaults, and I did not need to update the client code at all, only the MCP server data.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4   # rough intuition, not exact
LINES_OF_TOOL_CODE_EX4 = 2   # rough intuition, not exact

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP lets multiple agents use the same tools from one shared server instead of each client owning its own copy of the tool logic. In my run, I changed the venue status in the MCP server and the client output changed immediately without changing the client code. That means MCP gives reuse, one shared source of truth, and easier updates across both halves of PyNanoClaw.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The Planner lives in the autonomous-loop half and turns a messy request into ordered subgoals before the executor starts calling tools.
- The Executor lives in the autonomous-loop half and runs the ReAct loop, using tools to research venues, weather, pricing, and other open-ended tasks.
- The Structured Agent lives in the Rasa half and handles human conversations like booking confirmation with fixed flows and deterministic business rules.
- The Shared MCP Tool Server lives in the shared layer and exposes venue lookups, web search, calendar actions, and other tools to both halves.
- The Handoff Bridge lives between the two halves and passes work from the autonomous loop to the structured agent when a real conversation or approval step is needed.
- The Memory layer lives alongside both halves and stores files, past results, and retrieved knowledge so PyNanoClaw can continue work across longer tasks.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The research task fits LangGraph better because it has to explore, compare options, and chain tool calls across different steps like venue search, weather, catering, and flyer generation. The confirmation call fits Rasa better because it asks fixed questions, applies business rules, and stays inside scope. Swapping them feels wrong because LangGraph is more flexible but less controlled for high-stakes confirmations, while Rasa is more predictable and auditable but too rigid for messy research.
"""
