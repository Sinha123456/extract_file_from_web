#A string is said to be palindrome
# if reverse of the string is same as string.

def reverse(x):
    return x[::-1]
def isPalindrom(x):
    rev = reverse(x)
    if (x == rev):
        return True
    return False
x = 'mom'
ans = isPalindrom(x)
if ans == 1:
    print('yes')
else:
    print('no')