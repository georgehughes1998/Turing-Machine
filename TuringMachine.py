LEFT = "L"
RIGHT = "R"
HALT = "H"


class TuringMachine:
    def __init__(self, symbols, states, initial_state, tape, rules=None):
        self.rules = dict()
        self.symbols = symbols
        self.states = states

        self.blank = symbols[0]

        self.head = 0

        self.check_valid_state(initial_state)
        self.state = initial_state

        for q in tape:
            self.check_valid_symbol(q)
        if not tape:
            tape = [self.blank]
        self.tape = dict(enumerate(tape))

        self.last_move = None

        if rules:
            for r in rules:
                old_symbol, old_state = r
                new_state, direction, new_symbol = rules[r]

                self.add_rule(old_symbol, old_state, new_state, direction, new_symbol)

    def step(self):
        if self.state == HALT:
            return HALT
        else:
            # Identify rule
            # lhs = (self.tape[self.head], self.state)
            # new_state, direction, new_symbol = rhs = self.rules[lhs]
            lhs, rhs = self.get_next_move()
            new_state, direction, new_symbol = rhs

            # Set symbol
            self.tape[self.head] = new_symbol

            # Move head
            if direction == LEFT:
                self.head -= 1
            if direction == RIGHT:
                self.head += 1

            # Set state
            self.state = new_state

            # Ensure tape at head has value
            if self.head not in self.tape:
                self.tape[self.head] = self.blank

            self.last_move = lhs, rhs
            return lhs, rhs

    def add_rule(self, old_symbol, old_state, new_state, direction, new_symbol):
        self.check_valid_symbol(old_symbol)
        self.check_valid_symbol(new_symbol)

        self.check_valid_state(old_state)
        self.check_valid_state(new_state)

        self.rules[(old_symbol, old_state)] = (new_state, direction, new_symbol)

    def check_rules_complete(self):
        for s in self.states:
            for q in self.symbols:
                try:
                    s1, d, q1 = self.rules[(q, s)]
                except KeyError:
                    raise Exception(f"Missing rule for {q, s}")

    def is_halted(self):
        return self.state == HALT

    def get_tape(self):
        return self.tape

    def get_state(self):
        return self.state

    def get_head_pos(self):
        return self.head

    def get_rules(self):
        return self.rules

    def get_last_move(self):
        return self.last_move

    def get_next_move(self):
        if self.is_halted():
            return None
        else:
            lhs = (self.tape[self.head], self.state)
            rhs = self.rules[lhs]
            return lhs, rhs

    def __str__(self):
        keys = list(self.tape.keys())
        keys.sort()
        res = [(f"{self.state}{self.tape[pos]}" if pos == self.head else self.tape[pos]) for pos in keys]
        return str(res)

    def check_valid_state(self, state):
        if state not in self.states + [HALT]:
            raise Exception(f"Invalid state: {state}")

    def check_valid_symbol(self, symbol):
        if symbol not in self.symbols:
            raise Exception(f"Invalid symbol: {symbol}")
