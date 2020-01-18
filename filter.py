# Instead of for loop we use filter
'''

def oddnum(numbers):
    odd_item = []
    for item in numbers:
        if item % 2 != 0:
            odd_item.append(item)
    return odd_item

print(oddnum([1,2,3,4,5,6]))

'''


def oddnum(numbers):
    return numbers % 2 != 0

print(list(filter(oddnum,[1,2,3,4,5,6])))