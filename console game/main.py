from random import randint
from time import sleep

def guess_num() -> str:
    current_num = randint(1, 10)
    for i in range(3):
        user_num = int(input("Введите ваше число от 1 до 10: "))
        if user_num == current_num:
            return f"Вы угадали число с {i+1} попытки"
        else:
            print("Больше") if current_num > user_num else print("Меньше")
    return f"Повезёт в следующий раз!"
        
def random_num() -> str:
    result = randint(1, 6)
    points = "."
    for i in range(3):
        print(f"Бросаем кости{points}")
        points += "."
        sleep(1)
    return f"Выпало {result}!"

user = input("Как вас зовут? ")
num = int(input(f"{user}, выберите игру: \n 0 - Выход\n 1 - Угадай число\n 2 - Бросить кость\n"))

while num != 0:
    match num:
        case 1:
            print(guess_num())
        case 2:
            print(random_num())

    num = int(input(f"{user}, выберите игру: \n 0 - Выход\n 1 - Угадай число\n 2 - Бросить кость\n"))

print("Увидимся в следующий раз!")