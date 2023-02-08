#*) Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest. 

def first_rep_char(str_14):
    p = {i:str_14.count(i) for i in str_14}
    repeat_1 = list((i,j) for i,j in p.items() if j>=2)[0]
    rep_index = repeat_1[0]
    print('first repeated character is ',rep_index)
    print('first repeated character in a given string where the index of the first occurrence is',str_14.index(rep_index))
    
str_14 = input('Enter a string : ')
first_rep_char(str_14)