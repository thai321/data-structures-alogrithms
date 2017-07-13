# Graph

## Adjacency List implementation

## Word Ladder problem
- Transform the word "FOOL" into the word "SAGE".
- In a word ladder puzzle you must make the change occur gradualy by changing one letter at a time.
- At each step you must transform one word into another word, you are not allowed to transform a word into a non-word
>- `Example`:
  FOOL -> POOL -> POLL -> POLE -> PALE -> SALE -> SAGE

- `Solve` this problem using a graph algorithm.
  - Represent the relationships between the words as a graph
  - Use the graph algorithm known as breadth first search to find an efficient path from the starting word to the ending word.
- Figure out how to turn a large collection of words into a graph.
- What we would like is to have an edge from one word to another if the two words are only different by a single letter.
- Then any path from one word to another is a solution to the word ladder puzzle

- Suppose that we have a huge number of buckets, each of them with a four-letter word on the outside, except that one of the letters in the label has been replaced by an underscore.
- We can implement the scheme we have just described by using a dictionary.
- The labels on the buckets we have just described are the keys in our dictionary.
- The value stored for that key is a list of words.
- Once we have the dictionary built we can create the graph.
- We start our graph by creating a vertex for each word in the graph.
- Then we create edges between all the vertices we find for words found under the same key in the dictionary


## Breadth First Search (BFS)


## Knight's Tour Problem
