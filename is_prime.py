
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