import re
from collections import namedtuple

# {min}-{max} {char}: {password}
pattern = '(\d+)-(\d+) (\w): (\w+)'

# Create tuple to hold
Password = namedtuple('PasswordWithPolicy', ['min', 'max', 'char', 'password'])

# Read puzzle input
with open ('input.txt') as fp:
    data = fp.readlines()

# Unpack captured reges groups to named tuple
passwords = [Password(*re.match(pattern, x).groups()) for x in data]

# Valid passwords have occurences between min and max for the char in the password
valid_passwords_part_1 = list(filter(lambda  x: int(x.min) <= x.password.count(x.char) <= int(x.max), passwords))

print(len(valid_passwords_part_1))
