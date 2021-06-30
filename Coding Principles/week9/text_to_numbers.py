def encode():
    print('This program converts a text message into a sequence '
          'of numbers representing the Unicode encoding of the message.\n')

    message = input('Enter the message to encode: ')

    for ch in message:
        print(ord(ch), end=' ')

    print()
    print()


def decode():
    print('This program converts a sequence of Unicode numbers '
          'into the string of text that it represents.\n')

    in_string = input('Enter the Unicode-encoded message: ')
    chars = []

    for num_str in in_string.split():
        chars.append(chr(int(num_str)))

    message = ''.join(chars)
    print('The decoded message is:', message)


encode()
decode()
