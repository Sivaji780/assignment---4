numbers = [4,5,2,9]

def square(number):
  return number * number
square_numbers = map(square, numbers)


square_list = list(square_numbers)
print(square_list)