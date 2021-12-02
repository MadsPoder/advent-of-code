# Playing with pattern matching in python 3.10

# Add lambda to parse commands into command and corresponding units
parse_command = lambda x, y: (x, int(y))

# Read puzzle input
with open ('day2.txt') as fp:
    commands = [parse_command(*x.strip().split(' ')) for x in fp.readlines()]

horizontal_position = 0
depth = 0

for command in commands:
    match command:
        case ['forward', units]:
            horizontal_position = horizontal_position + units
        case ['down', units]: 
            depth = depth + units
        case ['up', units]:
            depth = depth - units

# Part 1
print(depth * horizontal_position)

# Part 2
aim = 0
horizontal_position = 0
depth = 0

for command in commands:
    match command:
        case ['forward', units]:
            horizontal_position = horizontal_position + units
            depth = depth + (aim * units)
        case ['down', units]: 
            aim = aim + units
        case ['up', units]:
            aim = aim - units

print(depth * horizontal_position)