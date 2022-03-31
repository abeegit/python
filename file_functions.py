print("Opening file.txt and writing to it")
file_stream =  open('file.txt', 'w')
file_stream.write('Line 1\n')
file_stream.close()
print('Saved and closed file')

print('Reading file')
file_stream = open('file.txt', 'r')
print(file_stream.readline())
file_stream.close()
print('Closed file')

print('Appending to file')
fs = open('file.txt', 'a+') # Adding '+' makes the file readable and writable
print('File contents before appending')
print(fs.read())
print('Appending Line 2')
fs.write('Line 2\n')
print('Closed file')
print('File contents after appending')
print(fs.read())
fs.close()
print('Closed file')

print('Reading all lines efficiently')
with open('file.txt', 'r') as fs:
  for line in fs:
    print(line, end = '')

