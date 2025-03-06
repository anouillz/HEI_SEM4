class State:
    '''Un état d'un AFN avec un identifiant séquentiel lisible.'''
    _next_id = 0  # Attribut de classe servant de compteur d'ID

    def __init__(self):
        # Transitions : dictionnaire { symbole (None pour epsilon): [états cibles] }
        self.transitions = {}
        # Affectation d'un identifiant unique et lisible à chaque état créé
        self.id = State._next_id
        State._next_id += 1

    def add_transition(self, symbol, state):
        '''Ajoute une transition vers state avec le symbole (None pour epsilon).'''
        if symbol in self.transitions:
            self.transitions[symbol].append(state)
        else:
            self.transitions[symbol] = [state]

    def __str__(self):
        lst = []
        for symbole, states in self.transitions.items():
            s_symbole = symbole if symbole is not None else 'ε'
            ids = [s.id for s in states]
            lst.append(f"{s_symbole} -> {ids}")
        return f"State({self.id}): " + ", ".join(lst)


class NFA:
    '''Un AFN qui possède un état initial et un état final.'''

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def display(self):
        '''Affichage simple de l'AFN par parcours en profondeur.'''
        visited = set()

        def dfs(state):
            if state in visited:
                return
            visited.add(state)
            print(state)
            for nexts in state.transitions.values():
                for s in nexts:
                    dfs(s)  # Récursif

        dfs(self.start)


# Création d'un AFN simple pour le symbole 'a'
if __name__ == "__main__":
    start = State()
    finish = State()
    start.add_transition('a', finish)
    nfa_symbol_a = NFA(start, finish)
    nfa_symbol_a.display()
