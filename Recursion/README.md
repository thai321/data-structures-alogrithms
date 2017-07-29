# Recursion

## Factorial
```py
def factorial(n):
  if n == 0 or n == 1: # Base case
    return 1
  return n * factorial(n-1)
```

## Recusive Sum

```py
def rec_sum(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return n + rec_sum(n-1)
rec_sum(4) # return 10
```

## Digits Sum

- Given an integer, create a function which returns the sum of all the
individual digits in that integer. For example: if n = 4321, return
4+3+2+1

```py
def sum_func(n):
  if n/10 == 0:
    return n
  return n%10 + sum_func(n/10)

sum_func(4321) # 4+3+2+1 should return 10
```


## Word Split

- Create a function called word_split() which takes in a string phrase
and a set list_of_words. The function will then determine if it is
possible to split the string in a way in which words can be made
from the list of words. You can assume the phrase will only contain
words found in the dictionary if it is completely splittable.


```py
def word_split(phrase,list_of_words, output = None):

  if output is None:
    output = []

  for word in list_of_words:

    if phrase.startswith(word):
      output.append(word)
      return word_split(phrase[len(word):], list_of_words, output) # save the result to output

  return output  # Case of yes
                  # the last frame of rescursion will return the out put since phrase == "",
                  # and "" is not in list_of_words
                  # case of no --> no match in list_of_words --> end of the loop --> return []

word_split('themanran',['the','ran','man'])
# ['the', 'man', 'ran']
```


## Memoization


```py
# Create cache for known results
factorial_memo = {}

def factorial(k):

  if k < 2:
    return 1

  if not k in factorial_memo:
    factorial_memo[k] = k * factorial(k-1)

  return factorial_memo[k]

factorial(4) # 24
```


```py
class Memoize:
  def __init__(self, f):
    self.f = f
    self.memo = {}
  def __call__(self, *args):
    if not args in self.memo:
      self.memo[args] = self.f(*args)
    return self.memo[args]

def factorial(k):

  if k < 2:
    return 1

  return k * factorial(k - 1)

factorial = Memoize(factorial)
factorial(10) # much faster 3628800
```


## Reverse a string

```py
def reverse(s):
  if len(s) <= 1:
    return s
  return reverse(s[1:]) + s[0]

class Memoize:
  def __init__(self, f):
    self.f = f
    self.memo = {}
  def __call__(self, *args):
    if not args in self.memo:
      self.memo[args] = self.f(*args)
    return self.memo[args]

rev = Memoize(reverse)
rev("hello world") # 'dlrow olleh'
```

## String Permutation


```py
def permute(s):
    out = []

  # Base Case
  if len(s) == 1:
      out = [s]

  else:
    # For every letter in string, with index i
    for i, let in enumerate(s):

      # For every permutation resulting from Step 2 and 3 described above
      for perm in permute(s[:i] + s[i+1:]):
#                 print i, let
          # Add it to output
        out += [let + perm]
#1st    # (abc) --> a + (bc) --> a + b + (c) and a + c + (b)
        # --> abc, acb
#2nd    # b + (ac) --> b + a + (c) and b + c + (a) --> bac, bca
#3nd    # c + (ab) --> c + a + (b) and c + b + (a) --> cab, cba
  return out
```

## Fibonnaci Sequence

```py
def fib_rec(n):
  if n == 0 or n == 1:
    return n
  return fib_rec(n-1) + fib_rec(n-2)
```

```py
# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
  if n == 0 or n == 1:
    return n

  if not n in cache:
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

  return cache[n]
```

```py
def fib_iter(n):
  a = 0
  b = 1
  for i in range(n):
    a, b = a + b, a
  return a
```


## Coin Change

- Problem Statement
  - Given a target amount n and a list (array) of distinct coin values,
what's the fewest coins needed to make the change amount.

- For example:

  - If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to
make change:

    - 1+1+1+1+1+1+1+1+1+1

    - 5 + 1+1+1+1+1

    - 5+5

    - 10

With 1 coin being the minimum amount.

Solution
Implement your solution below:
`rec_coin(10, [1,5]) # should return 2`

```py
def rec_coin(target,coins):  # iter
  '''
  INPUT: Target change amount and list of coin values
  OUTPUT: Minimum coins needed to make change

  Note, this solution is not optimized.
  '''

  # Default to target value
  min_coins = target

  # Check to see if we have a single coin match (BASE CASE)
  if target in coins:
    return 1

  else:

    # for every coin value that is <= than target
    for i in [c for c in coins if c <= target]:

      # Recursive Call (add a count coin and subtract from the target)
      num_coins = 1 + rec_coin(target-i,coins)

      # Reset Minimum if we have a new minimum
      if num_coins < min_coins:

        min_coins = num_coins

  return min_coins
```


```py
def rec_coin_dynam(target,coins,known_results): # dynamic solution
  '''
  INPUT: This funciton takes in a target amount and a list of possible coins to use.
  It also takes a third parameter, known_results, indicating previously calculated results.
  The known_results parameter shoud be started with [0] * (target+1)

  OUTPUT: Minimum number of coins needed to make the target.
  '''

  # Default output to target
  min_coins = target

  # Base Case
  if target in coins:
    known_results[target] = 1
    return 1

  # Return a known result if it happens to be greater than 1
  elif known_results[target] > 0:
    return known_results[target]

  else:
    # for every coin value that is <= than target
    for i in [c for c in coins if c <= target]:

      # Recursive call, note how we include the known results!
      num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)

      # Reset Minimum if we have a new minimum
      if num_coins < min_coins:
        min_coins = num_coins

        # Reset the known result
        known_results[target] = min_coins

  return min_coins

target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

rec_coin_dynam(target,coins,known_results)
# 8
```
