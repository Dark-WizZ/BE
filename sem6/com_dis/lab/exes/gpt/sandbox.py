class State:
    def __init__(self, label):
        self.label = label
        self.transitions = {}

    def add_transition(self, symbol, state):
        if symbol not in self.transitions:
            self.transitions[symbol] = []
        self.transitions[symbol].append(state)


def generate_nfa_from_regex(regex):
    stack = []

    for char in regex:
        if char.isalpha() or char.isdigit():
            # Create an NFA for a single character
            state1 = State(label=str(char))
            state2 = State(label=str(char))
            state1.add_transition(char, state2)
            stack.extend([state1, state2])

        elif char == '|':
            # Union operation
            nfa2, nfa1 = stack.pop(), stack.pop()
            start = State(label='ε')
            end = State(label='ε')
            start.add_transition('ε', nfa1)
            start.add_transition('ε', nfa2)
            nfa1.add_transition('ε', end)
            nfa2.add_transition('ε', end)
            stack.extend([start, end])

        elif char == '.':
            # Concatenation operation
            nfa2, nfa1 = stack.pop(), stack.pop()
            nfa1.transitions.update(nfa2.transitions)
            stack.extend([nfa1, nfa2])

        elif char == '*':
            # Kleene star operation
            nfa = stack.pop()
            start = State(label='ε')
            end = State(label='ε')
            start.add_transition('ε', nfa)
            start.add_transition('ε', end)
            nfa.add_transition('ε', nfa)
            nfa.add_transition('ε', end)
            stack.extend([start, end])

    return stack[0]


def generate_nfa_table(nfa):
    table = {}

    def dfs(state):
        nonlocal table
        if state.label not in table:
            table[state.label] = {}

        for symbol, next_states in state.transitions.items():
            for next_state in next_states:
                if next_state.label not in table[state.label]:
                    table[state.label][next_state.label] = set()
                table[state.label][next_state.label].add(symbol)

                dfs(next_state)

    dfs(nfa)
    return table

# Example usage:
regex = "a.b|c*"
nfa = generate_nfa_from_regex(regex)
print(nfa)
nfa_table = generate_nfa_table(nfa)

# Print the NFA table
print("NFA Table:")
for state, transitions in nfa_table.items():
    for next_state, symbols in transitions.items():
        print(f"{state} -- {', '.join(symbols)} --> {next_state}")
