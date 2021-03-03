def translate(msg):
    translated = ""
    for symbol in msg:
      if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = (num + key) % 26
        translated = translated + LETTERS[num]
    return translated


message = open('plain.txt', 'r').read()

key = 13

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = message.upper()

cipher = translate(message)

print(cipher)
open('cipher.txt', 'w').write(cipher)
