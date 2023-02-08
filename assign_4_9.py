#Write a Python program to count and display vowels in text. 

def count_vowels(str_9):
    p = [i for i in str_9 if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u']
    print(p)
    print(len(p))

str_9 = input("Enter a string : ")
count_vowels(str_9)