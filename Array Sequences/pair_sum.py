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
