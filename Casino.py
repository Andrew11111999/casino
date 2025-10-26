import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}


def get_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


def deposit():
    while True:
        amount = input('Какую сумму вы хотите внести? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Сумма должна быть больше 0.')
        else:
            print('Пожалуйста введите число.')

    return amount


def get_number_of_lines():
    while True:
        lines = input('Введите количество линий для ставки (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Введите правильное количество линий')
        else:
            print('Пожалуйста введите число.')

    return lines


def get_bet():
    while True:
        amount = input('Какую сумму вы хотите поставить на каждую линию? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Сумма должна быть между ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Пожалуйста введите число.')

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'Недостаточно средств, ваш баланс: ${balance}')
        else:
            break
    print(f'Вы ставите ${bet} на {lines} линии. Общая ставка ровна: ${total_bet}')
    print(balance, lines)


main()
