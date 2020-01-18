'''

Instead of looping we can simply iterate with map

'''

'''
def times3(numbers):
    new_array = []
    for number in numbers:
        new_array.append(number*3)
    return (new_array)

print(times3([1,2,3,4,5]))
'''


def times3(numbers):
    return numbers * 3

print(list(map(times3,[1,2,3,4,5])))