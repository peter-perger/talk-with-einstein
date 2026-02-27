from functions.einsteinAI import getAnswer

print("Ask something from Einstein!")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        break

    print(getAnswer(user_question))
