def get_length():
  print('Enter length of array')
  l = input()
  try:
    l = int(l)
  except ValueError:
    print('Please enter a number')
  return l

length = 0
while length <= 0:
  length = get_length()
  length = 0 if type(length) is not int else length

array = []
for i in range(0, length):
  array.append(input('Enter an element of the array and hit enter: '))

print('Printing contents of array')
print(array)
