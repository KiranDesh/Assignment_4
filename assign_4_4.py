#*) Write a Python program to print the index of a character in a string. 
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

def index_char(str_4):  
    for i in str_4:
        print("Current character",i,"position at {0}".format(str_4.index(i)))
    
str_4 = list("".join(input('Enter a string : ')))
index_char(str_4)