def info(name, surname, bd_year, city, email, phone):
    return str(name + " " + surname + ", " + bd_year + "года рождения, проживает в городе: " + city + ", email:  "
               + email + ", телефон: " + phone)


user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_bd_year = input("Введите год рождения: ")
user_city = input("Введите город проживания: ")
user_email = input("Введите email: ")
user_phone = input("Введите телефон: ")

print("Вы ввели данные: " + info(name=user_name, surname=user_surname, bd_year=user_bd_year,
                                 city=user_city, email=user_email, phone=user_phone))
