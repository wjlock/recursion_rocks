# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    if len(l) == 1:
        return l[0]
    else:
        if len(l) > 1:
            if l[0] > l[1]:
                list.remove(l[1])
            else:
                list.remove(l[0])
            find_max(l)

    # print(find_max([1, 4, 45, 6, -50, 10, 2]))
    # => 45
