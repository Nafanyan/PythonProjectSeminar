numbers = [1,2,3,4,5,6,7,8]
numbers = list(filter(lambda el: el % 2 == 0, numbers))
print(numbers)