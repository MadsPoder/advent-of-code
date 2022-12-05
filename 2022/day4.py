with open ('day4.txt') as fp:
    pairs = [tuple(x.strip('\n').split(',')) for x in fp.readlines()]

# Convenience method
def is_range_subset(range1: range, range2: range) -> bool:
    return range1.start in range2 and range1.stop in range2

def get_overlapping_totally(assignment_pair: tuple[str, str]) -> bool:
    # Get ranges for each elf - unpack tuple into start stop
    elf1 = range(*[int(section) for section in assignment_pair[0].split('-')])
    elf2 = range(*[int(section) for section in assignment_pair[1].split('-')])

    # Add 1 for inclusivety in end when comparing
    return is_range_subset(elf1, range(elf2.start, elf2.stop + 1))  or is_range_subset(elf2, range(elf1.start, elf1.stop + 1))

totally_overlapping_pairs = list(filter(get_overlapping_totally, pairs))

# Part 1. get all totally overlapping pairs
print(len(totally_overlapping_pairs))

def get_overlapping_partially(assignment_pair: tuple[str, str]) -> bool:
    # Get ranges for each elf 
    elf1 = range(*[int(section) for section in assignment_pair[0].split('-')])
    elf2 = range(*[int(section) for section in assignment_pair[1].split('-')])

    # Check for partially overlap - note max and min are probably not the most efficient
    return max(elf1.start, elf2.start) <= min(elf1.stop, elf2.stop)

partially_overlapping_pairs = list(filter(get_overlapping_partially, pairs))

# Part 2. get all partially overlapping pairs
print(len(partially_overlapping_pairs))