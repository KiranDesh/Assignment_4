#*) Write a Python program to print all permutations with a given repetition number of characters of a given string. 
from itertools import permutations

def permulation_1(str_12):
    for i in str_12:
        for j in str_12:
            print(i,j)

str_12 = list(set("".join(input("Enter a string:").split(' '))))
permulation_1(str_12)

def permulation_2(str_12):
    print (list(permutations(str_12)))

permulation_2(str_12)