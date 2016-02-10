f = open('workfile2.txt', 'w')

charsWritten = f.write('This is a text\n')
print(charsWritten)

value = ('the answer', 42)
s = str(value)
charsWritten = f.write(s)
print(charsWritten)

print(f.tell())