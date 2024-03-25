from graphviz import Digraph


class NFAState:
    def __init__(self, is_final=False):
        self.is_final = is_final
        self.transitions = {}
        self.epsilon_transitions = set()

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


def visualize_nfa(nfa):
    dot = Digraph()
    for state in nfa.states:
        if state.is_final:
            dot.node(str(nfa.states.index(state)), shape='doublecircle')
        else:
            dot.node(str(nfa.states.index(state)), shape='circle')

    for i, state in enumerate(nfa.states):
        for symbol, states in state.transitions.items():
            for target in states:
                dot.edge(str(i), str(nfa.states.index(target)), label=symbol)
        for target in state.epsilon_transitions:
            dot.edge(str(i), str(nfa.states.index(target)), label='ε')

    dot.attr(rankdir='LR')
    return dot


class DFAState:
    def __init__(self, nfa_states):
        self.nfa_states = frozenset(nfa_states)
        self.is_final = any(state.is_final for state in nfa_states)
        self.transitions = {}

    def add_transition(self, symbol, state):
        self.transitions[symbol] = state


class DFA:
    def __init__(self):
        self.start_state = None
        self.states = []

    def build_from_nfa(self, nfa):
        self.states = []
        self.start_state = None

        def epsilon_closure(states):
            closure = set(states)
            stack = list(states)
            while stack:
                state = stack.pop()
                for next_state in state.epsilon_transitions:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
            return closure

        def move(states, symbol):
            return {target for state in states for target in state.transitions.get(symbol, [])}

        initial_closure = epsilon_closure([nfa.start_state])
        self.start_state = DFAState(initial_closure)
        unmarked_states = [self.start_state]
        self.states.append(self.start_state)

        while unmarked_states:
            dfa_state = unmarked_states.pop(0)
            for symbol in {symbol for state in dfa_state.nfa_states for symbol in state.transitions}:
                targets = epsilon_closure(move(dfa_state.nfa_states, symbol))
                if not targets:
                    continue
                existing_state = next((state for state in self.states if state.nfa_states == targets), None)
                if not existing_state:
                    new_dfa_state = DFAState(targets)
                    self.states.append(new_dfa_state)
                    unmarked_states.append(new_dfa_state)
                    dfa_state.add_transition(symbol, new_dfa_state)
                else:
                    dfa_state.add_transition(symbol, existing_state)

        return self

    def print_dfa(self):
        for i, state in enumerate(self.states):
            transitions = {symbol: self.states.index(target) for symbol, target in state.transitions.items()}
            print(f"State {i}: Final={state.is_final}, Transitions={transitions}")


def visualize_dfa(dfa):
    dot = Digraph()
    for i, state in enumerate(dfa.states):
        if state.is_final:
            dot.node(str(i), shape='doublecircle')
        else:
            dot.node(str(i), shape='circle')

    for i, state in enumerate(dfa.states):
        for symbol, target in state.transitions.items():
            dot.edge(str(i), str(dfa.states.index(target)), label=symbol)

    dot.attr(rankdir='LR')
    return dot


def main():
    regex = "(ab)*a?|(ba)*b?"
    nfa = build_nfa_from_regex(regex)
    nfa_dot = visualize_nfa(nfa)
    nfa_dot.render('nfa', format='png', cleanup=True)

    dfa = DFA().build_from_nfa(nfa)
    dfa.print_dfa()
    dfa_dot = visualize_dfa(dfa)
    dfa_dot.render('dfa', format='png', cleanup=True)

    for i, state in enumerate(nfa.states):
        transitions = {symbol: [nfa.states.index(t) for t in states] for symbol, states in state.transitions.items()}
        epsilon_transitions = [nfa.states.index(t) for t in state.epsilon_transitions]
        print(f"State {i}: Final={state.is_final}, Transitions={transitions}, Epsilon={epsilon_transitions}")


if __name__ == '__main__':
    main()
