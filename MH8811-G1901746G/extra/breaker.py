def shift_letter(l, n):
    new_l = ord(l) - n if ord(l) - n >= ord('a') else ord(l) - n + 26
    return chr(new_l)


def vigenere_decrypt(m, k):
    decrypt = ''
    for index, value in enumerate(m):
        if value.isalpha():
            bias = ord(k[index]) - ord('a')
            letter = shift_letter(value, bias)
        else:
            letter = value
        decrypt += letter
    return decrypt


def caesar_decrypt(m, k):
    decrypt = ''
    for char in m:
        if char.isalpha():
            letter = shift_letter(char, k)
        else:
            letter = char
        decrypt += letter
    return decrypt


def decipher(m):
    for key in ['blink', 'nose', 'rabbit', 'thunder', 'match', 'heavenly', 'stereotype', 'bake']:
        n = len(m)
        key2 = ''
        while n > 0:
            key2 += key[:n]
            n = len(m) - len(key2)
        msg = vigenere_decrypt(m, key2)
        if msg[:20] == 'root@hackernetwork$>':
            return True, msg[21:]
        for key_caesar in range(1, 26):
            msg_caesar = caesar_decrypt(msg, key_caesar)
            if msg_caesar[:20] == 'root@hackernetwork$>':
                return True, msg_caesar[21:]

    for key_caesar in range(1, 26):
        msg_caesar = caesar_decrypt(m, key_caesar)
        if msg_caesar[:20] == 'root@hackernetwork$>':
            return True, msg_caesar[21:]
        for key in ['blink', 'nose', 'rabbit', 'thunder', 'match', 'heavenly', 'stereotype', 'bake']:
            n = len(m)
            key2 = ''
            while n > 0:
                key2 += key[:n]
                n = len(m) - len(key2)
            msg = vigenere_decrypt(m, key2)
            if msg[:20] == 'root@hackernetwork$>':
                return True, msg[21:]
    return False, ''

if __name__ == '__main__':
    file = open('intercepted.txt', 'r')
    messages = file.readlines()
    for message in messages:
        print(decipher(message.strip()))
