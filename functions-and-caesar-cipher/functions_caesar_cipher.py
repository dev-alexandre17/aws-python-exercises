# Função para concatenar o alfabeto duas vezes

def getDoubleAlphabet(alphabet):
    return alphabet + alphabet

# Recebdno a mensagem do usuário

def getMessage():
    message = str(input(f'Digite sua mensagem: '))
    return message

# Criando a chave de criptografia

def getCipherKey():
    key = int(input(f'Digite a chave de criptografia [1-25]: '))
    if key < 1 or key > 25:
        print(f'Chave inválida! Digite um número entre 1 e 25.')
        return getCipherKey()
    else:
        return key

# Criptografando a mensagem com a cifra de César

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    message = message.upper()
    alphabet = alphabet.upper()
    doubleAlphabet = getDoubleAlphabet(alphabet)
    for letter in message:
        if letter in alphabet:
            index = alphabet.find(letter)
            newIndex = index + cipherKey
            encryptedLetter = doubleAlphabet[newIndex]
            encryptedMessage += encryptedLetter
        else:
            encryptedMessage += letter
    return encryptedMessage

# Descriptografando a mensagem com a cifra de César

def decryptMessage(message, cipherKey, alphabet):
    cipherKey = -cipherKey
    decryptedMessage = encryptMessage(message, cipherKey, alphabet)
    return decryptedMessage

# Programa principal da cifra de César

def runCaesarCipherProgram():
    print(f'Programa Principal da Cifra de César\n')
    
    englishAlhabet = "abcdefghijklmnopqrstuvwxyz"
    print(f'Alfabeto englês: {englishAlhabet}')
    print(f'Alfabeto duplicado: {getDoubleAlphabet(englishAlhabet)}\n')
    
    userMessage = getMessage()
    print(f'Mensagem informada pelo usuário: {userMessage}\n')
    
    userCipherKey = getCipherKey()
    print(f'Chave de criptografia informada pelo usuário: {userCipherKey}\n')
    
    userEncryptedMessage = encryptMessage(userMessage, userCipherKey, englishAlhabet)
    print(f'Mensagem criptografada: {userEncryptedMessage}\n')

    userDecryptedMessage = decryptMessage(userEncryptedMessage, userCipherKey, englishAlhabet)
    print(f'Mensagem descriptografada: {userDecryptedMessage}')

runCaesarCipherProgram()