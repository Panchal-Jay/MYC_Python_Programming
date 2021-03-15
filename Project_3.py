# Task 1

# Printing frequencies of all characters in decreasing order from string or list

def most_frequent(str):
    d = {} # storing characters in d
    for n in str:
        if n in d:
            d[n] += 1 # assuming the character is already there and just we r increasing its count
        else:
            d[n] = 1 
    d = {key: val for key,val in sorted(d.items(),key = lambda ele:ele[1], reverse = True)}
    return d
    
print(most_frequent("Mississippi"))
    
# this is for printing output in different style     
'''
    print("\n")
    for n in d.keys():
        print(n," Occurs for ", d[n], " times.")
'''

