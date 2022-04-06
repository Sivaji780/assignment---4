numbers = [1,2,3,4,5,6,7]

def multiple(number):
  return number * 3
multiple_numbers = map(multiple, numbers)


three_table = list(multiple_numbers)
print(three_table)
