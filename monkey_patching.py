class Monkey:
    def patch(self):
        print("patch() is being called..")


def monk():
    print("Monk is being called..")



monkey = Monkey()

monkey.patch = monk



monkey.patch()