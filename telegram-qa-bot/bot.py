import json
import requests

TOKEN = "tokenn hereee"
CHAT_ID = "chatiddd"

with open("questions.json", "r") as f:
    questions = json.load(f)

message = ""

for i in range(len(questions)):
    q = questions[i]

    message += f"{i+1}. {q['question']}\n"
    message += f"Answer: {q['answer']}\n\n"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Sent")
