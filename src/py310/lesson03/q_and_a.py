all_answers = []
while True:
    questions = (
        "Your name : ",
        "Your age : ",
        "anything you want : ",
        "Favorite color : ",
        "Pet's name : ",
    )

    answers = []
    for question in questions:
        answers.append(input(question))

    print(answers)
    all_answers.append(tuple(answers))
    yorn = input("ask again?")
    if yorn == "y":
        continue
    break

print("end")
print(tuple(all_answers))
