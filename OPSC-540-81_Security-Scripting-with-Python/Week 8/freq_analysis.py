ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher = open('cipher.txt', 'r').read()

def getLetterCount(message):
  alphabet = [chr(i+65) for i in range(26)]
  letter_count = dict((x,0) for x in alphabet)

  for letter in message.upper():
    if letter in LETTERS:
        letter_count[letter] += 1

  return letter_count

def getFreq(freqPair):
  return freqPair[0]

def getFrequencyOrder(message):
  letterToFreq = getLetterCount(message)

  freqToLetter = {}
  for letter in LETTERS:
      if letterToFreq[letter] not in freqToLetter:
          freqToLetter[letterToFreq[letter]] = [letter]
      else:
          freqToLetter[letterToFreq[letter]].append(letter)

  for freq in freqToLetter:
      freqToLetter[freq].sort(key=ETAOIN.find)
      freqToLetter[freq] = ''.join(freqToLetter[freq])

  print(freqToLetter)

  freqPairs = list(freqToLetter.items())
  freqPairs.sort(key=getFreq, reverse=True)

  freqOrder = []
  for freqPair in freqPairs:
      freqOrder.append(freqPair[1])

  return ''.join(freqOrder)

mostFrequentLetters = getFrequencyOrder(cipher)

plaintext = ""
for letter in cipher:
  i = mostFrequentLetters.find(letter)
  plaintext += ETAOIN[i]

print(plaintext)
open('freq_input.txt', 'w').write(plaintext)