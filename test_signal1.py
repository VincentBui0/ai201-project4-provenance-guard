from app import llm_classify, init_db

init_db()
score = llm_classify("The sun dipped below the horizon, painting the sky in hues of amber and rose.")
print(f"Human-ish text: {score}")

score2 = llm_classify("Artificial intelligence is transforming industries by enabling automation, improving efficiency, and providing data-driven insights that help organizations make better decisions.")
print(f"AI-ish text: {score2}")

# $ curl -s -X POST http://localhost:5000/submit \
#   -H "Content-Type: application/json" \
#   -d '{"text": "The sun dipped below the horizon, painting the sky in hues of amber and rose. I sat on the porch, coffee in hand, watching the neighborhood slowly go quiet.", "creator_id": "test-user-1"}' | python -m json.tool
# {
#     "attribution": "likely_human",
#     "confidence": 0.2,
#     "content_id": "1e93722f-4a32-42e0-b71e-da118faa6b51",
#     "label": "TBD in M5"
# }

# $ curl -s -X POST http://localhost:5000/submit \
#   -H "Content-Type: application/json" \
#   -d '{"text": "Artificial intelligence is transforming industries by enabling automation, improving efficiency, and providing data-driven insights that help organizations make better decisions.", "creator_id": "test-user-2"}' | python -m json.tool
# {
#     "attribution": "likely_ai",
#     "confidence": 0.8,
#     "content_id": "339952f3-d6e5-448d-857c-0c897a41d91f",
#     "label": "TBD in M5"
# }

# $ curl -s -X POST http://localhost:5000/submit \
#   -H "Content-Type: application/json" \
#   -d '{"text": "I dunno, maybe its just me but every time I try to write something real it comes out wrong. Like the words are right but the feeling isnt there.", "creator_id": "test-user-3"}' | python -m json.tool
# {
#     "attribution": "likely_human",
#     "confidence": 0.2,
#     "content_id": "833e6f1e-a803-43a1-af48-f9b44fb0876d",
#     "label": "TBD in M5"
# }

# Test content_ids (saved for M5 appeals testing):
# likely_human:  1e93722f-4a32-42e0-b71e-da118faa6b51  (test-user-1)
# likely_ai:     339952f3-d6e5-448d-857c-0c897a41d91f  (test-user-2)
# likely_human:  833e6f1e-a803-43a1-af48-f9b44fb0876d  (test-user-3)