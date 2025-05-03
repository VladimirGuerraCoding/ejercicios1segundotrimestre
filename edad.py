from datetime import date

def años(birthday):
    
    birthday = date.fromisoformat(birthday)
    hoy = date.today()
    edad = hoy.year - birthday.year
    if hoy.month < birthday.month or (hoy.month == birthday.month and hoy.day < birthday.day):
        edad -= 1
    return edad

birthday = input('fecha de nacimiento (YYYY-MM-DD): ')
edad = años(birthday)
print(f'la edad es: {edad} años')
