def month_to_season(month):         
    if 3 <= month <= 5:
        return ("Весна")   
    elif 6 <= month <= 8:
        return ("Лето")      
    elif 9 <= month <= 11:
        return ("Осень")
    else:
        return ("Зима")     


month = int(input("Введите номер месяца: "))
print(month_to_season(month))
