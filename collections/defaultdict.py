from collections import defaultdict

# Dicionário com valor padrão igual ao inteiro zero.
# Caso seja acessado com uma chave que não existe a função `int` será chamada
# int() == 0
campos = defaultdict(int)

campo1 = {'boi' : 22, 'vaca': 37, 'porco': 10}
campo2 = {'cavalo': 11, 'porco': 4}

for chave, valor in campo1.items():
    campos[chave] += valor

for chave, valor in campo2.items():
    campos[chave] += valor

# campos = {'boi' : 22, 'vaca': 37, 'porco': 14, 'cavalo': 11}
print(campos)


from collections import defaultdict

# Dicionário com valor padrão igual ao inteiro zero.
# Caso seja acessado com uma chave que não existe a função `int` será chamada
# int() == 0
campos = defaultdict(int)

campo1 = {'boi' : 22, 'vaca': 37, 'porco': 10}
campo2 = {'cavalo': 11, 'porco': 4}

agregar(campos, campo1)
agregar(campos, campo2)

# campos = {'boi' : 22, 'vaca': 37, 'porco': 14, 'cavalo': 11}
print(campos)

def agregar(agregador: defaultdict[str, int], origem: dict[str, int]):
    """
    Agrega dicionários somando valores com chaves comuns.

    Incluir os pares chave e valor da origem no agregador.
    Para chaves comuns os valores são somados.

    Args:
        agregador (defaultdict[str, int]): dado final.
        origem (dict[str, int]): dado de origem a ser agregado.
    """

    for chave, valor in origem.items():
        agregador[chave] += valor
