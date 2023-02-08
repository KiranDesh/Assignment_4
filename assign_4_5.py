#*) Write a Python program to check whether a string contains all letters of the alphabet. 
import string

def alpha(str_5):
    list_of_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #p = ([str_5.replace(j,' ')for i in str_5 for j in punc if i == j])
    #print(p)
    p = [i for i in str_5]
    if len(p) == len(list_of_alphabet):
        print("string contains all letters of the alphabet")
    else:
        print("string not contains all letters of the alphabet")
        
str_5 = "".join(input('Enter a string : '))
alpha(str_5)