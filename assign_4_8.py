#*) Write a Python program to swap commas and dots in a string. 
#Sample string: "*)*),*)
#Expected Output: "*)*).*)

def swap_comma_dots(str_8):
    str_8=str_8.replace(',','third')
    str_8=str_8.replace('.',',')
    str_8=str_8.replace('third','.')
    print(str_8)
 
str_8 = input("Enter a string : ")   
swap_comma_dots(str_8)