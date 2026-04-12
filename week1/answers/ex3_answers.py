"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
2026-04-12 17:50:36 INFO     rasa.tracing.backend_tracing_config  - [info     ] No backend tracing configuration found in endpoints.yml. Supported backend tracing types are 'jaeger' and 'otlp'. Backend tracing will not be configured. event_key=endpoint.read.no_backend_tracing_config filename=/Users/kate/Documents/sovereign-agent-lab/exercise3_rasa/endpoints.yml
2026-04-12 17:50:37 INFO     root  - Starting Rasa server on http://0.0.0.0:5005
2026-04-12 17:50:37 INFO     rasa.core.processor  - [info     ] Loading model.                 event_key=rasa.core.processor.load_model model_path=models/20260412-174011-potential-cilantro.tar.gz
2026-04-12 17:50:38 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating
2026-04-12 17:50:38 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable LLM health check. It is recommended to set this variable to true in production environments. event_key=llm_based_command_generator.load.perform_llm_health_check.disabled
2026-04-12 17:50:38 INFO     rasa.dialogue_understanding.generator.llm_based_command_generator  - [info     ] llm_based_command_generator.flow_retrieval.enabled
2026-04-12 17:50:38 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable embeddings API health check. It is recommended to set this variable to true in production environments. event_key=flow_retrieval.load.perform_embeddings_health_check.disabled
2026-04-12 17:50:38 INFO     faiss.loader  - Loading faiss.
2026-04-12 17:50:38 INFO     faiss.loader  - Successfully loaded faiss.
2026-04-12 17:50:38 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating
2026-04-12 17:50:38 WARNING  rasa.validator  - [warning  ] Default pattern flows include responses with rephrasing enabled, but the NLG endpoint is not configured in endpoints.yml. Rephrasing for default patterns will be skipped. event_key=validator.verify_rephrase_endpoints_consistency.defaults_only_rephrase_without_nlg
2026-04-12 17:50:38 INFO     root  - Rasa server is up and running.
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
ClientConnectorError: Cannot connect to host localhost:5055 ssl:default [Multiple exceptions: [Errno
61] Connect call failed ('::1', 5055, 0, 0), [Errno 61] Connect call failed ('127.0.0.1', 5055)]
"""

CONVERSATION_2_OUTCOME = "ClientConnectorError: Cannot connect to host localhost:5055 ssl:default [Multiple exceptions: [Errno
61] Connect call failed ('::1', 5055, 0, 0), [Errno 61] Connect call failed ('127.0.0.1', 5055)]"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "ClientConnectorError: Cannot connect to host localhost:5055 ssl:default [Multiple exceptions: [Errno
61] Connect call failed ('::1', 5055, 0, 0), [Errno 61] Connect call failed ('127.0.0.1', 5055)]"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
ClientConnectorError: Cannot connect to host localhost:5055 ssl:default [Multiple exceptions: [Errno
61] Connect call failed ('::1', 5055, 0, 0), [Errno 61] Connect call failed ('127.0.0.1', 5055)]
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
ClientConnectorError: Cannot connect to host localhost:5055 ssl:default [Multiple exceptions: [Errno
61] Connect call failed ('::1', 5055, 0, 0), [Errno 61] Connect call failed ('127.0.0.1', 5055)]
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
ClientConnectorError: Cannot connect to host localhost:5055 ssl:default [Multiple exceptions: [Errno
61] Connect call failed ('::1', 5055, 0, 0), [Errno 61] Connect call failed ('127.0.0.1', 5055)]
"""
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = [actions.py]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
RasaException("Failed to execute custom action 'action_validate_booking'.   │ │
│ │                     Couldn't connect to the server
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
We havent used the old RASA but I see that the new RASA is easier to setup and more reliable


Think about:
- What does the LLM handle now that Python handled before?
- What does Python STILL handle, and why (hint: business rules)?
- Is there anything you trusted more in the old approach?
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
We havent used the old RASA but I see that the new RASA is easier to setup and more reliable


Be specific. What can the Rasa CALM agent NOT do that LangGraph could?
Is that a feature or a limitation for the confirmation use case?
Think about: can the CALM agent improvise a response it wasn't trained on?
Can it call a tool that wasn't defined in flows.yml?
"""
