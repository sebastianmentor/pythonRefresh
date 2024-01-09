import os
import datetime
import csv

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

transaktions = []

logg = []

def logg_user_logg_in(username):
    time = datetime.datetime.now()
    logg.append(f'{username}, {time.year}, {time.day}, {time.hour}, {time.minute}, {time.second}')

users = {'KalleAnka': 'Hejsan123',
         'JanneLångben': 'password',
         'Sebastianmentor': 'qwerty'}

bankkonto = {'KalleAnka': 1000,
             'JanneLångben': 100, 
             'Sebastianmentor': 0}


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
        print('Välkomen \2\n1. Logga in\n2. Avsluta')
        choice = input('>>>')

        if choice == '1':
            logg_in()
        elif choice == '2':
            break
        else:
            ...

if __name__ == '__main__':
    run()
    with open('my_logg.txt', 'w', encoding='utf-8') as f:
        for l in logg:
            f.write(l + '\n')

    with open('my_transaktion.txt', 'w', encoding='utf-8') as f:
        for t in transaktions:
            f.write(f'{t}' + '\n')

    with open('transaktions.csv','w',encoding='utf-8', newline='') as f:
        spamwriter = csv.writer(f, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for tran in transaktions:
            spamwriter.writerow(tran)

    print(bankkonto)