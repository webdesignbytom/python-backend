# Recursion and while loop searchs
# (0 + 9)/2  mid value of binary search.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# is search term above or below mid point?
# discard and start search again.
print(x)

## funtion takes a list or target params
## multi variables
## recursion or while loop

### WHILE LOOP
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start < end):
        print("Steps", steps ,":", str(list[start:end+1]))

        steps += 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]: ## remove top half
            end = middle -1
        else: 
            start = middle + 1 # use top half of array

    return -1

my_list = x
target = 2
binary_search(my_list, target)

### RECUSION