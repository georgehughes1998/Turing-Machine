from TuringMachine import TuringMachine

# Pointer moves back and forth between two extreme points on the tape
BACK_AND_FORTH = {
    'initial_state': "S0",
    'states': ["S0", "S1", "S2"],
    'symbols': ["q0", "q1"],
    'rules': {('q0', 'S0'): ('S1', 'R', 'q1'),
              ('q1', 'S1'): ('S1', 'R', 'q0'),
              ('q0', 'S1'): ('S2', 'L', 'q0'),
              ('q1', 'S0'): ('S0', 'L', 'q0'),
              ('q0', 'S2'): ('S2', 'L', 'q1'),
              ('q1', 'S2'): ('S1', 'R', 'q1')},
    'tape': ["q0"] + ["q1"] * 8 + ["q0"]
}

# Unary adder
UNARY_ADDER = {
    'initial_state': "S0",
    'states': ["S0", "S1", "S2", "S3", "S4", "S5"],
    'symbols': ["q0", "q1"],
    'rules': {('q0', 'S0'): ('H', 'R', 'q0'),
              ('q1', 'S0'): ('S1', 'R', 'q1'),
              ('q0', 'S1'): ('S2', 'R', 'q0'),
              ('q1', 'S1'): ('S1', 'R', 'q1'),
              ('q0', 'S2'): ('S3', 'L', 'q0'),
              ('q1', 'S2'): ('S2', 'R', 'q1'),
              ('q1', 'S3'): ('S4', 'L', 'q0'),
              ('q1', 'S4'): ('S4', 'L', 'q1'),
              ('q0', 'S4'): ('S5', 'L', 'q1'),
              ('q0', 'S5'): ('H', 'R', 'q0'),
              ('q1', 'S5'): ('S5', 'L', 'q1')},
    'tape': ["q1"] * 1 + ["q0"] + ["q1"] * 7
}



# Function to get a turing machine using the above configuration format
def create_machine_from_configuration(conf):
    tm = TuringMachine(symbols=conf['symbols'],
                       states=conf['states'],
                       initial_state=conf['initial_state'],
                       tape=conf['tape'],
                       rules=conf['rules'])

    return tm
