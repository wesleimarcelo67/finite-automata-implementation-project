# Definição da Máquina de Mealy
class MealyMachine:
    def __init__(self):
        # Estados
        self.estado_atual = 'q0'  # Estado inicial

        # Tabela de transições
        self.transicoes = {
            'q0': {25: 'q1', 50: 'q2', 100: 'q0'},
            'q1': {25: 'q2', 50: 'q3', 100: 'q1'},
            'q2': {25: 'q3', 50: 'q0', 100: 'q2'},
            'q3': {25: 'q0', 50: 'q1', 100: 'q3'}
        }

        # Tabela de saídas
        self.saidas = {
            'q0': {25: 0, 50: 0, 100: 1},
            'q1': {25: 0, 50: 0, 100: 1},
            'q2': {25: 0, 50: 1, 100: 1},
            'q3': {25: 1, 50: 1, 100: 1}
        }

    def processar_entrada(self, entrada):
        # Verifica se a entrada é válida
        if entrada not in self.transicoes[self.estado_atual]:
            print(f"Entrada inválida '{entrada}' para o estado atual '{self.estado_atual}'.")
            return None

        # Obtém a saída correspondente à transição
        saida = self.saidas[self.estado_atual][entrada]

        # Atualiza o estado atual
        self.estado_atual = self.transicoes[self.estado_atual][entrada]

        return saida


# Função principal para testar a Máquina de Mealy
def testar_maquina_mealy(entradas):
    maquina = MealyMachine()
    saidas = []

    for entrada in entradas:
        saida = maquina.processar_entrada(entrada)
        if saida is not None:
            saidas.append(saida)

    return saidas


# Entradas de teste
entradas = [100, 25, 25, 25, 25, 100, 50, 50, 100, 100, 25, 50, 25, 50, 25, 25, 100]

# Processar entradas e obter saídas
saidas = testar_maquina_mealy(entradas)

# Exibir resultados
print("Entradas:", entradas)
print("Saídas:", saidas)