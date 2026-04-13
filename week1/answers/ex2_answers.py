"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = []

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "FILL_ME_IN"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 0.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = None

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = "TODO: fix, as no tool calls were made"

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "live"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-fd59891b-0293-4f58-8a58-640af6cd1a4d_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography"

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
FILL ME IN
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
  The function calls provided meet the requirements for checking the availability of The Bow Bar, generating an event flyer, calculating catering costs, and getting the current weather in Edinburgh.

The Bow Bar does not meet the capacity requirements, so the next available venue is checked. The Haymarket Vaults and The Albanach both meet the requirements, but The Albanach is chosen for the event.

The event flyer is generated with the confirmed venue name, guest count, and event theme. The cate..."""

SCENARIO_1_FALLBACK_VENUE = "Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
  None of the known venues meet the capacity and dietary requirements. The Albanach, The Haymarket Vaults, and The Guilford Arms have a capacity of 180, 160, and 200 respectively, which is less than the required capacity of 300. The Bow Bar has a capacity of 80, which is also less than the required capacity, and it is currently full. Therefore, none of the known venues can accommodate 300 people with vegan options.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "  Your input is lacking necessary details. Please provide more information or specify the task you need help with."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
The behaviour is fine as the agent can not help here, but the AI output answer itself does not really explain what that this specific agent can only help with (booking pubs not trains), it might confuse the user.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
https://mermaid.live/edit#pako:eNpdkU1uwyAQha-CpptEslOM_xQSZdMcoauWyiI22JYcsDBum0a5ezFJXSUbNG_03jcwnKHUlQAKYRgyVWol25oyhZDs9FfZcGO9QqgczaegqGuV4IYpb68N7xv0ut8wxWxRDNbZi2Lxvu13s9o-97uPJaVUtmawk5HXQtmFP5eTtlp3w8KfyytIqGrG-HqGdPzKmPEoDHfIszYzG4Ur17xFH9t-zmae-5Av3YBhLySqhORjZ5Fsu44-SSKxlMH0-LARbd1YGq3IXcA_z9tD3fOytSeK7wzT1W-4gzxksoQAatNWQK0ZRQBHYY58knCeNs7ANuIoGFBX3m7DgKmLi_VcvWl9_EsaPdYNUMm7wamxr7gV-5a73_m3uF0I86JHZYFGaewZQM_wDZTEZJXhLE6yGKcRTnMSwMm5XDtPYkySPCckj-P8EsCPH4tXaRJneUQIySKc4PX68gvz6MGN
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
instead of rules.yml there is flows.yml, I assume this is the one we need. 
Rasa has all the flows listed - and decides predictably, which to start. 
The mermaid tool shows a diagram, with a loop where agent calls tools - we don see a clear algorytm over which tools.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
I think it works so well with a happy path and the little edge cases, like the impossible constrains.
But for the Out of Scope task the response was: ("AI: Your input is lacking necessary details. Please provide more information or specify the task you need help with") 
I think for an average user ambiguous responses with no clear next step (they want to learn about a train - they want a next step related to this task), this would make
our agent feel less approachable and convinient, than the non-agentic flows with buttons navigation, where user can only choose from the buttons available.
"""
