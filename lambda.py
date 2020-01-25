# Lambda no name function
# We don't have to use functions any more in map/filter/reduce

list1 = [1,2,3,4,5,6]

print(list(filter(lambda item: item % 2 == 0, list1)))

# It will print even numbers in list

