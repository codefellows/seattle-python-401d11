# Trees

There are two different types of trees that this tutorial will review:
1. Binary Trees
2. Binary Search Trees

We will review some common terminology that is shared amoungst all of the trees
and then dive into specifics of the different types.

### Common Terminology

1. *Node* - a node is the individual item/data that make up the data structure.
1. *Root* - The root is the first/top `Node` in a tree
3. *Left Child* - The node that is positioned to the left of the root
3. *Right Child* - The node that is positioned to the right of the root
1. *Edge* - The edge in a tree is the link between two nodes
1. *Leaf* - A leaf is the node that does not contain either a left child or a right child node.
1. *Height* - The height of a tree is determined by the number of edges from the root to the bottommost node.
This is what a tree looks like:

![DepthFirst Traversal](assets/BinaryTree1.PNG){:target="_blank"}



### Traversals

There are two categories of traversals when it comes to trees.
1. Depth First
2. Breadth First


#### Depth First
Depth first is a traversal that traverses the depth (height) of the tree.

The different traversals determine at which point the `Root` is looked at.
Here are the three different depth first traversals broken down:


1. Preorder
   - Root, Left, Right
2. Inorder
   - Left, Root, Right
3. Postorder
   - Left, Right, Root


![DepthFirst Traversal](assets/depthTraversal.PNG){:target="_blank"}


Output:

- ***Preorder:*** A, B, D, E, C, F
- ***Inorder:*** D, B, E, A, F, C
- ***Postorder:*** D, E, B, F, C, A




The most common way to traverse through a tree is to use recursion.
With these traversals, we rely on the callstack to navigate back up
the tree when we have reached the end.

Let's breakdown the `PreOrder` traversal.

Here is the code for a PreOrder traversal:

```python
def pre_order(self, node, operation):
    # Do your thing here... generally pass a lambda or named function
    operation(node)

    if node.left_child is not None:
        pre_order(node.left_child)
    if node.right_child is not None:
        pre_order(node.right_child)
```

1. PreOrder means that the `root` has to be looked at first.
The first thing we do is look at the root....in our case, we will just ouput that
to the console. When we call `PreOrder` for the first time, the `root`, NodeA, will be added to the callstack.

![PreOrder1](assets/DepthTraversal1.PNG){:target="_blank"}

2. Next we start reading the code from top to bottom. The first line of code reads this:

```python
    # ...
    operation(node)
    # ...
```

This means that we will output the `root.value` out to the console.

3. Next, the code above is instructing us to check if our `root` has a `left_child`.
If the root does, we will then send the `left_child` to our PreOrder method recursively.
`NodeB` is now our new root node, and after this call, `NodeB` is pushed onto the callstack.

![PreOrder1](assets/DepthTraversal2.PNG){:target="_blank"}


4. This process continues until we reach a `Leaf`. When we do hit a leaf, this is the state of our tree:

![PreOrder1](assets/DepthTraversal3.PNG){:target="_blank"}

It's important to note a few things that are about to happen.
  - The value of the node will output to the console.
  - The program will look for both a `node.left_child` and a `node.right_child`. Both will come be false, so it will end the execution of that method call.
  - `nodeD` wil pop off of the callstack and the root will be reassigned back to `NodeB`.


![PreOrder1](assets/DepthTraversal4.PNG){:target="_blank"}

5. The Code block will now pick up where it left off when we were in the `NodeB` frame.
Since it already looked for `node.left_child`, it will now look for `node.right_child`.

![PreOrder1](assets/DepthTraversal5.PNG){:target="_blank"}

6. `NodeE` will output to the console. Since `NodeE` is a leaf, it will complete the method code
block, and pop `NodeE` off of the call stack and makes it's way back up to `NodeB`.
![PreOrder1](assets/DepthTraversal6.PNG){:target="_blank"}

7. In the call frame, `NodeB` has already checked for `node.left_child`, and `node.right_child`,
the code block will complete and pop off `NodeB` from the callstack, and leave `NodeA` as the root.
![PreOrder1](assets/DepthTraversal7.PNG){:target="_blank"}

8. Following the same pattern as we did with the other nodes, `NodeA`'s callstack frame will pick up where it left off, and check out `Node.right_child`.
`NodeC` will be added to the callstack frame, and it will now be reassigned as the new root.

![PreOrder1](assets/DepthTraversal8.PNG){:target="_blank"}

9. `NodeC` will be outputted to the console, and `node.left_child` will be evaluated, and `PreOrder()` will be called sending `node.left_child` as it's root.

![PreOrder1](assets/DepthTraversal9.PNG){:target="_blank"}

10. At this point, the program will find taht `NodeF` does not have any children and it will make it's way back up the call stack up to `NodeC`.

![PreOrder1](assets/DepthTraversal10.PNG){:target="_blank"}


11. NodeC does not have a `node.right_child`, so it will pop off the callstack and return to Node A.

![PreOrder1](assets/DepthTraversal11.PNG){:target="_blank"}


12. Congratulations! Your PreOrder traversal is completed!



Here is the code for all 3 of the depth first traversals.

```python
def pre_order(self, node=None, operation=lambda node: print(node)):
    # Do your thing here... generally pass a lambda or named function
    operation(node)

    if node.left_child is not None:
        pre_order(node.left_child)
    if node.right_child is not None:
        pre_order(node.right_child)
```
```python
def post_order(self, node=None, operation=lambda node: print(node)):
    if node.left_child is not None:
        pre_order(node.left_child)
    if node.right_child is not None:
        pre_order(node.right_child)

    # Do your thing here... generally pass a lambda or named function
    operation(node)
```
```python
def in_order(self, node=None, operation=lambda node: print(node)):
    if node.left_child is not None:
        pre_order(node.left_child)

    # Do your thing here... generally pass a lambda or named function
    operation(node)

    if node.right_child is not None:
        pre_order(node.right_child)
```

Notice the similarities between the three different traversals above.
The biggest difference between each of the traversals is ***when you are looking
at the root node***.


#### Breadth First
The breadth first traversal iterates through the tree by
going through each level of the tree node by node.

***Output:*** A, B, C, D, E, F


Traditionally the breadth first traversal leverages a queue to
traverse the width (or the breadth) of the tree. Let's break down
the process:

1. First, Let's take a look at a tree that we can conduct a Breadth First traversal on:

![DepthFirst Traversal](assets/depthTraversal.PNG){:target="_blank"}


2. Let's start by putting the root Node into the queue (`Queue.enqueue(root)`)

![DepthFirst Traversal](assets/BreadthTraversal2.PNG){:target="_blank"}


3. Now that we have one node in our queue, let's `dequeue`.

![DepthFirst Traversal](assets/BreadthTraversal3.PNG){:target="_blank"}


4. Since we have completed the `dequeue` action on the the root node, we can now `enqueue` both
it's `root.left_child` and it's `root.right_child`.

![DepthFirst Traversal](assets/BreadthTraversal4.PNG){:target="_blank"}

4. We will repeat this process  with the next node in the front of the queue.

![DepthFirst Traversal](assets/BreadthTraversal5.PNG){:target="_blank"}

5. With `NodeB`, we can then `enqueue` the two children node.

![DepthFirst Traversal](assets/BreadthTraversal6.PNG){:target="_blank"}

6. `dequeue` the front of the queue
![DepthFirst Traversal](assets/BreadthTraversal7.PNG){:target="_blank"}

7. `enqueue` the children...
![DepthFirst Traversal](assets/BreadthTraversal8.PNG){:target="_blank"}

8. Keep `dequeue`ing, and only `enqueue` if the `node.left_child` or `node.right_child` is not null.
![DepthFirst Traversal](assets/BreadthTraversal9.PNG){:target="_blank"}
![DepthFirst Traversal](assets/BreadthTraversal10.PNG){:target="_blank"}
![DepthFirst Traversal](assets/BreadthTraversal11.PNG){:target="_blank"}


Here is the code, utulizing a built in queue, to
implement a Breadth First traversal.
```python
def breadth_first(self, root=None, operation=lambda node: print(node)):
    q = Queue()
    q.enqueue(root)

    while q.peek():
        front = q.dequeue()

        # Do your thing here... generally pass a lambda or named function
        operation(front)

        if front.left_child is not None:
            q.enqueue(front.left_child)
        if front.right_child is not None:
            q.enqueue(front.right_child)
```


## Binary Trees

Binary Trees are trees that only contain numbers. This is not restricted
to just `ints`, but can extend out to other numeric types such as `decimal`, `double`, `float`, etc...

There is not a specific sorting order for a binary tree. When adding a node to a binary tree,
you are not restricted on the node's location.

Here is what a binary tree looks like:

![Binary Tree](assets/BinaryTree2.PNG){:target="_blank"}

### Adding a node

When adding a node to a binary tree, we will leveraage the use of the breadth first traversal.

During the traversal, we will find the first node that does not have a left or right child node, and insert
the new node in it's place.  Because there is no structure to where nodes are "supposed to go" in a binary tree,
it really doesn't matter where the new node gets placed.

In the event you would like to have a node placed in a specific locaion, you would reference not only the new
node that is going to get created, but also the node you would like to new node to be attached to.

### Big O
The Big O of an insertion an searching in a Binary tree will always be O(n).

This is because there is no structure or organizaiton to a Binary Tree. This means that worst case
scenario, we will have to search the whole tree for the node we need to add or find.

## Binary Search Trees
A binary search tree is a type of tree that does have structure attached to it. In a binary search tree,
the tree is organized in a manner where all numbers that are smaller than the root are placed to the left,
and all numbers that are larger than the root are placed to the right.

Here is an example of a Binary Search Tree:

![BST](assets/BST1.PNG){:target="_blank"}

### Searching a BST
Searching a BST can be done quickly, because all you do is compare the node you are searching for
against each root of the tree. Dependent on the value being larger or smaller, will determine
the direction on which you will traverse.

Here is an example:

1. Let's say we are searching for the node that contains 60. First thing we do is compare 60 against the root:

2. We can see that 60 is less than 100, so we will go left.

3. We then compare 60 against the next root, 50.
4. We know that 60 is greater than 50, so we will go right.
5. Next, we compare 60 against 75. We know that 75 is greater than 60, so we go left.
6. Finally, we compare 60 against 60. These numbers are exactly the same which tells us we found our node. We then return our node back to the user.


### Big O
The Big O of a Binary Search Tree for insertion and search is O(log n).

This means that we are always able to reduce
the number of searches we do of a logrithmic value each time because of how the tree is structured.
Each traversal we do in a Binary Search Tree helps us eliminate the branches of the opposite direction
we traverse.



