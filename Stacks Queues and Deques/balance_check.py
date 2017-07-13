def balance_check(s):

  if len(s)%2 != 0:
    return False

  opening =  set('([{')

  matches = set([('(', ')'), ('[', ']'), ('{', '}')])

  stack = []

  for paren in s:
    if paren in opening:
        stack.append(paren)
    else:

      if len(stack) == 0: # there is no opening parenthese for
        return False    # this 'paren' close parenthese

      last_open = stack.pop()
      if (last_open, paren) not in matches:
        return False
  return len(stack) == 0
  # false if the opening parenthese never close

balance_check('[]') # True
balance_check('[](){([[[]]])}') # True
balance_check('()(){]}') # False
