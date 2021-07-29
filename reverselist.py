# function that reverses a list

def reverse_list(l):
    reversedl = []
    count = len(l) - 1
    while count >= 0:
        reversedl.append(l[count])
        count -= 1
    print(reversedl)
        

reverse_list(["a", "b", "c", "d", "e"])