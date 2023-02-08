#*) Write a Python program to count repeated characters in a string. 
#Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
 
def count_rep(sample_string):
    solution = {i:sample_string.count(i) for i in sample_string}
    print([(i,j) for i,j in (list(zip(solution.keys(),solution.values()))) if j>=2])

sample_string='thequickbrownfoxjumpsoverthelazydog'
count_rep(sample_string)

