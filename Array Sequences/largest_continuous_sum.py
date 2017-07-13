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
