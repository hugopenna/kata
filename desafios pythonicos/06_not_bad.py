"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""
# A função not_bad remove o trecho entre not e bad através do split da string 's' em strings menores
# onde not e bad são removidos e a string desejada é concatenada novamente.
# Como a função split retorna uma lista de strings, é feita a verificação se 'bad' aparece na string que esta na
# segunda posição da lista list1[1]. O que valida que temos 'bad' depois de not.
#  list2 retorna o split('bad') da string que contém bad, onde a primeira string é o conteúdo entre not e bad,
# que é descartado e a segunda sting da lista é o conteúdo após bad e que precisa ser adicionado depois de 'good'.

def not_bad(s):
    list1 = s.split("not")
    if "bad" in list1[1]:
        list2 = list1[1].split("bad")
        s = list1[0] + "good" + list2[1]
    return s

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
