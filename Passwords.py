"""Напишите программу, которая сохраняет идентификаторы пользователей и их пароли.
Программа должна выводить следующее меню:
1) Create a new User ID
2) Change a password
3) Display all User IDs
4) Quit
Enter Selection:
Если пользователь выбирает пункт 1, программа предлагает ввести идентификатор
пользователя. Она должна проверить, существует ли введенный идентификатор
в списке. Если это так, программа выводит соответствующее сообщение и предлага-
ет выбрать другой идентификатор. После того как пользователь введет допустимый
идентификатор, программа запрашивает пароль. Паролю начисляется по одному баллу
за соответствие перечисленным ниже условиям:
пароль должен содержать не менее 8 символов;
пароль должен включать буквы верхнего регистра;
пароль должен включать буквы нижнего регистра;
пароль должен включать цифры;
пароль должен включать хотя бы один специальный символ: !, £, $, %, &, <, * или @.
Если пароль получает всего 1 или 2 балла, он должен быть отклонен с формулировкой,
что он является слабым. Если у пароля 3 или 4 балла, выводится сообщение о том, что
его можно улучшить. Спросите пользователя, хочет ли он повторить попытку. Если па-
роль набрал 5 баллов, сообщите, что он является сильным. В конец файла .csv должны
добавляться только допустимые идентификаторы и пароли.
Если пользователь выберет пункт 2, он должен будет ввести идентификатор пользо-
вателя. Проверьте, существует ли идентификатор в списке. Если это так, предложите
пользователю изменить пароль и сохраните изменения в файле .csv. Убедитесь в том,
что программа только изменяет существующий пароль, а не создает новую запись.
Если пользователь выберет пункт 3, выведите только идентификаторы
пользователей без паролей.
Наконец, при выборе пункта 4 программа должна завершиться."""

import csv
import re

def main():
    start = True
    while start == True:
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all User IDs")
        print("4) Quit")
        user_choice = input("Enter: ")
        filePasswords = open("passwords.csv", "a")
        filePasswords.close()
        if user_choice == "1":
            newID, newUserName, newPassword = createNew()
            examinationID(newID)
            passStrength(newPassword)
            newUser(newID, newUserName, newPassword)
        elif user_choice == "2":
            changePass()
        elif user_choice == "3":
            displayID()
        elif user_choice == "4":
            quit()
        else:
            print("Error. Try again!")

#1
def createNew():
    newID = input("Enter new ID: ")
    newUserName = input("Enter username: ")
    newPassword = input("Enter password: ")
    newUser = newID, newUserName, newPassword
    return newUser

def examinationID(newID): #Проверка на входимость в список
    filePasswords = open("passwords.csv", "r")
    search = newID
    for row in filePasswords:
        if search in str(row[0]):
            print("This ID is already taken.\n")
            filePasswords.close()
            main()

def newUser(newID, newUserName, newPassword): # Запись нового user
    filePasswords = open("passwords.csv", "a")
    newUser = newID + ", " + newUserName + ", " + newPassword + "\n"
    filePasswords.write(str(newUser))
    filePasswords.close()

#Проверка пароля на надежность Password check for strength 
def passStrength(newPassword):
    while True:
        password = newPassword
        if len(password) < 8 or re.search('[0-9]',password) is None or re.search('[A-Z]',password) is None \
            or re.search('[a-z]',password) is None or re.search('[!£$%&<*@]',password) is None:
            print("""The password must contain at least 8 characters;
            the password must include uppercase letters;
            the password must include lowercase letters;
            the password must include numbers;
            the password must include at least one special character:!, £, $,%, &, <, *, or @. \n""")
            main()
        else:
            print("Your password seems fine")
            break

#2
def changePass():
    filePasswords = csv.reader(open("passwords.csv"))
    rows = list(filePasswords)
    changePassUser = int(input("Enter ID for change password: "))
    try:
        row = rows[changePassUser-1]
    except IndexError:
        print("The specified ID was not found. ")
        main()
    print(row)
    newPassword = input("Сhange Password (y/n): ")
    if newPassword == "y":
        newPassword = input("Enter new password: ")
        passStrength(newPassword)
        rows[changePassUser-1][2] =" " + newPassword
        writer = csv.writer(open("passwords.csv", "w", newline=""))
        writer.writerows(rows)
    else:
        main()
    # filePasswords = open("passwords.csv", "r")
    # for row in filePasswords:
    #     print(row)
    # changePassUser = input("Enter ID for change password: ")
    # filePasswords = list(csv.reader(open("passwords.csv")))
    # change = []
    # for changePassUser in filePasswords:
    #     change.append(changePassUser)
    #     print(change)
    # print(change)

#3
def displayID():
    filePasswords = open("passwords.csv", "r")
    reader = csv.reader(filePasswords)
    for row in reader:
        print(row)

main()