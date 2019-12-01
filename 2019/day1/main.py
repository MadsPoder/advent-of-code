from functools import reduce

# Read puzzle input
with open ('input.txt') as fp:
    data = [int(line.strip()) for line in fp.readlines()]

# Sum up values for fuel usage
sum_of_fuel_modules = reduce(lambda x, y: ((y // 3) - 2) + x, data, 0)

# Print solution
print(f'Solution for part one: {sum_of_fuel_modules}')

# Recursively calculate fuel required for each fuel mass
def add_fuel_for_fuel(mass: int) -> int:
    if mass <= 0:
        return 0

    else:
        fuel = (mass // 3) - 2
        return fuel + add_fuel_for_fuel(fuel) if fuel > 0 else 0

# Sum up values for fuel usage ( with each its own fuel usage )
sum_of_fuel_modules_with_fuel = reduce(lambda x, y: add_fuel_for_fuel(y) + x, data, 0)

# Print solution
print(f'Solution for part two: {sum_of_fuel_modules_with_fuel}')
