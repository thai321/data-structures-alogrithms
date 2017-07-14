## `Dynamic Array`

```python
import ctypes

class DynamicArray(object):

  def __init__(self):
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)

  def __len__(self):
    return self.n

  def __getitem__(self,k):
    if not 0 <= k < self.n:
        return IndexError('K is out of bounds!')
    return self.A[k]

  def append(self, ele):
    if self.n == self.capacity:
      self._resize(2*self.capacity) # 2x if capacity isn't enough
    self.A[self.n] = ele
    self.n += 1

  def _resize(self, new_cap):
    B = self.make_array(new_cap)

    for k in range(self.n):
      B[k] = self.A[k]

    self.A = B
    self.capacity = new_cap

  def make_array(self, new_cap):
    return (new_cap * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
len(arr) # 1
arr.append(2)
len(arr) # 2
arr[0] # 1
arr[1] # 2
```

## `Anagram Problem`

Given two strings, check to see if they are anagrams. <p>An anagram is when the two strings can be written using the exact same letters <p> (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

```python
def anagram(s1,s2):
  s1 = s1.replace(' ', '').lower()
  s2 = s2.replace(' ', '').lower()
  # return sorted(s1) == sorted(s2)

  #Edge Case Check
  if len(s1) != len(s2):
    return False

  count = {}

  for letter in s1:
    if letter in count:
      count[letter] += 1
    else:
      count[letter] = 1

  for letter in s2:
    if letter in count:
      count[letter] -=1
    else:
      count[letter] = 1

  for k in count:
    if count[k] != 0:
      return False

  return True

anagram("dog",'god') # True
anagram('clint eastwood','old west action') # True
anagram('aa','bb') # false
```


## `Array Pair Sum`
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 + (1,3)
 + (2,2)

```python
def pair_sum1(arr,k):
  h = {}
  count = 0
  for x in arr:
    if x in h:
      h[x] += 1
    else:
      h[x] = 1

  for i in h:
    target = k - i
    if target in h and h[i] > 0 and h[target] > 0:
      count += 1
      h[target] -= 1
      h[i] -= 1
  return count

def pair_sum2(arr,k):

  if len(arr) < 2:
    return

  #Sets for tracking
  seen = set()
  output = set()

  for num in arr:
    target = k - num

    if target not in seen:
      seen.add(num)  # this make thing unique , ex: [1,2,3,1], 3
    else:
      output.add( ((min(num,target)), max(num,target)) )
  #     return len(output)
  print '\n'.join(map(str,list(output)))

pair_sum2([1,2,3,1],3) # (1, 2)
pair_sum2([1,3,2,2],4)
"""
(1, 3)
(2, 2)
"""
```

## `Find the Missing Element`
Consider an array of non-negative integers.<p>A second array is formed by shuffling the elements of the first array and deleting a random element.

Given these two arrays, find which element is missing in the second array.
<p>Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
<p>Input:
<p>finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
<p>Output:
5 is the missing number

```python
def finder(arr1,arr2):
  h = {}

  for x in arr2:
    if x in h:
      h[x] += 1
    else:
      h[x] = 1

  for x in arr1:
    if (x in h) and (h[x] > 0):
      h[x] -= 1
    else:
      return x

def finder1(arr1,arr2): # O(nlog(n))

  arr1.sort()
  arr2.sort()

  for num1, num2 in zip(arr1,arr2):
    if num1 != num2:
      return num1
  return arr1[-1] # just return any element, won't get here


import collections
def finder2(arr1,arr2):
  d = collections.defaultdict(int)

  for num in arr2:
    d[num] += 1

  for num in arr1:
    if d[num] == 0:
      return num
    else:
      d[num] -= 1

def finder3(arr1, arr2):
  result = 0

  # Perform an XOR between the numbers in the arrays
  for num in arr1 + arr2:# [1,2,3]  + [2,5,6] = [1,2,3,2,5,6]
    result^= num   # it outputs true whenever the inputs differ
    print result

  return result

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
finder(arr1,arr2) # 5

arr1 = [5,5,7,7]
arr2 = [5,7,7]
finder(arr1,arr2) # 5

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
finder(arr1,arr2) # 5

arr1 = [9,8,7,6,5,4,3,2,1]
arr2 = [9,8,7,5,4,3,2,1]
finder(arr1,arr2) # 6
```

## `Largest Continuous Sum`
Given an array of integers (positive and negative)
<p>find the largest continuous sum.

```python
def large_cont_sum(arr):
  if len(arr) == 0:
    return 0

  max_sum = current_sum = arr[0]

  for num in arr[1:]:
    current_sum = max(current_sum + num, num) # [-10, 2, ..] , current_sum = 2
    max_sum = max(current_sum, max_sum)

  return max_sum

# Many times in an interview setting the question also requires
# you to report back the start and end points of the sum.
def large_cont_sum(arr):
  if len(arr) == 0:
    return 0

  start = end = 0
  max_sum = current_sum = arr[0]

  for i in range(1,len(arr)):
    current_sum += arr[i]

    if current_sum  < arr[i]:
      current_sum = arr[i]
      start = i

    if current_sum > max_sum:
      end = i
      max_sum = current_sum
  print "max_sum = " , max_sum
  print "start and end point: ", (start,end)

large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
"""
max_sum =  29
start and end point:  (0, 6)
"""

large_cont_sum([1,2,-1,3,4,-1])
"""
max_sum =  9
start and end point:  (0, 4)
"""

large_cont_sum([-1,1])
"""
max_sum =  1
start and end point:  (1, 1)
"""
```

## `Sentence Reversal`
Given a string of word, rverse all the words.For ex:
<p>Given: 'This is the best'
will return: 'best the is this'
<p>Given ' space here' and 'space here ' both become: 'here space'

```python
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
```

## `String compression`
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
<p>For this problem, you can falsely "compress" strings of single or double letters.
<p>For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
<p>The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

```python
def compress(s):
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
```

## `Unique Characters in string`
Given a string,determine if it is compreised of all unique characters.
<p>For example, the string 'abcde' has all unique characters and should return True.
<p>The string 'aabcde' contains duplicate characters and should return false.

````python
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
```
