import csv
from openai import OpenAI

client = OpenAI()

# Load CSV data
data = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

print("🚀 Smart AI System (OpenAI) Started (type 'exit' to quit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("AI: Bye! 👋")
        break

    # DATA LOGIC
    if "average" in user_input:
        total = sum(int(d["marks"]) for d in data)
        avg = total / len(data)
        print(f"📊 AI: Average marks are {avg}")

    elif "highest" in user_input:
        max_marks = max(int(d["marks"]) for d in data)
        print(f"🏆 AI: Highest marks are {max_marks}")

    else:
        # OPENAI AI RESPONSE
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content
        print("🤖 AI:", answer)
