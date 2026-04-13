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

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]


# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.00

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = "Default Qwen/Qwen3-32B did not make tool calls in my environment, so I ran Exercise 2 with RESEARCH_MODEL=nvidia/nemotron-3-super-120b-a12b."


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
TASK_B_MODE = "placeholder" 
# "live"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"
#"https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-fd59891b-0293-4f58-8a58-640af6cd1a4d_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."
# "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography"

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
generate_event_flyer has a fallback - if real_url is None, it uses the website placehold.co
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
        {
          "role": "tool_call",
          "tool": "check_pub_availability",
          "args": {
            "pub_name": "The Albanach",
            "required_capacity": 160,
            "requires_vegan": true
          }
        },
        {
          "role": "tool_result",
          "tool": "check_pub_availability",
          "content": "{\"success\": true, \"pub_name\": \"The Albanach\", \"address\": \"2 Hunter Square, Edinburgh\", \"capacity\": 180, \"vegan\": true, \"status\": \"available\", \"meets_all_constraints\": true}"
        },
        {
          "role": "ai",
          "content": "\n\nThe Bow Bar does **not** meet your requirements \u2013 it has a capacity of only\u202f80\u202fpeople, which is below the 160\u202fguests you need, even though it does offer vegan options.\n\nI then checked the next available venue from the list:\n\n**The Albanach**  \n- Address: 2 Hunter Square, Edinburgh  \n- Capacity: 180\u202fpeople (meets your 160\u2011guest requirement)  \n- Vegan options: Yes  \n- Current status: Available  \n\n**Result:** The Albanach satisfies all your constraints (capacity \u2265\u202f160 and vegan\u2011friendly) and is available for tonight. You can proceed with booking The Albanach for your event."
        }
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
After checking all four known Edinburgh venues, none can accommodate **300 people** while also providing vegan options:\n\n| Venue | Capacity | Vegan Options | Meets 300\u2011person + Vegan Requirement? |\n|-------|----------|---------------|----------------------------------------|\n| The Albanach | 180 | \u2705 Yes | \u274c No (capacity too low) |\n| The Haymarket Vaults | 160 | \u2705 Yes | \u274c No (capacity too low) |\n| The Guilford Arms | 200 | \u274c No | \u274c No (capacity too low & no vegan) |\n| The Bow Bar | 80 | \u2705 Yes | \u274c No (capacity too low) |\n\n**Result:** No venue from the current list satisfies both the 300\u2011person capacity and vegan\u2011food requirement.\n\n**Next steps you might consider:**\n- Look for a larger venue outside the known list (e.g., a conference center, hotel banquet hall, or larger event space) that can host 300 guests and offers vegan catering.\n- Reduce the expected guest count to fit within the capacities of the available venues (the largest is The Albanach at 180).\n- If vegan options are flexible, The Guilford Arms holds 200 but does not currently offer vegan food\u2014you could check if they can accommodate a vegan menu upon request.\n\nLet me know if you\u2019d like help checking any other specific venue, adjusting the guest count, or exploring catering costs for a chosen location.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "I don't have access to real-time train schedule information, including departure times for services from Edinburgh Waverley to London. My capabilities are focused on helping with event planning in Edinburgh\u2014such as checking venue availability, weather, catering costs, and generating promotional materials.\n\nFor the most accurate and up-to-date train times, I recommend checking:\n- **National Rail Enquiries** (nationalrail.co.uk)\n- **Trainline** or similar booking apps\n- **ScotRail** or **LNER** websites (depending on the operator)\n- Station departure boards at Edinburgh Waverley\n\nIf you're planning an event in Edinburgh and need help with venues, weather, catering, or promotional materials, I'd be happy to assist with those aspects instead."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
For the old result, using Qwen/Qwen3-32B: when i used The behaviour is fine as the agent can not help here, but the AI output answer itself does not really explain what that this specific agent can only help with (booking pubs not trains), it might confuse the user.
For the new result, using nvidia/nemotron-3-super-120b-a12b: yes it is perfect!
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
{
  "task_d_mermaid": "---\nconfig:\n  flowchart:\n    curve: linear\n---\ngraph TD;\n\t__start__([<p>__start__</p>]):::first\n\tagent(agent)\n\ttools(tools)\n\t__end__([<p>__end__</p>]):::last\n\t__start__ --> agent;\n\tagent -.-> __end__;\n\tagent -.-> tools;\n\ttools --> agent;\n\tclassDef default fill:#f2f0ff,line-height:1.2\n\tclassDef first fill-opacity:0\n\tclassDef last fill:#bfb6fc\n"
}
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
I think the small model Qwen/Qwen3-32B works well with a happy path and the little edge cases, like the impossible constrains.
But for the Out of Scope task the response was: ("AI: Your input is lacking necessary details. Please provide more information or specify the task you need help with") 
I think for an average user ambiguous responses with no clear next step (they want to learn about a train - they want a next step related to this task), this would make
our agent feel less approachable and convinient, than the non-agentic flows with buttons navigation, where user can only choose from the buttons available.
Qwen/Qwen3-32B had a failure with the task a tool calls too.

nvidia/nemotron-3-super-120b-a12b had a much better failure message and fixed the task a for me. 
"""
