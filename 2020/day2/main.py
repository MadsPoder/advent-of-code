import re
from collections import namedtuple

# {min}-{max} {char}: {password}
pattern = '(\d+)-(\d+) (\w): (\w+)'

# Create tuple to hold
Password = namedtuple('PasswordWithPolicy', ['min', 'max', 'char', 'password'])

# Read puzzle input
with open ('input.txt') as fp:
    data = fp.readlines()

# Unpack captured regex groups to named tuple
passwords = [Password(*re.match(pattern, x).groups()) for x in data]

# Valid passwords have occurences between min and max for the char in the password
valid_passwords_part_1 = list(filter(lambda  x: int(x.min) <= x.password.count(x.char) <= int(x.max), passwords))

print(len(valid_passwords_part_1))

# Valid passwords for part 2 must have the char appear exactly once in the positions defined in min or max
# Similar to XOR. Subtract 1 from index as Toboggan Corporate Policies have no concept of "index zero"!
valid_passwords_part_2 = list(filter(lambda  x: 
    (x.password[int(x.min) - 1] == x.char) ^
    (x.password[int(x.max) - 1] == x.char),
    passwords))

print(len(valid_passwords_part_2))
