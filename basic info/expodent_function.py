
def raise_to_power(base_numb, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_numb
    return result

print(raise_to_power(3,2))