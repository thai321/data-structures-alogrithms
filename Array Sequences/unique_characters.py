def uni_char1(s): # O(n)
  if s == "":
    return True

  uniq = {}

  for ch in s:
    if ch in uniq:
      return False
    else:
      uniq[ch] = 1

  return True

def uni_char2(s):
  return len(set(s)) == len(s)

def uni_char3(s):

  chars = set()
  for let in s:
    if let in chars:
      return False
    else:
      chars.add(let)

  return True

"""
uni_char('') # True
uni_char('goo') # False
uni_char('abcdefg') # True
"""
