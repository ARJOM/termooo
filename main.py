import random


def get_words():
    resultado = []
    with open('palavras.txt', 'rt', encoding='utf-8') as palavras:
        for palavra in palavras:
            resultado.append(palavra)
    return resultado

def get_termo():
    return random.choice(get_words())

def verificar(palavra, palpite):
    mensagens = [f'O palpite foi {palpite}']
    if palavra == palpite+'\n':
        mensagens.append('Venceu')
    else:
        for i in range(5):
            if palavra[i] == palpite[i]:
                mensagens.append(f'A letra {palpite[i]} está na posição correta')
            elif palpite[i] in palavra:
                mensagens.append(f'A letra {palpite[i]} está na palavra, mas na posição incorreta')
            else:
                mensagens.append(f'A letra {palpite[i]} não está na palavra')
    
    for mensagem in mensagens:
        print(mensagem)

def verificar_automatico(palavra, palpite, informacoes):
    print(f'O palpite é {palpite}')
    for i in range(5):
        if palavra[i] == palpite[i]:
            print(f'A letra {palpite[i]} está na posição correta')
            informacoes[palpite[i]] = {'esta': True, 'posicao': i}
        elif palpite[i] in palavra:
            print(f'A letra {palpite[i]} está na palavra, mas na posição incorreta')
            if palpite[i] in list(informacoes.keys()):
                if 'posicao' not in list(informacoes[palpite[i]].keys()):
                    informacoes[palpite[i]]['posicao_nao'].append(i)
            else:
                informacoes[palpite[i]] = {'esta': True, 'posicao_nao': [i]}
        else:
            print(f'A letra {palpite[i]} não está na palavra')
            informacoes[palpite[i]] = {'esta': False}

    if palavra == palpite:
        print('Venceu')
    
def get_word_by_info(palavra):
    result = True
    for letra in informacoes:
        value = informacoes[letra]
        chaves = value.keys()

        #verificar letras que estão
        if value['esta']:
            # se a letra deve estar na palavra, mas não está, então não pode ser
            if letra not in palavra:
                result = False
            # se a posição da letra atual é conhecida e a letra na mesma posição na palavra é diferente, então não pode ser
            elif 'posicao' in chaves and letra != palavra[value['posicao']]:
                result = False
            # se a posição da letra atual coincide com algum indice da lista posicao não, então não pode ser
            elif 'posicao_nao' in chaves:
                for indice in value['posicao_nao']:
                    if letra == palavra[indice]:
                        result = False
        #verifica letras que não estão
        elif letra in palavra:
            result = False

    return result



def get_palpite():
    palavras = get_words()
    validas = list(filter(get_word_by_info, palavras))
    return random.choice(validas)

def preenche_info():
    nova_informacao = int(input("Quantos novos dados você conseguiu? "))
    for i in range(nova_informacao):
        letra = input("Informe a letra: ")
        dados = {'posicao_nao': []}
        if letra in informacoes.keys():
            dados = informacoes[letra]
        esta = input("A letra está na palavra? s/n") == 's'
        dados['esta'] = esta
        if esta:
            if input("Acertou a posição? s/n") == 's':
                dados['posicao'] = int(input("Informe a posição da letra: "))-1
            else:
                dados['posicao_nao'].append(int(input("Informe a posição em que a letra não está: "))-1)
        informacoes[letra] = dados


palavras = get_words()

# MODO auxílio
# informacoes = {}
# for i in range(6):
#     print(get_palpite())
#     preenche_info()

# MODO máquina contra máquina
# informacoes = {}
# palavra = get_termo()
# for i in range(6):
#     verificar_automatico(palavra, get_palpite(), informacoes)

# MODO máquina contra humano
# informacoes = {}
# while True:
#     palavra = input("Escolha uma palavra válida de 5 letras")
#     if palavra+'\n' in palavras:
#         break
# for i in range(6):
#     verificar_automatico(palavra, get_palpite(), informacoes)

# MODO humano contra máquina
# palavra = get_termo()
# for i in range(6):
#     while True:
#         palpite = str(input("Informe o palpite: "))
#         if palpite+'\n' in palavras:
#             break
#     verificar(palavra, palpite)
# print(palavra)