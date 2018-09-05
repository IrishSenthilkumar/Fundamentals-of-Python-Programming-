'''
Created on 5 Sep 2018

@author: Irish
'''

# Manipulating the print function using the { end } command
print('______________________________\ 1 /______________________________')
print('The next sentence will be on the same line. ', end='')
print('I told you so.')

# The real, unsimplified, full { print() } function
print('\n______________________________\ 2 /______________________________')
print('Hello World', end='\n')

# Manipulating the print function using the { sep } command
print('\n______________________________\ 3 /______________________________')
w, x, y, z = 1, 2, 3, 4
print(w, x, y, z, sep=' ')
print(w, x, y, z, sep=' LOL ')
print(w, x, y, z, sep='-->')