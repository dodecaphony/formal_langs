class NFAState:
    def __init__(self, is_final=False):
        self.is_final = is_final
        self.transitions = {}  # symbol -> set of NFAStates
        self.epsilon_transitions = set()  # set of NFAStates

    def add_transition(self, symbol, state):
        if symbol not in self.transitions:
            self.transitions[symbol] = set()
        self.transitions[symbol].add(state)

    def add_epsilon_transition(self, state):
        self.epsilon_transitions.add(state)


class NFA:
    def __init__(self):
        self.start_state = NFAState()
        self.states = [self.start_state]

    def add_state(self, is_final=False):
        state = NFAState(is_final)
        self.states.append(state)
        return state

    def clone(self):
        clone_map = {original: NFAState(original.is_final) for original in self.states}
        for original, clone in clone_map.items():
            for symbol, next_states in original.transitions.items():
                clone.transitions[symbol] = {clone_map[next_state] for next_state in next_states}
            clone.epsilon_transitions = {clone_map[next_state] for next_state in original.epsilon_transitions}

        cloned_nfa = NFA()
        cloned_nfa.start_state = clone_map[self.start_state]
        cloned_nfa.states = list(clone_map.values())
        return cloned_nfa

    def merge(self, other):
        merged_nfa = NFA()
        merged_nfa.start_state.add_epsilon_transition(self.start_state)
        merged_nfa.start_state.add_epsilon_transition(other.start_state)

        final_state = NFAState(is_final=True)
        for state in self.states + other.states:
            if state.is_final:
                state.is_final = False
                state.add_epsilon_transition(final_state)

        merged_nfa.states.extend(self.states)
        merged_nfa.states.extend(other.states)
        merged_nfa.states.append(final_state)
        return merged_nfa


def build_nfa_from_regex(regex):
    nfa_stack = []
    for char in regex:
        if char in {'a', 'b'}:
            nfa = NFA()
            end_state = nfa.add_state(is_final=True)
            nfa.start_state.add_transition(char, end_state)
            nfa_stack.append(nfa)
        elif char == '*':
            nfa = nfa_stack.pop()
            start_state = NFAState()
            end_state = NFAState(is_final=True)
            start_state.add_epsilon_transition(nfa.start_state)
            start_state.add_epsilon_transition(end_state)
            nfa.states[-1].is_final = False
            nfa.states[-1].add_epsilon_transition(nfa.start_state)
            nfa.states[-1].add_epsilon_transition(end_state)
            nfa.start_state = start_state
            nfa.states.append(start_state)
            nfa.states.append(end_state)
            nfa_stack.append(nfa)
        elif char == '?':
            nfa = nfa_stack.pop()
            nfa.start_state.add_epsilon_transition(nfa.states[-1])
            nfa_stack.append(nfa)
        elif char == '|':
            right_nfa = nfa_stack.pop()
            left_nfa = nfa_stack.pop()
            nfa_stack.append(left_nfa.merge(right_nfa))
        elif char == '(':
            nfa_stack.append('(')
        elif char == ')':
            sub_nfas = []
            while nfa_stack[-1] != '(':
                sub_nfas.append(nfa_stack.pop())
            nfa_stack.pop()  # Remove '('
            sub_nfas.reverse()
            nfa = sub_nfas[0]
            for sub_nfa in sub_nfas[1:]:
                nfa = nfa.merge(sub_nfa)
            nfa_stack.append(nfa)

    if len(nfa_stack) > 1:
        nfa = nfa_stack[0]
        for sub_nfa in nfa_stack[1:]:
            nfa = nfa.merge(sub_nfa)
        return nfa
    else:
        return nfa_stack[0]


# Test the NFA construction with the regex
regex = "(ab)*a?|(ba)*b?"
nfa = build_nfa_from_regex(regex)

# Print out the NFA structure
for i, state in enumerate(nfa.states):
    transitions = {symbol: [nfa.states.index(t) for t in states] for symbol, states in state.transitions.items()}
    epsilon_transitions = [nfa.states.index(t) for t in state.epsilon_transitions]
    print(f"State {i}: Final={state.is_final}, Transitions={transitions}, Epsilon={epsilon_transitions}")
