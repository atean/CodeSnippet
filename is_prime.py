
def is_prime(num):
    counter = 2

    while counter * counter <= num:
        if num % counter == 0:
            return False
        counter += 1

    return True

natural_numbers = range(1001)
print("prime numbers--%s" % natural_numbers)
a = [i for i in natural_numbers[2:] if is_prime(i)]
print(a)
print(len(a))

# #
# Calculate equilibrium index of the list

def ei(this_list):
    equi_index = []

    for i in range(len(this_list)):
        if sum(this_list[:i]) == sum(this_list[i+1:]):
            print("%s = %s" % (sum(this_list[:i]), sum(this_list[i + 1:])))
            equi_index.append(i)

    print(equi_index)

l = [2,1,4,1,1,0,2,3,1]

ei(l)