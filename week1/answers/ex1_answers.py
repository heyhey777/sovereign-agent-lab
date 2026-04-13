"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Quick result, all results are correct, but they differed in token usage.
The Sandwich used considerably more tokens, 289. PLAIN the least tokens, 180. 
XML is closer to SANDWICH, 251 tokens
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
To my understanding, The Holyrood Arms: it is next to the right answer that is the middle (The Haymarket Vaults. vs The Albanach, which is the very first where attention dillution or the context loss typical fot the middle might happen). 
It also satisfies the first two constraints, the capacily and the vegan catering
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Since the parts A and B returned correct results, the small model was run for me in part C.
The answer provided by it was correct. Interestingly, while the for the plain case the output stayed same, for XML and Sandwich only in part c the picked answer was "The Haymarket Vaults".
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when there are some parameters that we consider important (for example, we need to be careful not to choose the pub with the "full" status)
but they could be missed because of 1) near-miss distractors, that might on a quick skim look like a correct answer (but in fact can be a total failure for the task)
2) smaller models and a lot of data. 
We did not demonstrate it here, however errors are likely to happen with more data and complexity.
"""
