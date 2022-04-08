import string


def encode_lower(message):
    """
        Função codificadora para servir de parâmetro.
    """
    encoded = ''
    for l in message:
        if l in string.ascii_lowercase:
            ascii_n = ord(l) + 15
            if ascii_n >= 123:
                ascii_n -= 26
            encoded += chr(ascii_n)
        else:
            encoded += l
    return encoded


def encode_upper(message):
    """
        Função codificadora para servir de parâmetro.
    """
    encoded = ''
    for l in message:
        if l in string.ascii_uppercase:
            ascii_n = ord(l) + 9
            if ascii_n >= 91:
                ascii_n -= 26
            encoded += chr(ascii_n)
        else:
            encoded += l
    return encoded


def encode_int(message):
    """
        Função codificadora para servir de parâmetro.
    """
    encoded = ''
    for l in message:
        if ord(l) in range(48, 58):
            ascii_n = ord(l) + 4
            if ascii_n >= 58:
                ascii_n -= 10
            encoded += chr(ascii_n)
        else:
            encoded += l
    return encoded


def encoder_decorator(func):
    """
        Decorador para avisar que as mensagens estão codificadas.
    """
    def wrapper(*arguments, dictionary):
        new_messages = []
        encoded_texts = func(*arguments, dictionary=dictionary)
        warning = 'This message is encoded. Can you understand?\n'
        for text in encoded_texts:
            new_text = warning + text + '\n' + '-' * 70
            new_messages.append(new_text)
        return new_messages
    return wrapper


@encoder_decorator
def encode_texts(*arguments, dictionary):
    """
        Função com lista de argumentos e dicionário
        de chaves como parâmetros.
        Serve para codificar as entradas de acordo com o
        "dictionary" usando as funções fornecidas em "arguments".
    """
    encoded_texts = []
    for func in arguments:
        input_message = dictionary[func.__name__]
        encoded_text = func(input_message)
        encoded_texts.append(encoded_text)

    return encoded_texts


def run():
    """
        Roda teste do decorador.
    """
    dic = {
        'encode_lower': 'How are YOU doing?',
        'encode_upper': 'Hi! I\'M DOING FINE. CAN I HAVE YA NUM?',
        'encode_int': 'Yes: 5587966557642'
    }

    texts = encode_texts(encode_lower, encode_upper, encode_int, dictionary=dic)

    for text in texts:
        print(text)


if __name__ == '__main__':
    run()