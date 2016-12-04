from log_annotation import log
from stack import Stack

stack = Stack()
stack.set_max_size(10)


@log(stack)
def get_text(name):
    return "hello, " + name


def save_and_clear_stack():
    items = stack.clear()
    with open("stack.txt", mode="a", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n\n")


if __name__ == "__main__":
    print(get_text("Matt"))
    print(stack.peek())
    print(get_text("Alex"))
    print(stack.peek())

    save_and_clear_stack()
