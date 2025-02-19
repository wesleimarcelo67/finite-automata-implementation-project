# Definição do AFD ajustado
class AFD:
    def __init__(self):
        # Estados: q0, q1, q2, q3
        self.estado_atual = 'q0'  # Estado inicial
        self.estados_finais = {'q0', 'q3'}  # Estados de aceitação

        # Tabela de transições
        self.transicoes = {
            'q0': {'0': 'q0', '1': 'q1'},  # Em q0, lendo '0' permanece em q0; lendo '1' vai para q1
            'q1': {'0': 'q2'},  # Em q1, lendo '0' vai para q2; lendo '1' rejeita
            'q2': {'0': 'q3'},  # Em q2, lendo '0' vai para q3; lendo '1' rejeita
            'q3': {'0': 'q3', '1': 'q1'},  # Em q3, lendo '0' permanece em q3; lendo '1' vai para q1
        }

    def processar_cadeia(self, cadeia):
        self.estado_atual = 'q0'  # Reinicia o estado atual para o inicial

        for simbolo in cadeia:
            if simbolo not in {'0', '1'}:
                print(f"Erro: Símbolo inválido '{simbolo}' na cadeia.")
                return False

            # Atualiza o estado atual com base na função de transição
            if self.estado_atual in self.transicoes and simbolo in self.transicoes[self.estado_atual]:
                self.estado_atual = self.transicoes[self.estado_atual][simbolo]

        # Verifica se o estado final é de aceitação
        return self.estado_atual in self.estados_finais


# Função principal para testar o AFD
def testar_afd(cadeia):
    afd = AFD()
    if afd.processar_cadeia(cadeia):
        print(f'A cadeia "{cadeia}" é ACEITA pelo AFD.')
    else:
        print(f'A cadeia "{cadeia}" é REJEITADA pelo AFD.')


# Testes
testar_afd("0")
testar_afd("0100")
testar_afd("100")
testar_afd("1")
testar_afd("1001")
testar_afd("010")
testar_afd("0001")