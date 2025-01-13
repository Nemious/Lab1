import random
import logging


# Настройка логгера
logging.basicConfig(filename='game.log', level=logging.DEBUG)

# Функция для игры "Камень - ножницы - бумага"
def rock_paper_scissors():
    user_choice = input("Выберите камень, ножницы или бумагу: ").lower()
    logging.info(f"Пользователь выбрал: {user_choice}")

    if user_choice not in ['камень', 'ножницы', 'бумага']:
        print("Неправильный выбор, попробуйте снова.")
        logging.error("Ошибка: неправильный выбор пользователя")
        return

    computer_choice = random.choice(['камень', 'ножницы', 'бумага'])
    logging.info(f"Компьютер выбрал: {computer_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
        logging.info("Результат: ничья")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or (user_choice == 'ножницы' and computer_choice == 'бумага') or (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы победили!")
        logging.info("Результат: победа пользователя")
    else:
        print("Вы проиграли!")
        logging.info("Результат: победа компьютера")

# Запуск игры
while True:
    print("\nИгра 'Камень - ножницы - бумага'")
    logging.info("Новая игра началась")
    rock_paper_scissors()
    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    logging.info(f"Пользователь выбрал: {play_again}")
    if play_again != 'да':
        print("Спасибо за игру!")
        logging.info("Игра завершена")
        break