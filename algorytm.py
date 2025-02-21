
def generate_autokey(key, text):
    return (key + text)[:len(text)]


def create_vigenere_table():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    size = len(alphabet)
    table = {}
    for i in range(size):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        table[alphabet[i]] = {alphabet[j]: shifted_alphabet[j]
                              for j in range(size)}
    return table


def encrypt_vigenere(text, key):
    table = create_vigenere_table()
    keyToCrypt = ""

    for i in range(0, len(key)):
        if ('а' <= key[i] <= 'я' or key[i]=='ё'):
            keyToCrypt += key[i]
    if(len(text)<len(keyToCrypt)):
        raise ValueError("Длина strToCrypt должна быть не меньше длины keyToCrypt")
    key = generate_autokey(key, text)
    encrypted_text = ""

    for t, k in zip(text, key):
        if t in table and k in table:
            encrypted_text += table[k][t]
        else:
            encrypted_text += t  

    return encrypted_text


def decrypt_vigenere(encrypted_text, key):
    table = create_vigenere_table()
    original_text = ""

    for i in range(len(encrypted_text)):
        k = key[i]
        if k in table:
            row = table[k]
            for original_char, encrypted_char in row.items():
                if encrypted_char == encrypted_text[i]:
                    original_text += original_char
                    key += original_char 
                    break
        else:
            original_text += encrypted_text[i]

    return original_text


def encryptFileContentVigenere(key: str, text: str):
    print(text)
    text = text.lower()
    strToCrypt = ""

    for i in range(0, len(text)):
        if ('а' <= text[i] <= 'я' or text[i]=='ё'):
            strToCrypt += text[i]
    key = key.lower()
    keyToCrypt=""


    for i in range(0,len(key)):
        if ('а' <= key[i] <= 'я' or key[i]=='ё'):
            keyToCrypt += key[i]
    
    print(strToCrypt)
    print(keyToCrypt)
    encrypted = encrypt_vigenere(strToCrypt, keyToCrypt)
    return encrypted


def decryptFileContentVigenere(key: str, text: str):
    text = text.lower()
    strToCrypt = ""
    for i in range(0, len(text)):
        if ('а' <= text[i] <= 'я' or text[i]=='ё'):
            strToCrypt += text[i]
    key = key.lower()
    keyToCrypt=""

    for i in range(len(key)):
        if ('а' <= key[i] <= 'я' or key[i]=='ё'):
            keyToCrypt += key[i]
    if(len(strToCrypt)<len(keyToCrypt)):
        raise ValueError("Длина strToCrypt должна быть не меньше длины keyToCrypt")
    decrypted = decrypt_vigenere(strToCrypt, keyToCrypt)
    return decrypted


def sortMatrix(matrix, key):
    key = list(key)
    n = len(key)

    sorted_key_indices = sorted(range(n), key=lambda x: key[x])

    sorted_matrix = []
    for row in matrix:
        sorted_matrix.append([row[i] for i in sorted_key_indices])

    return sorted_matrix


def bubbleSortColumns(matrix):
    num_columns = len(matrix[0])
    num_rows = len(matrix)

    for j in range(num_columns):
        for i in range(num_columns - 1):

            if matrix[0][i] > matrix[0][i + 1]:

                for row in matrix:
                    row[i], row[i + 1] = row[i + 1], row[i]

    return matrix


def decryptFileContentColumn(key: str, content: str):
    

    content = content.lower()
    key=key.lower()
    strToCrypt = ""
    keyToCrypt=""

    for i in range(len(key)):
        if ('а' <= key[i] <= 'я' or key[i]=='ё'):
            keyToCrypt += key[i]
    num_columns = len(keyToCrypt)
    for i in range(len(content)):
        if ('а' <= content[i] <= 'я' or content[i]=='ё'):
            strToCrypt += content[i]
    if(len(strToCrypt)<len(keyToCrypt)):
        raise ValueError("Длина strToCrypt должна быть не меньше длины keyToCrypt")
    num_rows = len(strToCrypt) // num_columns
    if len(strToCrypt) % num_columns > 0:
        num_rows += 1
    num_rows += 1

    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    for j in range(0, num_columns):
        matrix[0][j] = j
    if(len(strToCrypt) % num_columns>0):
        for j in range(len(strToCrypt) % num_columns, num_columns):
            matrix[num_rows-1][j] = ' '

    matrix = sortMatrix(matrix, keyToCrypt)

    k = 0
    for j in range(num_columns):
        for i in range(1, num_rows):
            if matrix[i][j] == '':
                matrix[i][j] = strToCrypt[k]
                k += 1
    print(matrix)

    matrix = bubbleSortColumns(matrix)
    print(matrix)

    decryptedStr = ""
    for i in range(1, num_rows):
        for j in range(num_columns):
            if matrix[i][j] != ' ' and isinstance(matrix[i][j], str):
                decryptedStr += matrix[i][j]

    return decryptedStr


def encryptFileContentColumn(key: str, content: str):
    
    content = content.lower()
    key=key.lower()
    strToCrypt = ""
    keyToCrypt = ""

    for i in range(0, len(key)):
        if ('а' <= key[i] <= 'я' or key[i]=='ё'):
            keyToCrypt += key[i]
    print(keyToCrypt)
    num_columns = len(keyToCrypt)

    for i in range(0, len(content)):
        if ('а' <= content[i] <= 'я' or content[i]=='ё'):
            strToCrypt += content[i]
    num_rows = len(strToCrypt)//num_columns
    if (len(strToCrypt) % num_columns > 0):
        num_rows += 1
    print(strToCrypt)
    if(len(strToCrypt)<len(keyToCrypt)):
        raise ValueError("Длина strToCrypt должна быть не меньше длины keyToCrypt")
    matrix = [[''for _ in range(num_columns)]for _ in range(num_rows)]
    k = 0
    for i in range(0, num_rows):
        for j in range(0, num_columns):
            if (k < len(strToCrypt)):
                matrix[i][j] = strToCrypt[k]
                k += 1
    matrix = sortMatrix(matrix, keyToCrypt)
    encryptedStr = ""
    for j in range(0, num_columns):
        for i in range(0, num_rows):
            encryptedStr += matrix[i][j]
    return encryptedStr
