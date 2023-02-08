#*)Write a Python program to find the first repeated word in a given string. 

def first_rep(str_15):
    p = {i:str_15.count(i) for i in str_15}
    print("the first repeated word is",[(i,j) for i,j in p.items() if j>=2][0][0])

str_15 = input('Enter a string : ')
first_rep(str_15)
