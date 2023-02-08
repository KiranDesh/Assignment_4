# Write a Python program to strip a set of characters from a string. 

def strip_char(str_1):
    char_strip = input("Enter a character you want to strip : ").split(" ")
    print("".join(i for i in str_1 if i not in char_strip))
    
str_1 = input("Enter a string : ")
strip_char(str_1)