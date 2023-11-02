# ЗАДАЧА:
# A = {1}.
# Если число чётное и больше 0 - в конце напечатать "**",
# Если число нечётное и больше 0 - в конце напечатать "*",
# = 0 - ничего.

class TuringMachine:
    def __init__(self, tape, initial_state, transition_function, final_states):
        self.tape = list(tape)
        self.head = 0
        self.state = initial_state
        self.transition_function = transition_function
        self.final_states = final_states

    def run(self):
        while self.state not in self.final_states:

            # Выходим за границы ленты
            if self.head >= len(self.tape):
                self.tape.append('_')
            if self.head < 0:
                self.tape.insert(0, '_')

            # Проверяем, существует ли правило перехода для текущего состояния self.state
            # и текущего символа symbol в функции переходов self.transition_function
            symbol = self.tape[self.head]
            if (self.state, symbol) not in self.transition_function:
                break

            new_symbol, move, new_state = self.transition_function[(self.state, symbol)]
            self.state = new_state
            self.tape[self.head] = new_symbol

            if move == 'L':
                self.head -= 1
            elif move == 'R':
                self.head += 1

    def get_tape(self):
        return ''.join(self.tape)

# Пример использования:

# Словарь, который содержит правила перехода для машины Тьюринга
transition_function = {
    ('S0', '1'): ('1', 'R', 'S3'),
    ('S0', '_'): ('', 'L', 'SEnd'),
    ('S3', '1'): ('1', 'R', 'S2'),
    ('S3', '_'): ('', 'L', 'SEnd'),
    ('S2', '1'): ('1', 'R', 'S5'),
    ('S2', '_'): ('*', 'L', 'SEnd'),
    ('S5', '1'): ('1', 'R', 'S2'),
    ('S5', '_'): ('*', 'R', 'S6'),
    ('S6', '_'): ('*', 'L', 'SEnd'),
}

initial_state = 'S0'
final_states = {'SEnd'}

tm = TuringMachine('111', initial_state, transition_function, final_states)

tm.run()

print("Результат работы машины Тьюринга:", tm.get_tape())

