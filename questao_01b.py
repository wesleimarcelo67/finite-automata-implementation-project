# Definição do AFD ajustado
class AFD:
    def __init__(self):
        # Estados: q0, q1, q2, q3
        self.estado_atual = 'q0'  # Estado inicial
        self.estados_finais = {'q2'}  # Estado de aceitação

        # Tabela de transições
        self.transicoes = {
            'q0': {'a': 'q1', 'b': 'q2'},  # Em q0, lendo 'a' vai para q1; lendo 'b' vai para q2
            'q1': {'a': 'q0', 'b': 'q3'},  # Em q1, lendo 'a' vai para q0; lendo 'b' vai para q3
            'q2': {'a': 'q3', 'b': 'q2'},  # Em q2, lendo 'a' vai para q3; lendo 'b' permanece em q2
            'q3': {'a': 'q2', 'b': 'q3'},  # Em q3, lendo 'a' vai para q2; lendo 'b' permanece em q3
        }

    def processar_cadeia(self, cadeia):
        self.estado_atual = 'q0'  # Reinicia o estado atual para o inicial

        for simbolo in cadeia:
            if simbolo not in {'a', 'b'}:
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
testar_afd("b")
testar_afd("aab")   
testar_afd("babab")
testar_afd("baab")
testar_afd("a")
testar_afd("ab")
testar_afd("bab")
testar_afd("aba")