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
