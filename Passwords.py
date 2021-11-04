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

def main():
    start = True
    while start == True:
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all User IDs")
        print("4) Quit")
        user_choice = input("Enter: ")
        if user_choice == "1":
            newID, newUserName, newPassword = createNew()
            examination(newID, newUserName, newPassword)
        # elif user_choice == "2":
        #     changePass()
        # elif user_choice == "3":
        #     displayID()
        elif user_choice == "4":
            quit()
        else:
            print("Error. Try again!")

def createNew():
    newID = input("Enter new ID: ")
    newUserName = input("Enter username: ")
    newPassword = input("Enter password: ")
    filePasswords = open("passwords.csv", "a")
    filePasswords.close()
    newUser = newID, newUserName, newPassword
    return newUser

def examination(newID, newUserName, newPassword):
    filePasswords = open("passwords.csv", "r")
    search = newID
    csv.reader(filePasswords)
    for row in filePasswords:
        if search in str(row):
            print("This ID is already taken.")
        else:
            filePasswords = open("passwords.csv", "a")
            newUser = newID + ", " + newUserName + ", " + newPassword
            filePasswords.write(str(newUser))
            filePasswords.close()




# def changePass():

# def displayID():

main()