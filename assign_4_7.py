#*) Write a Python program to lowercase the first n characters in a string. 

def lowercase(str_7):
    n = int(input("Enter a number till you want lowercase : "))
    print(str_7[:n].lower()+str_7[n:])

str_7 = input("Enter a string : ")
lowercase(str_7)