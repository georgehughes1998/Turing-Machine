from turing_machine_func import generate_random_turing_machine
import sys


def test_run_turing_machine(turing_machine):
    # Test Run
    for s in range(100):
        step = turing_machine.step()

        if turing_machine.is_halted():
            return True
    return False


# Test some machines and output how many halted
num_halted = 0
num_tested = 0

num_to_test = 100

max_num_symbols = 20
max_num_states = 20
max_tape_length = 20

total_to_do = num_to_test * max_num_symbols * max_num_states * max_tape_length

for rep in range(num_to_test):
    for num_symbols in range(1, max_num_symbols):
        for num_states in range(1, max_num_states):
            for tape_length in range(max_tape_length):
                tm = generate_random_turing_machine(num_symbols=num_symbols, num_states=num_states, tape_length=max_tape_length)
                if test_run_turing_machine(tm):
                    num_halted += 1
                num_tested += 1

            percentage_halted = round((num_halted / num_tested) * 100, 2)
            percentage_done = round((num_tested / total_to_do) * 100, 2)
            sys.stdout.write(f"\r{num_halted}/{num_tested} machines halted ({percentage_halted}%) - {percentage_done}% done.")
            sys.stdout.flush()
print()
