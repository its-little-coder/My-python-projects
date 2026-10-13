#half adder
def half_adder(a, b):
    sum_bits = a ^ b
    carry_bits = a & b
    return sum_bits, carry_bits
#full adder
def full_adder(a, b, carry_in):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, carry_in)
    final_carry = carry1 | carry2   # OR gate
    return sum2, final_carry
#testing
print(full_adder(0, 0, 0))
print(full_adder(0, 0, 1))
print(full_adder(0, 1, 0))
print(full_adder(0, 1, 1))
print(full_adder(1, 0, 0))
print(full_adder(1, 0, 1))
print(full_adder(1, 1, 0))
print(full_adder(1, 1, 1))
