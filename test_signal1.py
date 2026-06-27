from app import stylometric_score, combine_scores

texts = [
    ("clearly_ai",    "Artificial intelligence represents a transformative paradigm shift in modern society. It is important to note that while the benefits of AI are numerous, it is equally essential to consider the ethical implications. Furthermore, stakeholders across various sectors must collaborate to ensure responsible deployment. Organizations that embrace these technologies will be better positioned to achieve sustainable growth and competitive advantage in the digital economy."),
    ("clearly_human", "ok so i finally tried that new ramen place downtown and honestly? underwhelming. the broth was fine but they put WAY too much sodium in it and i was thirsty for like three hours after. my friend got the spicy version and said it was better but i dont know, the vibe was off too. like why is it so loud in there. probably won't go back unless someone drags me there lol"),
]

for label, text in texts:
    wc = len(text.split())
    stylo = stylometric_score(text)
    # Simulate what llm_classify would return (use your M3 test results)
    llm = 0.8 if "ai" in label else 0.2
    combined = combine_scores(llm, stylo, wc)
    print(f"{label}: llm={llm:.2f}  stylometric={stylo:.3f}  combined={combined:.3f}  words={wc}")

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

#Milestone 4

# $ curl -s -X POST http://localhost:5000/submit \
#   -H "Content-Type: application/json" \
#   -d '{"text": "Artificial intelligence represents a transformative paradigm shift in modern society. It is important to note that while the benefits of AI are numerous, it is equally essential to consider the ethical implications. Furthermore, stakeholders across various sectors must collaborate to ensure responsible deployment. Organizations that embrace these technologies will be better positioned to achieve sustainable growth and competitive advantage in the digital economy.", "creator_id": "test-user-ai"}' | python -m json.tool
# {
#     "attribution": "likely_ai",
#     "confidence": 0.6703,
#     "content_id": "eae9e8a0-20fa-4eca-aab8-f3ab8686d19a",
#     "label": "TBD in M5",
#     "llm_score": 0.8,
#     "stylometric_score": 0.3677
# }

# $ curl -s -X POST http://localhost:5000/submit \
#   -H "Content-Type: application/json" \
#   -d '{"text": "ok so i finally tried that new ramen place downtown and honestly? underwhelming. the broth was fine but they put WAY too much sodium in it and i was thirsty for like three hours after. my friend got the spicy version and said it was better but i dont know, the vibe was off too. like why is it so loud in there. probably wont go back unless someone drags me there lol", "creator_id": "test-user-human"}' | python -m json.tool
# {
#     "attribution": "likely_human",
#     "confidence": 0.22,
#     "content_id": "c7bb7be5-0ac2-4dee-8cfd-4774106d1576",
#     "label": "TBD in M5",
#     "llm_score": 0.2,
#     "stylometric_score": 0.2667
# }

# $ curl -s -X POST http://localhost:5000/submit \
#   -H "Content-Type: application/json" \
#   -d '{"text": "The relationship between monetary policy and asset price inflation has been extensively studied in the literature. Central banks face a fundamental tension between their mandate for price stability and the unintended consequences of prolonged low interest rates on equity and real estate valuations.", "creator_id": "test-user-formal"}' | python -m json.tool
# {
#     "attribution": "likely_human",
#     "confidence": 0.3025,
#     "content_id": "ae3e70e5-045a-4323-8e4a-31d16006d1ac",
#     "label": "TBD in M5",
#     "llm_score": 0.2,
#     "stylometric_score": 0.5417
# }

# $ curl -s -X POST http://localhost:5000/submit \
#   -H "Content-Type: application/json" \
#   -d '{"text": "I have been thinking a lot about remote work lately. There are genuine tradeoffs - flexibility and no commute on one side, isolation and blurred work-life boundaries on the other. Studies show productivity varies widely by individual and role type.", "creator_id": "test-user-edited"}' | python -m json.tool
# {
#     "attribution": "likely_human",
#     "confidence": 0.2044,
#     "content_id": "b3bbefaa-abf8-489d-944f-b2e6a9f62963",
#     "label": "TBD in M5",
#     "llm_score": 0.2,
#     "stylometric_score": 0.2148
# }
# (.venv) 

# likely_ai: eae9e8a0-20fa-4eca-aab8-f3ab8686d19a  (test-user-ai)