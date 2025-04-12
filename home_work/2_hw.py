
def task_1() -> None:
    print("этот текст должен же появиться")
    a = 2
    b = 3.14
    c = "Hi"
    d = [1, 2, 3]
    e = True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

task_1()



def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[:3])

task_2()


def task_3(x: int) ->int:
    return x ** 2

print(task_3(5))