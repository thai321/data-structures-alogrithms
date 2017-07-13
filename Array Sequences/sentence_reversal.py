def rev_word(s):
  if len(s) == 1:
    return s
  arr = s.split()
  result = []

  for i in range(len(arr)):
    result = [arr[i]] + result
  return ' '.join(result)

def rev_word(s):
  words = []
  length = len(s)
  space = [' ']

  i = 0

  while i < length:
    if s[i] not in space:
      word_start = i

      while i < length and s[i] not in space:
        i += 1
      words.append(s[word_start:i]) # get a word and append to words
    i += 1

  return final_output(words)  # return " ".join(reversed(words))

def final_output(words):
  arr = []

  for word in words:
    arr = [word] + arr

  return " ".join(arr)

rev_word('Hi John,   are you ready to go?') # 'go? to ready you are John, Hi'
rev_word('    space before') # 'before space'
rev_word('1') # '1'
