def do_something1(p):
    return p


def do_something2(p):
    return p


def do_something3(p):
    return p


def get_input():
    results = dict()
    results['name'] = input("enter name : ")
    results['age'] = input("enter age : ")
    return results


def display_results(z):
    for key, value in z.items():
        print(key, value)


def main():
    results = get_input()
    x = do_something1(results)
    y = do_something2(x)
    z = do_something3(y)
    display_results(z)


if __name__ == '__main__':
    main()
