#*) Write a Python program to capitalize the first and last letters of each word in a given string.

def cap(str_20):
    print([i[0].upper()+i[1:-1]+i[-1:].upper() for i in str_20])

str_20 = input("Enter a string : ").split(' ')
cap(str_20)