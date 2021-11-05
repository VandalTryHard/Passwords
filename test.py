exam1 = "0123456789"
exam2 = "abcdefghijklmnopqrstuvwxyz"
exam3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
exam4 = "!£$%&<*@"
exam = set(exam1+exam2+exam3+exam4)
password = set("qwerty")
print(exam)
print(password)
print(password in exam)