def is_prime(x):
    if x < 2:
        return False
    for number in range(2, x - 1):
        if x % number == 0:
            return False
            break
    else:
        return True
