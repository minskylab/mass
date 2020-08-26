# Computability

This section of our Learning Path is only a gentle and brief introduction to awesome topics: **Computability** and **Automata Theory**. Each one are very deep and transversal sciences but in this document we only define some concepts and refer util resources if you are more interested. The main goal is that you can make relations between this theoretical concepts and the modern software development.

## 1. What's computation and what's computable ?

    - What is a Turing Machine?
    - What can solve a Turing Machine?

### Resources

-   https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/turing-machine/one.html
-   https://www.i2cell.science/how-a-turing-machine-works/
-   https://www.quora.com/Can-all-problems-be-solved-by-a-Turing-machine

## 2. What's an automata?

It's an abstraction of machines with the computation capability, an automaton is a generalization of state machines. We have 4 classes of automatons:

1. **Combinational Logic:** time independent logic, only depends of the input [[ref]](https://books.google.com.pe/books/about/Electronic_Design.html?id=uylVPgAACAAJ&redir_esc=y).
2. **Finite-State Machine:** the FSM can change from one state to another in response to some inputs; the change from one state to another is called a transition [[ref]](https://books.google.com.pe/books/about/Formal_Methods_in_Computer_Science.html?id=1VIiwQEACAAJ&redir_esc=y).
3. **Pushdown Automaton:** the power of the context. This automaton can use the top of the stack to decide which transition to take and it can manipulate the stack as part of performing a transition.
4. **Turing Machine:** is a mathematical model of computation that defines an abstract machine, which manipulates symbols on a strip of tape according to a table of rules.

### Resources

-   [Turing about computability](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)

## 3. How now which algorithm is better? (Big O notation)

    - Sorting Algorithms
    - Data structures
    - Big O

### Resources

-   https://www.geeksforgeeks.org/sorting-algorithms/
-   https://www.bigocheatsheet.com/

## One snippet is worth hundred of words

```python
# TODO code
print("hello world")
```
