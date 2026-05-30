print("=== General Knowledge Quiz ===")

score = 0

questions = {
    "What is the capital of India? ": "new delhi",
    "Which planet is known as the Red Planet? ": "mars",
    "How many days are there in a week? ": "7",
    "What is the national animal of India? ": "tiger",
    "What is 5 + 5? ": "10"
}

for question, answer in questions.items():
    user_answer = input(question).lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nFinal Score: {score}/{len(questions)}")