#hw_1

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 4)
rect3 = Rectangle(7, 2)

print("Площадь 1:", rect1.area(), "Периметр 1:", rect1.perimeter())
print("Площадь 2:", rect2.area(), "Периметр 2:", rect2.perimeter())
print("Площадь 3:", rect3.area(), "Периметр 3:", rect3.perimeter())


#hw_2

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print("Сложение:", self.a + self.b)

    def multiplication(self):
        print("Умножение:", self.a * self.b)

    def division(self):
        if self.b != 0:
            print("Деление:", self.a / self.b)
        else:
            print("На ноль делить нельзя!")

    def subtraction(self):
        print("Вычитание:", self.a - self.b)

m = Math(10, 2)
m.addition()
m.multiplication()
m.division()
m.subtraction()

#hw_3

class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"

btn1 = Button("Text Box")
btn2 = Button("Check Box")
btn3 = Button("Radio Button")
btn4 = Button ("Web tables")
btn5 = Button("Buttons")
btn6 = Button ("links")
btn7 = Button("Broken link - img")
btn8 = Button("Upload and download")
btn9 = Button ("Dynamic properties")

buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

for button in buttons:
    print("Текст кнопки:", button.text)
    print(button.click())

#hw_4

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

mcar = Car("Шоколадный", "Кроссовер", 2025)
mcar.start()
mcar.stop()
mcar.set_year("2025")
print(mcar.year)
mcar.set_type("Кроссовер")
print(mcar.type)
mcar.set_color("Салатовый")
print(mcar.color)


