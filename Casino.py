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

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_winnings(columns, lines, bet, values):
    """
    Проверяет выигрышные линии.

    columns — список из списков с символами для каждого барабана.
    lines — количество линий, на которые сделана ставка.
    bet — ставка на одну линию.
    values — словарь с ценностью каждого символа.

    Возвращает сумму выигрыша и список выигрышных линий.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Генерирует случайное распределение символов по колонкам.

    rows — количество рядов.
    cols — количество колонок.
    symbols — словарь с количеством каждого символа.

    Возвращает list из cols списков длины rows с символами.
    """
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Выводит на экран игровое поле.

    columns — список списков символов.
    """
    for row in range(len(columns[0])):
        row_symbols = [columns[col][row] for col in range(len(columns))]
        print(" | ".join(row_symbols))


def deposit():
    """
    Запрашивает у пользователя сумму для депозита.

    Возвращает положительное целое число.
    """
    while True:
        amount = input('Какую сумму вы хотите внести? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print('Сумма должна быть больше 0.')
        else:
            print('Пожалуйста введите число.')


def get_number_of_lines():
    """
    Запрашивает у пользователя количество линий для ставки.

    Возвращает целое число от 1 до MAX_LINES.
    """
    while True:
        lines = input(f'Введите количество линий для ставки (1-{MAX_LINES})? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print('Введите правильное количество линий.')
        else:
            print('Пожалуйста введите число.')


def get_bet():
    """
    Запрашивает у пользователя сумму ставки на одну линию.

    Возвращает целое число от MIN_BET до MAX_BET.
    """
    while True:
        amount = input(f'Какую сумму вы хотите поставить на каждую линию? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f'Сумма должна быть между ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Пожалуйста введите число.')


def spin(balance):
    """
    Выполняет один раунд игры: ставки, спин барабанов и подсчёт выигрыша.

    balance — текущий баланс пользователя.

    Возвращает чистый результат раунда: (выигрыш - ставка).
    """
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'Недостаточно средств, ваш баланс: ${balance}')
        else:
            break

    print(f'Вы ставите ${bet} на {lines} линии. Общая ставка ровна: ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'Ты выиграл ${winnings}.')
    if winning_lines:
        print(f'Вы выиграли на линиях:', *winning_lines)
    else:
        print('К сожалению, выигрышных линий нет.')

    return winnings - total_bet


def main():
    """
    Основная функция запуска игры.
    """
    balance = deposit()
    while True:
        print(f'Текущий баланс равен ${balance}')
        answer = input('Нажмите enter чтобы начать игру (q чтобы выйти). ')
        if answer.lower() == 'q':
            break
        balance += spin(balance)

    print(f'Вы ушли с ${balance}')


if __name__ == '__main__':
    main()
