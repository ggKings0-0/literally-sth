def from_celsia_to_farengeit(C):
    F = (5/9)*(C+32)
    return F
def from_farengeit_to_celsia(F):
    C = (5/9)*F + 32
    return C
def calvin(K):
    C = K - 273
    return C
def celsia_to_calvin(C):
    K = 273 + C
    return K
yes_or_not = input('Enter your starter(K, C, F): ')
to_sth = input('Convert to')
if yes_or_not == 'K' and to_sth == 'C':
    K = int(input('Enter number of calvins'))
    if K < 0:
        print('Invalid data // Try again')
        while K < 0:
            K = int(input())
    if K >= 0:
        print(calvin(K))
if yes_or_not == 'K' and to_sth == 'F':
    print('Try to convert to celsias first and when to farengeit')
    to_sth = input()
if yes_or_not == 'C':
    C = int(input())
    if to_sth == 'K':
        if C > -273:
            print(celsia_to_calvin(C))
        else:
            print('Invalid data // Enter again')
            C = int(input())
    elif to_sth == 'F':
        print(from_celsia_to_farengeit(C))
elif yes_or_not == 'F':
    F = int(input())
    print(from_farengeit_to_celsia(F))
