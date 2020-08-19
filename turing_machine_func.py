from random import choice
from TuringMachine import TuringMachine, HALT, LEFT, RIGHT


def generate_random_turing_machine(num_symbols=2, num_states=2, tape_length=1):
    symbols = [f"q{q}" for q in range(num_symbols)]
    states = [f"S{s}" for s in range(num_states)]

    initial_state = states[0]
    tape = [choice(symbols) for i in range(tape_length)]

    tm = TuringMachine(symbols, states, initial_state, tape)

    # Design a machine
    for q in range(num_symbols):
        for s in range(num_states):
            tm.add_rule(symbols[q], states[s], choice(states + [HALT]), choice([LEFT, RIGHT]),
                        choice(symbols))

    tm.check_rules_complete()

    return tm
