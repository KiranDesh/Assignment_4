#*) Write a Python program to split a string on the last occurrence of the delimiter. 

def delimit(str_10,delimiter):
    rev = [i for i in ''.join(str_10[::-1])]
    rev.pop(rev.index(delimiter))
    print("".join(rev[::-1]))

str_10 = input('Enter a string : ')
delimiter = input("Enter a delimiter : ")

delimit(str_10,delimiter)