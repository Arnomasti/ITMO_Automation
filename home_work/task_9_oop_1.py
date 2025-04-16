
from task_9_checks import Checks

class Button (Checks):
    pass
class  Car (Checks):
    pass

class Math (Checks):
    pass

class Rectangle (Checks):
    pass
btn = Button ("Локатор кнопки")
car = Car ("Локатор авто")
mth = Math ("Локатор счета")
rct = Rectangle ("Локатор прямоугольника")

print(btn.check_text())
print(car.check_text())
print(mth.check_text())
print(rct.check_text())

