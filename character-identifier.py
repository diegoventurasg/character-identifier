def get_character_name(character):
    map = {
        ' ': 'espaço',
        '!': 'exclamação',
        '"': 'aspas duplas',
        '#': 'jogo da velha',
        '$': 'cifrão',
        '%': 'porcentagem',
        '&': 'e comercial',
        "'": 'aspas simples',
        '(': 'abre parênteses',
        ')': 'fecha parênteses',
        '*': 'asterisco',
        '+': 'mais',
        ',': 'vírgula',
        '-': 'hífen',
        '.': 'ponto',
        '/': 'barra',
        ':': 'dois pontos',
        ';': 'ponto e vírgula',
        '<': 'menor que',
        '=': 'igual',
        '>': 'maior que',
        '?': 'interrogação',
        '@': 'arroba',
        '[': 'abre colchetes',
        '\\': 'barra invertida',
        ']': 'fecha colchetes',
        '^': 'acento circunflexo',
        '_': 'sublinhado',
        '`': 'acento grave',
        '{': 'abre chaves',
        '|': 'barra vertical',
        '}': 'fecha chaves',
        '~': 'til'
    }
    return map.get(character, "CARACTERE DESCONHECIDO")


def identify_characters(text: str):
    detalhes_caracteres = []
    
    for character in text:
        if character.isalpha():
            if character.islower():
                detalhes_caracteres.append((character, 'minúscula'))
            elif character.isupper():
                detalhes_caracteres.append((character, 'maiúscula'))
        elif character.isnumeric():
            detalhes_caracteres.append((character, 'número'))
        else:
            nome_caractere = get_character_name(character)
            detalhes_caracteres.append((character, nome_caractere))
            
    return detalhes_caracteres

while True:
    string_usuario = input("Digite uma string: ")
    result = identify_characters(string_usuario)

    for character, detail in result:
        print(f"'{character}': {detail}")