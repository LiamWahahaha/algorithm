* time complexity(average case)[1]
|          |   list    |   queue    |    set    |   dict    |
|----------|:---------:|:----------:|:---------:|:---------:|
|Copy      |    O(n)   |    O(n)    |           |    O(n)   |
|Append    |    O(1)   |    O(1)    |           |           |
|Appendleft|           |    O(1)    |           |           |
|Pop(last) |    O(1)   |    O(1)    |           |           |
|Popleft   |           |    O(1)    |           |           |
|Pop(inter)|    O(k)   |            |           |           |
|Extend    |    O(k)   |    O(k)    |           |           |
|Extendleft|           |    O(k)    |           |           |
|rotate    |           |    O(k)    |           |           |
|remove    |           |    O(k)    |           |           |
|Insert    |    O(n)   |            |           |           |
|Get Item  |    O(1)   |            |           |    O(1)   |
|Set Item  |    O(1)   |            |           |    O(1)   |
|Delete    |    O(n)   |            |           |    O(1)   |
|Iteration |    O(n)   |            |           |    O(n)   |
|Get Slice |    O(k)   |            |           |           |
|Del Slice |    O(n)   |            |           |           |
|Set Slice |   O(k+n)  |            |           |           |
|Sort      | O(n log n)|            |           |           |
|Multiply  |   O(nk)   |            |           |           |
|x in s    |    O(n)   |            |    O(1)   |           |
|min(s)    |    O(n)   |            |           |           |
|max(s)    |    O(n)   |            |           |           |
|Get Length|    O(1)   |            |           |           |

* list, sets, dictionaries[2]

  * ***list:***

    * Internally, a list is represented as an array.

    * All of the methods of list objects are as follows:

      > * list.append(x)
      > * list.extend(iterable)
      > * list.insert(index, x)
      > * list.remove(x)
      > * list.pop() or list.pop([i])
      > * list.clear(), equivalent to del a[:]
      > * list.index(x[, start[, end]])
      > * list.count(x)
      > * list.sort(key=None, reverse=False)
      > * list.reverse()
      > * list.copy(), equivalent to a[:] (return a shallow copy of the list)

    * queue(collections.deque):

      * A deque (double-ended queue) is represented internally as a doubly linked list.

  * ***set:***

    * The implementation is intentionally very similar to dict.
    * Curly braces or the set() function can be used to create sets.
    * To create an empty set you have to use set(), not {}. ***The latter creates an empty dictionary.***

  * ***dict:***

    * There is a fast-path for dicts that (in practice) only deal with str keys.


Ref:
[1] https://wiki.python.org/moin/TimeComplexity
[2] https://docs.python.org/3/tutorial/datastructures.html
