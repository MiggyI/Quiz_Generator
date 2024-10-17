import json
import random

def load():
    with open("Questions.json","r") as f:
        question = json.load(f)["questions"]

    return question

def rand_question(question, num_quesetion):
    if num_quesetion > len(question):
        num_quesetion = len(question)

    random_question = random.sample(question,num_quesetion)
    return random_question


def ask(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i+1) + ".", option)
    
    number = int(input("Select Correct Number: "))
    if number < 1 or number > len(question["options"]):
        print("Don't work")
        return False
    
    correct = question["options"][number -1] == question["answer"]
    return correct



question = load()
question_count = int(input("Enter Number of Questions"))
random_question = rand_question(question,question_count)
correct = 0


for q in random_question:
    is_correct = ask(q)
    if is_correct:
        correct += 1

    print("       ")

print("summary")
print("Total Questions", question_count)
print("Correct", correct)
print("Score:", str(round((correct / question_count) * 100, 2)) + "%")



# NOW JUST CHANGE THE QUESTIONS TO THINGS ABOUT OUR GROUP!!