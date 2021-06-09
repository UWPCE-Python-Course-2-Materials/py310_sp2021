def andy_print(print_this):
    return print_this + " xxx"


print = andy_print

assert print("Here it is") == "Here it is xxx"
