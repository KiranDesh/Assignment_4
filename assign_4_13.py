#*) Write a Python program to find the first repeated character in a given string. 

def first_rep_char(str_13):
    dict_1 ={i:str_13.count(i) for i in str_13}
    print([(i,j) for i,j in zip(dict_1.keys(),dict_1.values()) if j >= 2][0])

str_13 = input("Enter a string : ")
first_rep_char(str_13)