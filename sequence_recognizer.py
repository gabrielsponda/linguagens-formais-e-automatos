from automathon import DFA
from automathon import NFA

# Função para converter caracteres, de forma que toda letra maiúscula é convertida em um 'A', toda letra minúscula é convertida em um 'a', todo número é convertido em um '1' e qualquer outro caracter (caracteres especiais) é convertido em um '#'.
def categorizar_entrada(entrada):
    entrada_categorizada = ""
    for char in entrada:
        if char.islower():  # Checa se é minúscula
            entrada_categorizada += 'a'
        elif char.isupper():  # Checa se é maiúscula
            entrada_categorizada += 'A'
        elif char.isdigit():  # Checa se é dígito
            entrada_categorizada += '1'
        else:  # Assume que o restante são caracteres especiais
            entrada_categorizada += '#'
    return entrada_categorizada

#Função que cria um atômato a partir do produto de outros dois autômatos.
def automata_product_dfa(M, N):
    # Novo conjunto de estados: produto dos conjuntos de estados,
    # convertendo cada par de estados em uma string formatada
    Q_new = {f"{q1},{q2}" for q1 in M.Q for q2 in N.Q}

    # Novo alfabeto: união dos alfabetos (que, neste caso, são iguais)
    sigma_new = M.sigma.union(N.sigma)

    # Nova função de transição
    delta_new = {}
    for q1 in M.Q:
        for q2 in N.Q:
            q_new = f"{q1},{q2}"
            delta_new[q_new] = {}
            for a in sigma_new:
                delta_new[q_new][a] = f"{M.delta[q1][a]},{N.delta[q2][a]}"

    # Novo estado inicial
    initialState_new = f"{M.initialState},{N.initialState}"

    # Novo conjunto de estados finais
    F_new = {f"{q1},{q2}" for q1 in M.F for q2 in N.F}

    # Cria o novo DFA
    new_dfa = DFA(Q_new, sigma_new, delta_new, initialState_new, F_new)
    return new_dfa

    
def main():
    print("\n\nLINGUAGENS FORMAIS E AUTOMATA")
    
    print("\n\n→Criando o autômato M, que reconhece sequências de 8 caracteres.")
    # Autômato M
    Q_m = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
    sigma_m = {'a', 'A', '#', '1'}
    delta_m = {
        'q0': {'a': 'q1', 'A': 'q1', '#': 'q1', '1': 'q1'},
        'q1': {'a': 'q2', 'A': 'q2', '#': 'q2', '1': 'q2'},
        'q2': {'a': 'q3', 'A': 'q3', '#': 'q3', '1': 'q3'},
        'q3': {'a': 'q4', 'A': 'q4', '#': 'q4', '1': 'q4'},
        'q4': {'a': 'q5', 'A': 'q5', '#': 'q5', '1': 'q5'},
        'q5': {'a': 'q6', 'A': 'q6', '#': 'q6', '1': 'q6'},
        'q6': {'a': 'q7', 'A': 'q7', '#': 'q7', '1': 'q7'},
        'q7': {'a': 'q8', 'A': 'q8', '#': 'q8', '1': 'q8'},
        'q8': {'a': 'q8', 'A': 'q8', '#': 'q8', '1': 'q8'}
    }
    initialState_m = 'q0'
    F_m = {'q8'}

    M = DFA(Q_m, sigma_m, delta_m, initialState_m, F_m)

    # Autômato N
    print("\n\n→Criando o autômato N, que reconhece sequências que contenham um caracter de cada tipo.")
    Q_n = {f'q{i}' for i in range(16)}
    sigma_n = {'a', 'A', '#', '1'}
    delta_n = {
        'q0': {'a': 'q1', 'A': 'q2', '#': 'q3', '1': 'q4'},
        'q1': {'a': 'q1', 'A': 'q5', '#': 'q6', '1': 'q7'},
        'q2': {'a': 'q5', 'A': 'q2', '#': 'q8', '1': 'q9'},
        'q3': {'a': 'q6', 'A': 'q8', '#': 'q3', '1': 'q10'},
        'q4': {'a': 'q7', 'A': 'q9', '#': 'q10', '1': 'q4'},
        'q5': {'a': 'q5', 'A': 'q5', '#': 'q11', '1': 'q12'},
        'q6': {'a': 'q6', 'A': 'q11', '#': 'q6', '1': 'q13'},
        'q7': {'a': 'q7', 'A': 'q12', '#': 'q13', '1': 'q7'},
        'q8': {'a': 'q11', 'A': 'q8', '#': 'q8', '1': 'q14'},
        'q9': {'a': 'q12', 'A': 'q9', '#': 'q14', '1': 'q9'},
        'q10': {'a': 'q13', 'A': 'q14', '#': 'q10', '1': 'q10'},
        'q11': {'a': 'q11', 'A': 'q11', '#': 'q11', '1': 'q15'},
        'q12': {'a': 'q12', 'A': 'q12', '#': 'q15', '1': 'q12'},
        'q13': {'a': 'q13', 'A': 'q15', '#': 'q13', '1': 'q13'},
        'q14': {'a': 'q15', 'A': 'q14', '#': 'q14', '1': 'q14'},
        'q15': {'a': 'q15', 'A': 'q15', '#': 'q15', '1': 'q15'}
    }
    initial_state_n = 'q0'
    F_n = {'q15'}

    N = DFA(Q_n, sigma_n, delta_n, initial_state_n, F_n)

    print("\n\n→Testando a validade de cada autômato.")
    print("O autômato M é válido: ", M.is_valid(), ".")
    print("O autômato M é válido: ", N.is_valid(), ".")
    
    print("\n\n→Testando entradas em cada um dos autômatos. Entre com o caracter '!' para terminar os testes.")
    entrada = ""
    while entrada != "!":
        entrada = input("\nDigite uma sequência: ")
        if entrada != "!":
            print("O autômato M aceita a cadeia ", entrada, ": ", M.accept(categorizar_entrada(entrada)), ".")
            print("O autômato N aceita a cadeia ", entrada, ": ", N.accept(categorizar_entrada(entrada)), ".")
        else: 
            print("Continuando...")
    
    #print("\n\nGerando arquivos de visualização dos autômatos M e N.")
    #M.view(
    #    file_name="m",
    #    node_attr={'fontsize': '20'},
    #    edge_attr={'fontsize': '20pt'}
    #)
    #N.view(
    #    file_name="n",
    #    node_attr={'fontsize': '20'},
    #    edge_attr={'fontsize': '20pt'}
    #)
    
    print("\n\n→Gerando o autômato O, que reconhe cadeia de 8 caracteres e se existem ao menos um caractere de cada tipo.")
    O = automata_product_dfa(M, N)
    
    print("\n\n→Testando a validade do autômato.")
    print("\nO autômato O é válido: ", O.is_valid(), ".")
    
    print("\n\n→Testando entradas no autômato. Entre com o caracter '!' para terminar os testes.")
    entrada = ""
    while entrada != "!":
        entrada = input("\nDigite uma sequência: ")
        if entrada != "!":
            print("O autômato O aceita a cadeia ", entrada, ": ", O.accept(categorizar_entrada(entrada)), ".")
        else: 
            print("Continuando...")
            
    #print("\n\nGerando arquivo de visualização do autômato O.")
    #O.view(
    #    file_name="o",
    #    node_attr={'fontsize': '20'},
    #    edge_attr={'fontsize': '20pt'}
    #)
    
    print("\n\n→Convertendo o autômato O para um NFA, que chamaremos de O_NFA.")
    O_nfa = O
    O_nfa = O_nfa.get_nfa()
    
    #print("\n\nGerando arquivo de visualização do autômato O_NFA.")
    #O_nfa.view(
    #    file_name="o_nfa",
    #    node_attr={'fontsize': '20'},
    #    edge_attr={'fontsize': '20pt'}
    #)
    
    print("\n\n→Minimizando o autômato O_NFA.")
    O_nfa = O_nfa.minimize()
    
    #print("\n\nGerando arquivo de visualização do autômato O_NFA minimizado.")
    #O_nfa.view(
    #    file_name="o_nfa",
    #    node_attr={'fontsize': '20'},
    #    edge_attr={'fontsize': '20pt'}
    #)
    
    print("\n\n→Convertendo o autômato O_NFA minimizado para um DFA, que chamaremos de O_minimized.")
    O_minimized = O_nfa.get_dfa()
    
    print("\n\n→Testando a validade do autômato.")
    print("\nO autômato O_minimized é válido: ", O_minimized.is_valid(), ".")
    
    print("\n\n→Testando entradas no autômato O_minimized. Entre com o caracter '!' para terminar os testes.")
    entrada = ""
    while entrada != "!":
        entrada = input("\nDigite uma sequência: ")
        if entrada != "!":
            print("O autômato O_minimized aceita a cadeia ", entrada, ": ", O_minimized.accept(categorizar_entrada(entrada)), ".")
        else: 
            print("Continuando...")
            
if __name__ == "__main__":
    main()