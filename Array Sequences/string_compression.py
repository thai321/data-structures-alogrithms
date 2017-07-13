def compress(s): # my version
  if len(s) == 0:
    return ""
  current_letter = s[0]
  count = 1
  result = ""

  for letter in s[1:]:
    if current_letter == letter:
      count += 1
    else:
      result += current_letter + str(count)
      current_letter = letter
      count = 1

  result += current_letter + str(count)

  return result

#This solution compresses without checking. Known as the RunLength Compression algorithm.
def compress(s): # Time and space complexity of O(n)

  # Begin Run as empty string
  r = ""
  l = len(s)

  # Check for length 0
  if l == 0:
    return ""

  # Check for length 1
  if l == 1:
    return s + "1"

  #Intialize Values
  last = s[0]
  cnt = 1
  i = 1

  while i < l:

    # Check to see if it is the same letter
    if s[i] == s[i - 1]:
      # Add a count if same as previous
      cnt += 1
    else:
      # Otherwise store the previous data
      r = r + s[i - 1] + str(cnt)
      cnt = 1

    # Add to index count to terminate while loop
    i += 1

  # Put everything back into run
  r = r + s[i - 1] + str(cnt)

  return r

compress('AAAAABBBBCCCC') # 'A5B4C4'
compress('AAABCCDDDDD') # 'A3B1C2D5'
compress('AABBCC') # 'A2B2C2'
compress('abcdAAABBBAAA') # 'a1b1c1d1A3B3A3'
