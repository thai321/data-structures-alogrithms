# Search and Sorting

## Sequntial Search Analysis

```txt
_ Unordered List Analysis

Case                Best Case          Worst Case       Average Case
item is present        1                   n                n/2
item is not present    n                   n                n
```

```txt
_ Ordered List Analysis

Case                Best Case          Worst Case       Average Case
item is present        1                   n                n/2
item is not present    1                   n                n/2
```

```py
def seq_search(arr, ele):  # not order, unordered

  pos = 0
  found = False

  while pos < len(arr) and not found:

    if arr[pos] == ele:
      found = True

    else:
      pos += 1

  return found

arr = [1,2,3,4,5]
seq_search(arr,6) # False
```

```py
def ordered_seq_search(arr, ele):
  pos = 0
  found = False
  stopped = False

  while pos < len(arr) and not found and not stopped:

    if arr[pos] == ele:
      found = True
    elif arr[pos] > ele:
      stopped = True
    else:
      pos += 1
  return found # True
```


## Binary Search

- Binary search uses Divide and Conquer!
- We divide the problem into smaller pieces,
solve the smaller pieces in some way, and then reassemble the
whole problem to get the result.

```txt
Binary Search Analysis

Comparisions           Approximate Number of Items Left
    1                      n/2
    2                      n/4
    3                      n/8
    ...

    i                      n/ (n^i)/
```

```py
def binary_search(arr, ele):

  first = 0
  last = len(arr) - 1

  found = False

  while first <= last and not found:

    mid = (first + last)/2

    if arr[mid] == ele:
      found = True
    else:
      if ele < arr[mid]:
        last = mid - 1
      else:
        first = mid + 1

  return found

arr = [1,2,3,4,5,6,7,8,9,10]
binary_search(arr, 7) # True
```


```py
def rec_bin_search(arr, ele):

  if len(arr) == 0:
    return False
  else:

    mid = len(arr)/2

    if arr[mid] == ele:
      return True
    else:
      if ele < arr[mid]:
        return rec_bin_search(arr[:mid],ele)
      else:
        return rec_bin_search(arr[mid + 1:],ele)

arr = [1,2,3,4,5,6,7,8,9,10]
rec_bin_search(arr, 13) # False
```


## Hashing

 - The idea of a dictionary used as a hash table to get and retrieve
items using keys is often referred to as a mapping. In our
implementation we will have the following methods:
    - HashTable(): Create a new, empty map. It returns an empty
    map collection.
    - put(key,val): Add a new key-value pair to the map. If the key
    is already in the map then replace the old value with the new
    value.
    - get(key): Given a key, return the value stored in the map or
    None otherwise.
    - del: Delete the key-value pair from the map using a statement
    of the form del map[key]
    - len(): Return the number of key-value pairs stored
    - in : the map in Return True for a statement of the form
    "key in map", if the given key is in the map, False otherwise.

```py
class HashTable(object):

  def __init__(self,size):
    self.size = size
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def put(self, key, data):
    hashvalue = self.hashfunction(key, len(self.slots))

    if self.slots[hashvalue] == None: # new bucket --> update key, and data
      self.slots[hashvalue] = key
      self.data[hashvalue] = data

    else:
      if self.slots[hashvalue] == key: # found a bucket that has same key, update date only
        self.data[hashvalue] = data
      else: # rehash, current hashvalue doesn't have the same key
        nextslot = self.rehash(hashvalue,len(self.slots))
          #  while can't find an empty bucket and the slot which doesn't have the same key
        while self.slots[nextslot] != None and self.slots[nextslot] != key:
          nextslot = self.rehash(nextslot, len(self.slots))

          if self.slots[nextslot] == None: # found a new bucket, update key, and data
            self.slots[nextslot] = key
            self.data[nextslot] = data
          else:
            self.data[nextslot] = data # found a bucket that has same key, update date only

  def hashfunction(self, key, size):
    # the actual has function
    return key%size

  def rehash(self,oldhash,size):
    return (oldhash+1)%size

  def get(self, key):

    startslot = self.hashfunction(key, len(self.slots))
    data = None
    stop = False
    found = False
    position = startslot


    while self.slots[position] != None and not found and not stop:

      if self.slots[position] == key:
        found = True
        data = self.data[position]
      else:
        position = self.rehash(position,len(self.slots))

        if position == startslot:
          stop = True

    return data

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self,key, data):
    self.put(key,data)

h = HashTable(5)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'

h[1] # 'one'
h[2] # 'two'
h[3] # 'three'
```


# Sorting

```py
def bubble_sort(arr):
  for n in range(len(arr) - 1, 0 , -1): # decreasing --> step is -1
    for k in range(n): # 0 to n exclusive (0 .. n-1)
      if arr[k] > arr[k+1]:
        arr[k], arr[k+1] = arr[k+1], arr[k]

arr = [5,3,7,2]
bubble_sort(arr)
arr # [2, 3, 5, 7]
```

# Selection Sort

```py
def selection_sort(arr):          # from len(arr)-1 to 1, (len(arr)-1) .. 1
  for fillslot in range (len(arr)-1, 0, -1): # decreasing --> step is -1
    positionOfMax = 0
    for location in range(1, fillslot + 1):

      if arr[location] > arr[positionOfMax]:
        positionOfMax = location

    arr[fillslot], arr[positionOfMax] = arr[positionOfMax], arr[fillslot]

arr = [5,8,3,10,1]
selection_sort(arr)
arr # [1, 3, 5, 8, 10]
```


```py
for n in range(5,-1, -1):
  print "this is n: ", n
  for i in range (1, n+1):
    print "this is i = ", i

"""
this is n:  5
this is i =  1
this is i =  2
this is i =  3
this is i =  4
this is i =  5

this is n:  4
this is i =  1
this is i =  2
this is i =  3
this is i =  4

this is n:  3
this is i =  1
this is i =  2
this is i =  3

this is n:  2
this is i =  1
this is i =  2

this is n:  1
this is i =  1

this is n:  0
"""
```


## Insertion Sort

- The insertion sort always maintains a sorted sublist in the lower
positions of the list.

- Each new item is then "inserted" back into the previous sublist
such that the sorted sublist is one item larger.

- We begin by assuming that a list with one item (position 0) is
already sorted.
- On each pass, one for each item 1 through n - 1, the current item
is checked against those in the already sorted sublist.
- As we look back into the already sorted sublist, we shift those
items that are greater to the right.
- When we reach a smaller item or the end of the sublist, the
current item can be inserted

```py
def insertion_sort(arr): # O(n^2)

  for i in range(1,len(arr)):

    currentvalue = arr[i]
    position = i

    while (position > 0) and (arr[position-1] > currentvalue):
      arr[position] = arr[position - 1]
      position = position - 1

    arr[position] = currentvalue

arr = [5,8,3,10,1]
insertion_sort(arr)
arr  # [1, 3, 5, 8, 10]

```

## Shell Sort

-  The shell sort improves on the insertion sort by breaking the
original list into a number os smaller sublists,
- The unique way that these sublists are chosen is the key to the
shell sort.

- Instead of breaking the list into sublists of contiguous items,
the shell sort uses an increment "i" to create a sublist by choosing
all items that are "i" items apart.

- The shell sort improves on the insertion sort by breaking the
original list into a number of smaller sublists, each of which is
sorted using an insertion sort. The unique way that these sublists
are chosen is the key to the shell sort. Instead of breaking the
list into sublists of contiguous items, the shell sort uses an
increment i, sometimes called the gap, to create a sublist by
choosing all items that are i items apart.


```py
def shell_sort(arr):
  sublistcount = len(arr)/2

  # While we still have sub lists
  while sublistcount > 0:
    for start in range(sublistcount):
      # Use a gap insertion
      gap_insertion_sort(arr,start,sublistcount)

    print 'After increments of size: ', sublistcount
    print 'The list is ', arr


    sublistcount = sublistcount / 2


def gap_insertion_sort(arr,start,gap):
  for i in range(start+gap,len(arr),gap):
    currentvalue = arr[i]
    position = i

    print 'position = ', position
    print 'gap = ', gap
    print 'currentvalue = ', currentvalue

    # Using the Gap
    while position >= gap and arr[position-gap] > currentvalue:
      arr[position]=arr[position-gap]
      position = position-gap

    # Set current value
    arr[position]=currentvalue

arr = [45,67,23,45,21,24,7,2,6,4,90] ## length is 11
arr # [45, 67, 23, 45, 21, 24, 7, 2, 6, 4, 90]

shell_sort(arr)
arr

"""
position =  5
gap =  5
currentvalue =  24
position =  10
gap =  5
currentvalue =  90
position =  6
gap =  5
currentvalue =  7
position =  7
gap =  5
currentvalue =  2
position =  8
gap =  5
currentvalue =  6
position =  9
gap =  5
currentvalue =  4
After increments of size:  5
The list is  [24, 7, 2, 6, 4, 45, 67, 23, 45, 21, 90]
position =  2
gap =  2
currentvalue =  2
position =  4
gap =  2
currentvalue =  4
position =  6
gap =  2
currentvalue =  67
position =  8
gap =  2
currentvalue =  45
position =  10
gap =  2
currentvalue =  90
position =  3
gap =  2
currentvalue =  6
position =  5
gap =  2
currentvalue =  45
position =  7
gap =  2
currentvalue =  23
position =  9
gap =  2
currentvalue =  21
After increments of size:  2
The list is  [2, 6, 4, 7, 24, 21, 45, 23, 67, 45, 90]
position =  1
gap =  1
currentvalue =  6
position =  2
gap =  1
currentvalue =  4
position =  3
gap =  1
currentvalue =  7
position =  4
gap =  1
currentvalue =  24
position =  5
gap =  1
currentvalue =  21
position =  6
gap =  1
currentvalue =  45
position =  7
gap =  1
currentvalue =  23
position =  8
gap =  1
currentvalue =  67
position =  9
gap =  1
currentvalue =  45
position =  10
gap =  1
currentvalue =  90
After increments of size:  1
The list is  [2, 4, 6, 7, 21, 23, 24, 45, 45, 67, 90]
"""
```

## Merge Sort
- Merge sort is a recursive algorithm that continually splits a
list in half.
- If the list is empty or has one item, it is sorted by definition
(the base case).
- If the list has more than one item, we split the list and
recursively invoke a merge sort on both halves.


```py
def merge_sort(arr):

  if len(arr) > 1:

    mid = len(arr)/2
    lefthalf = arr[0:mid]
    righthalf = arr[mid:]

    merge_sort(lefthalf)
    merge_sort(righthalf)

    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):

      if lefthalf[i] < righthalf[j]:
        arr[k] = lefthalf[i]  # update to original arr

        i += 1
      else:
        arr[k] = righthalf[j] # update to original arr
        j += 1

      k += 1

    while i < len(lefthalf): #update the remainding to arr
      arr[k] = lefthalf[i]
      i += 1
      k += 1

    while j < len(righthalf):  #update the remainding to arr
      arr[k] = righthalf[j]
      j += 1
      k += 1
  print 'Merging ', arr
"""
Merging  [11]
Merging  [2]
Merging  [2, 11]
Merging  [5]
Merging  [4]
Merging  [4, 5]
Merging  [2, 4, 5, 11]
Merging  [7]
Merging  [6]
Merging  [6, 7]
Merging  [5]
Merging  [1]
Merging  [23]
Merging  [1, 23]
Merging  [1, 5, 23]
Merging  [1, 5, 6, 7, 23]
Merging  [1, 2, 4, 5, 5, 6, 7, 11, 23]
"""
```

## Quick sort

- The quick sort uses divide and conquer to gain the same
advantages as the merge sort, while not using additional storage.
- As a trade-off, however, it is possible that the list may
not be divided in half.
- When this happens, we will see that performance is diminished.
- A quick sor first selects a value, which is called the pivot
value.
- The role of the pivot value is to assist with splitting the list.
- The actual position where the pivot value belongs in the final
sorted list, commonly called the split point, will be used to
divide the list for subsequent calls to the quick sort.

```py
def quick_sort(arr):

  quick_sort_help(arr, 0 , len(arr) - 1)


def quick_sort_help(arr, first, last):

  if first < last:
    splitpoint = partition(arr, first, last)

    quick_sort_help(arr, first, splitpoint - 1)
    quick_sort_help(arr, splitpoint + 1, last)

def partition(arr, first, last):

  pivotvalue = arr[first]

  leftmark = first + 1
  rightmark = last

  done = False

  while not done:

    while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
      leftmark += 1

    while arr[rightmark] > pivotvalue and rightmark >= leftmark:
      rightmark -= 1

    if rightmark < leftmark:# it's over when leftmark and right mark cross
      done = True

    else:   # swap because arr[leftmark] > arr[rightmark]
      temp = arr[leftmark]
      arr[leftmark] = arr[rightmark]
      arr[rightmark] = temp

  temp = arr[first]   # swap because the pivotvalue is between
  arr[first] = arr[rightmark]
  arr[rightmark] = temp

  return rightmark

arr = [2,5,4,6,7,3,1,4,12,11]
quick_sort(arr)
arr # [1, 2, 3, 4, 4, 5, 6, 7, 11, 12]
```
