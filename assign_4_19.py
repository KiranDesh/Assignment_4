#*) Write a Python program to find the maximum number of characters in a given string. 

def max_char(str_19):
    print('the maximum number of characters in a given string',max([len(i) for i in str_19]))

str_19 = input("Enter a string : ").split(" ")
max_char(str_19)