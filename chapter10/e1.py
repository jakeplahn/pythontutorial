import os
print(os.getcwd())
os.chdir('/Users/jakeplahn')
os.system('mkdir today')
print(dir(os))
print(help(os))
print('end')