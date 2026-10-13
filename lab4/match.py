number = int(input("Введите номер месяца: "))
match number:
    case 12 | 1 | 2:
        print("Это зима!")
    case 3 | 4 | 5:
        print("Это весна!")
    case 6 | 7 | 8:
        print("Это лето!")
    case 9 | 10 | 11:
        print("Это осень!")
    case _:
        print("Вы не так поняли. Номера месяцев от 1 до 12!")


http_status = int(input("Введите статус http(400/401/403/404): "))
match http_status:
    case 400:
        print("400: Bad request")
    case 401:
        print("401: Unauthorized")
    case 403:
        print("403: Forbidden")
    case 404:
        print("404: Not found")
    case _:
        print("Нужно ввести верное значение: 400/401/403/404")