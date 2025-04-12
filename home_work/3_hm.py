#практический урок
def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print("YES")
    else:
        print("NO")

task_yes_no(str_1='test', str_2='test1')



def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4: #равно либо 1, либо 2,...
        print("Вы - бакалавар")
    elif year_of_study in range(5, 7): #входит в диапазон 5 и 7 не включая 7
        print("Вы - магистр")
    elif 7 <= year_of_study <= 9: #в диапазоне включительно
        print("Вы - аспирант")
    else:
        print("Введите корректный год обучения")

student_rank(3)


a = 5

if a >100 or a < -100:
    print('-')
else:
    print('+')


#HOME WORK_3

#HW_2

def compare_numbers(a, b):
    print(max(a, b))

compare_numbers(4, 9)

#HW3
def check_difference(a, b):
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")

check_difference(100, 35)

#HW4
def get_season(month):
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Некорректный номер месяца")

get_season(4)

#HW5
def all_above_ten(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

all_above_ten(13, 10,11)


#HW6, логикой понятно, что надо сравнить каждое с нулем, но вопрос, а если таких сотни числе, это же можно как-то по иному написать?:)
def task_6(num1, num2, num3, num4, num5) -> int:
    count = 0
    if num1 > 0:
        count += 1
    if num2 > 0:
        count += 1
    if num3 > 0:
        count += 1
    if num4 > 0:
        count += 1
    if num5 > 0:
        count += 1

    print("Количество положительных чисел:", count)
task_6(-4, 5, -324, -24, 1)


#HW7
def count_days(years, months) ->int:
    result = (years * 12 + months) * 29
    print(result)

count_days(2, 4)

