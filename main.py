import os
import datetime
import csv

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

transaktions = []


def logg_user_logg_in(username):
    time = datetime.datetime.now()
    l = f'{username}, {time.year}, {time.day}, {time.hour}, {time.minute}, {time.second}'
    with open('my_logg.txt', 'a', encoding='utf-8') as f:
            f.write(l + '\n')

users = {'KalleAnka': 'Hejsan123',
         'JanneLångben': 'password',
         'Sebastianmentor': 'qwerty'}

bankkonto = {'KalleAnka': 1000,
             'JanneLångben': 100, 
             'Sebastianmentor': 0}

def create_new_user():
    clear_screen()
    for i in range(3,0,-1):
        username = input("Ange nytt användarnamn: ")
        if username in users:
            print(f"Användaren finns redan! Du har {i-1} försök kvar!")
        else:
            clear_screen()
            break
    
    while True:
        new_password = input('Ange nytt lösenord: ')
        confirm_password = input('Bekräfta lösenord: ')

        if new_password == confirm_password:
           break
        print('Inkorrekt lösenord! Försök igen.')


    users[username] = new_password
    bankkonto[username] = 0

    print(f"Ny användare med användarnamn {username} är skapat!")
    print(f"Nytt konto skapat med 0 i saldo!")
    input('Tryck enter för att gå tillbaka till menyn!')


def is_logged_in(username):
    logg_user_logg_in(username)

    print('Grattis, du är inloggad!!!')
    while True:
        print('1. Sätt in pengar\n2. Ta ut pengar\n3. Visa saldo\n4. Avsluta')
        choice = input('>>>')
        match choice:
            case '1':
                try:
                    value = int(input('Hur mycket vill du sätta in?'))

                except ValueError:
                    print('Totalt fel mannen!!!')
                    continue
                    
                if value < 0:
                    print('Hur tänkte du nu???')
                else:
                    bankkonto[username] += value
                    transaktions.append((username,value,'Insättning',datetime.datetime.now()))
                
            case '2':
                try:
                    value = int(input('Hur mycket vill du ta ut?'))

                except ValueError:
                    print('Totalt fel mannen!!!')
                    continue
                    
                if value <= 0:
                    print('Hur tänkte du nu??? Går inte att ta ut negativa pengar!')

                elif not bankkonto[username] > value:
                    print('Inte tillräckligt tyvärr!!!!(fattiglapp....)')
                else:
                    bankkonto[username] -= value
                    transaktions.append((username,value,'Uttag',datetime.datetime.now()))

            case '3':
                print(bankkonto[username])
            case '4':
                break
            case _:
                print('Invalid input')


def logg_in():
    username = input('Ange användarnamn: ')

    if username in users:
        pwd = input('Ange ditt lösenord: ')
        if users[username] == pwd:
            clear_screen()
            is_logged_in(username)
        else:
            print('Fel lösenord!')

    else:
        print('Användarnamnet finns inte!!! Skriv rätt för tusan')


def run():
    
    while True:
        clear_screen()
        print('Välkomen \2\n1. Logga in\n2. Skapa ny användare\n0. Avsluta')
        choice = input('>>>')

        if choice == '1':
            logg_in()

        elif choice == '2':
            create_new_user()

        elif choice == '0':
            break
        else:
            print('Ogiltligt val \4')

if __name__ == '__main__':
    run()

    with open('my_transaktion.txt', 'w', encoding='utf-8') as f:
        for t in transaktions:
            f.write(f'{t}' + '\n')

    with open('transaktions.csv','w',encoding='utf-8', newline='') as f:
        spamwriter = csv.writer(f, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for tran in transaktions:
            spamwriter.writerow(tran)

    print(bankkonto)