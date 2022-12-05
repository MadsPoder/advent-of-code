import string
from functools import reduce


with open ('day3.txt') as fp:
    rucksacks = [x.strip('\n') for x in fp.readlines()]

def get_priority(rucksack: str) -> int:
    compartment1 = set(rucksack[:len(rucksack)//2])
    compartment2 = set(rucksack[len(rucksack)//2:])

    # Get intersection between the two compartments
    intersection = compartment1.intersection(compartment2).pop()

    # Add 1 as ascii_letters.index is zero indexed
    return string.ascii_letters.index(intersection) + 1

# Part 1. Sum all priorities
print(reduce(lambda previous, current: previous + get_priority(current), rucksacks, 0))

# Convert rucksacks into list of lists with the sublist having size 3 - the size of the elf groups
groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]

def get_priority_for_a_group(group: list[str]) -> int:
    # Get intersection between the 3 rucksacks in the group
    intersection = set.intersection(*[set(rucksack) for rucksack in group]).pop()

    # Add 1 as ascii_letters.index is zero indexed
    return string.ascii_letters.index(intersection) + 1

# Part 2. Sum all priorities for the groups
print(reduce(lambda previous, current: previous + get_priority_for_a_group(current), groups, 0))
