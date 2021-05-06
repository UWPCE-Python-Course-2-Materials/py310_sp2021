def anti_pattern_menu():
    for option in ["1. do this", "2. do that"]:
        print("option")
    chosen = input("your chocie : ")
    if option == 1:
        do_function_1()
    elif option == 2:
        do_function_x()


messages = {
    1: "hello",
    2: "goodbye",
}

# choice = int(input("1 or 2 : "))
choice = 1
assert messages[choice] == "hello"
choice = 2
assert messages[choice] == "goodbye"


def adder(number1, number2):
    return number1 + number2


def suber(number1, number2):
    return number1 - number2


todo = {
    1: adder,
    2: suber,
}

assert todo[2](3, 4) == -1
assert todo[1](3, 4) == 7

better = {
    1: {'prompt': "add it : ", 'func':  adder},
    2: {'prompt': "sub it : ", 'func':  suber},
}


for key, value in better.items():
    print(f"{key} {value['prompt']}")

#choice = int(input("what do you want? : "))
choice = 1
result = better[choice]['func'](3,4)
assert result == 7

choice = 2
result = better[choice]['func'](3,4)
assert result == -1
