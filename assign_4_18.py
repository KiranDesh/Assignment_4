#*) Write a Python program to move spaces to the front of a given string. 

def move_space(str_18):
    spaces = len([i for i in str_18 if i == ' '])
    print('Length of space',spaces)
    print()
    print(str_18)
    print()
    print("length of original string",len(str_18))
    print()
    print(' '*spaces+str_18)
    print()
    print('Length of spaced string',len(" "*spaces+str_18))

str_18 = input("Enter a string : ")
move_space(str_18)