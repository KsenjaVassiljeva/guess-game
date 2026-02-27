import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    
    print("Я загадал число от 1 до 100")

    while True:
        guess = int(input("Введите число: "))
        attempts += 1

        if guess < number:
            print("Слишком маленькое!")
        elif guess > number:
            print("Слишком большое!")
        else:
            print(f"Правильно! Попыток: {attempts}")
            break

guess_number()