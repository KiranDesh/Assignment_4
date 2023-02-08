#*) Write a Python program to find the second most repeated word in a given string. 

def second_repeat(str_16):
    p = {i:str_16.count(i) for i in str_16}
    print("the second most repeated word is",[(i,j) for i,j in p.items() if j>=2][1][0])

str_16 = input('Enter a string : ')
second_repeat(str_16)