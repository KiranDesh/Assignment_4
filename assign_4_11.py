#*) Write a Python program to find the first non-repeating character in a given string. 

def non_rep(str_11):
    p = {i:str_11.count(i) for i in str_11}
    print([(i,j) for i,j in zip(p.keys(),p.values()) if j == 1][0])

str_11 = input("Enter a string : ")
non_rep(str_11)
