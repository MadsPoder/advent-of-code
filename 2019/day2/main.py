from typing import List

# Read puzzle input
with open('input.txt') as fp:
    intcode_program = [int(intcode) for intcode in fp.readline().split(',')]

# Pre-process to restore the gravity assist program
intcode_program[1] = 12
intcode_program[2] = 2

def intcode_parser(input: List[int]) -> List[int]:
    # Make a copy
    mutated_program = input[:]

    # Imperatively iterate list
    for i in range(len(mutated_program) // 4):
        instruction = mutated_program[i * 4:(i + 1) * 4]

        # Opcode 99 = exit
        if(instruction[0] == 99):
            return mutated_program
        
        # Opcode 1 = addition
        elif(instruction[0] == 1):
            mutated_program[instruction[3]] = mutated_program[instruction[1]] + mutated_program[instruction[2]]
        
        # Opcode 2 = multiplication
        elif(instruction[0] == 2):
            mutated_program[instruction[3]] = mutated_program[instruction[1]] * mutated_program[instruction[2]]

        else:
            print('Something horrible happened')

    return mutated_program

print(f'Solution part one {intcode_parser(intcode_program)[0]}')

# Brute force to get 19690720 yolo
def bruteforce(input: List[int]) -> List[int]:
    for noun in range(100):
        for verb in range(100):
            mutated_list = input[:]
            mutated_list[1] = noun
            mutated_list[2] = verb
            mutated_list = intcode_parser(mutated_list)
            if(mutated_list[0] == 19690720):
                return mutated_list

bruteforced = bruteforce(intcode_program)
print(f'Solution part two {100 * bruteforced[1] + bruteforced[2]}')
