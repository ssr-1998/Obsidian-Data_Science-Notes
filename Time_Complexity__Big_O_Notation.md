Source - https://www.youtube.com/watch?v=vgSKOMsjLbc
# Table of Contents

- [[#Time Complexity]]
- [[#O (Big O Order of)]]
	- [[#Definitions of O]]
		- [[#Mathematical Definition]]
		- [[#Industry Definition]]
	- [[#Types of O]]
		- [[#O(1) if Algorithm runtime is Constant]]
			- [[#Derivation of Equation]]
		- [[#O(n) if Algorithm runtime is Linear]]
			- [[#Derivation of Equation]]
## Time Complexity

With an increase in the Size of the Input what change will we see in the runtime of an Algorithm, this analysis is called Time Complexity Analysis.

OR

How time taken to execute an Algorithm grows with the size of the Input.

OR

Time Complexity is the study of efficiency of Algorithms.

## O (Big O | Order of)
### Definitions of O

There are two definitions or we can meanings of ***O***:
1. Mathematical Definition
2. Industry Definition
#### Mathematical Definition

Academically we refer ***O*** as ***Big_O***, where O(n) can be written in many Polynomial Degree forms like O(n^2), O(n^3), etc.

Where n refers to the Input Size

#### Industry Definition

In interviews or verbally, we refer ***O*** as ***Order of*** and the Industry expects us to write the minimum of [O(n^1), O(n^2), O(n^3), etc.].

### Types of O

#### O(1) if Algorithm runtime is Constant

Irrespective of the Input Size, if the Algorithm runtime is Approximately Constant then in that case we use O(1) (Big O of 1).
##### Derivation of Equation:

Lets suppose we have an equation for a line which gives us the amount of runtime (t) that an Algorithm will take to process Input Data of Size (n) based on the various sub-processes of the Algorithm (a, b & c). This means that whatever time each sub-process will take to process the Data, will be the runtime for the Algorithm. So, the equation will be:

t = a + b + c

We know that the runtime is Approximately Constant, so this means that there is no effect of ***n*** on the equation. Therefore, we can also write it as:

t = a(n^0) + b(n^0) + c(n^0)

Such that, Big_O for any constant is written as O(1) as [(n^0) = 1].

#### O(n) if Algorithm runtime is Linear

If the Algorithm runtime is linear w.r.t. the Input Size, then in that case we use O(n) (Big O of n).
##### Derivation of Equation:

Lets suppose we have an equation for a line which gives us the amount of runtime (t) an Algorithm will take to process Input Data of Size (n) based on the various sub-processes of the Algorithm (a, b & c). This means that whatever time each sub-process will take to process the Data, will be the runtime for the Algorithm. So, the equation will be:

t = a + b + c

We know that the runtime is Approximately Linear, so this means that there is an effect of ***n*** on the equation. Therefore, we can also write it as:

t = a(n^1) + b(n^2) + c(n^3)

	Note: Polynomial Degrees stated in the equation are random.

In such equations, the sub-process taking maximum time or which is expressed with maximum degree will be taken in the Big_O equation, like:

O(n^3) == O(n)

___

Next Video: https://www.youtube.com/watch?v=1OTX-WXQHCQ

Asymptotic Notations are used to compare Algorithms.
There are 3 types of Asymptotic Notations:
- Big O
- Big Theta
- Big Omega

Big O
- A function f(n) is said to be [O(g(n))] (Big O of g(n)) if and only if there exists a constant `c` & a constant `n_node`, such that [0 <= f(n) <= c.(g(n))].
	- g(n) is basically the ***function of the Algorithm*** which is represented under ***Big O parentheses*** [O(g(n))].
	- f(n) is Time & n is Input Data Size.
	- The above statement states that if there is a constant `c` which when gets multiplied to the `O(g(n))` their result will always be either equal or greater than the time i.e. `f(n)` for all the values where `n` is greater than or equal to `n_node`, it will fulfill this condition [0 <= f(n) <= c.(g(n))].
	- `Toh agar hum *c* ki value ke saath *n_node* ki value ka koi ek aisa combination dhund le jissame fir *n* ki value chahe kitni hi *n_node* se badhi kyu na aa jaye fir bhi ye *Condition [0 <= f(n) <= c.(g(n))]* fulfill hogi toh hum ye keh skenge ki *Function f(n) is said to be (Big O of g(n)) [O(g(n))]* but agar aisa koi combination hum nahi dhund paye toh ye kahenge ki *Function f(n) can't be said as (Big O of g(n)) [O(g(n))]*`
	- Example,
```
		f(n) = 1 + n^3
		g(n) = n^4
		So, we need to find a Constant `c` and `n_node`.

		Condition: 0 <= f(n) <= c . g(n)
		Let's put the values and check the validity of the Equation.
			0 <= 1 + n^3 <= n^4 . c
		Starting from n = 1 & c = 1,
			0 <= 1 + 1^3 <= 1^4 . 1
			0 <= 2 >= 1    (This fails the condition)
		Now, n = 2 & c = 1,
			0 <= 1 + 2^3 <= 2^4 . 1
			0 <= 9 <= 16    (This Validates the Condition)
		So, we can say that if c = 1 and n_node = 2 then for all the values where n >= n_node, the Condition will always be TRUE.
```


13:28 - Big Omega















