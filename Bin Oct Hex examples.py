# Generate computer numbers in binary base 2, hexadecimal base 16 and octal base
# 8. Type in ASCII codes and see what they look like. For example: 'print(bin(65))' is
# the ASCII code value for the capital letter 'A' in bibary base 2 as: '0b1000001'. Note:
# the '0b' is Python's prefix, which simply tells Python to work with binary base 2
# numbers.

'''----------------------------------------------------------------'''

# Convert any number into a binary base 2 number.

print(bin(255))

# Convert any number into a hexadecimal base 16 number.

print(hex(255))

# Convert any number into an octal base 8 number.

print(oct(255))

'''----------------------------------------------------------------'''

# Type and execute/run each of these program examples below and see what
# happens.

comp_nums=int(input('Please type any number to see its binary base 2 number \
value: ').strip())

print(f'The number {comp_nums} = the binary base 2 number value: \
{bin(comp_nums)}.')

comp_nums=int(input('Please type any number to see its hexadecimal base 16 \
number value: ').strip())

print(f'The number {comp_nums} = the hexadecimal base 16 number value: \
{hex(comp_nums)}.')
            
comp_nums=int(input('Please type any number to see its octal base 8 \
number value: ').strip())

print(f'The number {comp_nums} = the octal base 8 number value: \
{oct(comp_nums)}.')
