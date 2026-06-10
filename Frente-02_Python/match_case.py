numero_problema = int(input())

match numero_problema:
    case 1000:
        print('Problema inicial')
    case numero_problema if 1001 <= numero_problema <= 1020:
        print('Lista básica 1')
    case _:
        print('Lista avançada')
        