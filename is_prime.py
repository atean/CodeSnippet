
def is_prime(num):
    counter = 2

    while counter * counter <= num:
        if num % counter == 0:
            return False
        counter += 1

    return True

'''
natural_numbers = range(1001)
print("prime numbers--%s" % natural_numbers)
a = [i for i in natural_numbers[2:] if is_prime(i)]
print(a)
print(len(a))
'''
# #
# Calculate equilibrium index of the list

def equilibrium_index(this_list):
    equi_index = []

    for i in range(len(this_list)):
        if sum(this_list[:i]) == sum(this_list[i+1:]):
            print("%s = %s" % (sum(this_list[:i]), sum(this_list[i + 1:])))
            equi_index.append(i)

    print(equi_index)

'''
l = [2,1,4,1,1,0,2,3,1]

equilibrium_index(l)
'''

# # fibbonaci series

def fibbo_(max):
    a, b = 0, 1
    print(a)
    while(a <= max):
        a, b = b, a + b
        print(a)

def fibbo_nth_item(nth):

    i = 2
    a, b = 0, 1

    while i <= nth:
        a, b = b, a+b
        i += 1
    return a


def fibbo_r(n):
    if n in (0,1):
        return n

    return fibbo_r(n-1) + fibbo_r(n-2)



# # list builtin simulation

def list_remove_first_occur(l1, item):
    new_list = l1
    for i in range(len(l1)):
        if l1[i] == item:
            new_list = l1[:i] + l1[i+1:]
            break

    return new_list


def list_insert(l1, item, pos):
    return l1[:pos] + [item] + l1[pos:]


def list_remove_nth_occur(l1, item, occur):
    new_list = l1
    remove_index = []

    # get all the indexes with equal value in a list
    for i in range(len(l1)):
        if l1[i] == item:
            remove_index += [i]

    # now remove the nth occurrence from the original list ond return it otherwise return without modification
    if occur <= len(remove_index):
        i = remove_index[occur - 1]
        new_list = l1[:i] + l1[i + 1:]

    return new_list


def list_pop(l1, pos=None):
    if not pos:
        l1

if __name__ == '__main__':
    lit = [2, 9, 88, 3, 10, 11, 88, 88, 88, 3]
    print(list_insert(lit, 99999, -5))