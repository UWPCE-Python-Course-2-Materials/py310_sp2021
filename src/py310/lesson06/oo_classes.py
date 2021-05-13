

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_my_emails = []

    def send_email(self, to_user, message):
        print(f"send from {self.name} with email {self.email}")
        print(f"sending to {to_user} message {message}")
        return True

    def say_hello(self, message):
        print(f"I am {self.name}")


andy = Person("andy", "akmiles@icloud.com")
print(andy.name)
print(andy.email)

fred = Person("fred", "Fred@yahoo.com")
print(fred.name)

andy.send_email("harry", "blah blah blah")
andy.say_hello("khkjhkj")
