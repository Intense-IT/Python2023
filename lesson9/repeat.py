"""Цикл while, прерываемый командой break"""

while True:
    command = input()
    if command == 'стоп':
        break
    print('Выполняется команда ' + command)
