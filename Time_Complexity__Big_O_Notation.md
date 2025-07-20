Source - https://www.youtube.com/watch?v=vgSKOMsjLbc
# Table of Contents

- [[#Time Complexity]]
- [[#O (Big O Order of)]]
	- [[#Definitions of O]]
		- [[#Mathematical Definition]]
		- [[#Industry Definition]]
	- [[#Types of O]]
		- [[#O(1) - Constant Time]]
			- [[#Derivation of Equation]]
		- [[#O(n) - Linear Time]]
			- [[#Derivation of Equation]]
		- [[#O(n x) - Polynomial Time (e.g., O(n 2) - Quadratic, O(n 3) - Cubic)]]
		- [[#O(log n) - Logarithmic Time]]
		- [[#O(n log n) - Log-linear (or Linearithmic or Quasilinear) Time]]
		- [[#O(2 n) - Exponential Time]]
		- [[#O(n!) - Factorial Time]]
	- [[#Order of Big O Notations from Best to Worst]]
- [[#Asymptotic Notations]]
	- [[#Big O]]
	- [[#Big Omega Ω]]
	- [[#Big Theta θ]]
- [[#Best, Worst, and Expected Cases]]
	- [[#Using Algo 1]]
		- [[#Best Case]]
		- [[#Worst Case]]
		- [[#Expected Case]]
	- [[#Using Algo 2]]
		- [[#Best Case]]
		- [[#Worst Case]]
- [[#Other Sources]]

## Time Complexity

With an increase in the Size of the Input what change will we see in the runtime of an Algorithm, this analysis is called Time Complexity Analysis.

OR

How time taken to execute an Algorithm grows with the size of the Input.

OR

Time Complexity is the study of efficiency of Algorithms.

## O (Big O | Order of)
### Definitions of O

There are two definitions or we can say, the meanings of ***O***:
1. Mathematical Definition
2. Industry Definition
#### Mathematical Definition

Academically we refer ***O*** as ***Big_O***, where O(n) can be written in many Polynomial Degree forms like O(n^2), O(n^3), etc.

Where n refers to the Input Size

#### Industry Definition

In interviews or verbally, we refer ***O*** as ***Order of*** and the Industry expects us to write the minimum of [O(n^1), O(n^2), O(n^3), etc.].

### Types of Big O or Big O Notations

Big O Notation describes the upper bound of an Algorithm's Time Complexity as the input size grows, with common types including **O(1) (Constant), O(n) (Linear), O(log n) (Logarithmic), O(n log n) (Log-linear), O(n²) (Quadratic), O(2ⁿ) (Exponential), and O(n!) (Factorial)**. These notations represent ***different growth rates*** of an Algorithm's Runtime, with `O(1) being the most efficient and O(n!) being the least efficient.`
#### O(1) - Constant Time

Irrespective of the Input Size, if the Algorithm runtime is Approximately Constant then in that case we use O(1) (Big O of 1).
##### Derivation of Equation:

Lets suppose we have an equation for a line which gives us the amount of the runtime (t), that an Algorithm will take to process Input Data of Size (n), based on the various sub-processes of the Algorithm (a, b & c). This means that whatever time each sub-process will take to process the Data, the sum of them will be the runtime (t) for the Algorithm. So, the equation will be:

t = a + b + c

We know that the runtime is Approximately Constant, so this means that there is no effect of ***n*** on the equation. Therefore, we can also write it as:

t = a(n^0) + b(n^0) + c(n^0)

Such that, Big_O for any constant is written as O(1) as [(n^0) = 1].

#### O(n) - Linear Time

If the Algorithm runtime is linear w.r.t. the Input Size, then in that case we use O(n) (Big O of n).
##### Derivation of Equation:

Lets suppose we have an equation for a line that gives us the amount of runtime (t) for an Algorithm which will take it to process Input Data of Size (n) based on the various sub-processes of the Algorithm (a, b & c). This means that whatever time each sub-process will take to process the Data, the sum of them will be the runtime for the Algorithm. So, the equation will be:

t = a + b + c

We know that the runtime is Approximately Linear, so this means that there is an effect of ***n*** on the equation. Therefore, we can also write it as:

t = a(n^1) + b(n^2) + c(n^3)

	Note: Polynomial Degrees stated in the equation are random.

In such equations, the sub-process that takes the maximum time or which is expressed with the maximum degree, will be taken in the Big_O equation, like:

O(n^3) == O(n)

#### O(n^x) - Polynomial Time (e.g., O(n^2) - Quadratic, O(n^3) - Cubic)

#### O(log n) - Logarithmic Time

#### O(n log n) - Log-linear (or Linearithmic or Quasilinear) Time

#### O(2^n) - Exponential Time

#### O(n!) - Factorial Time

### Order of Big O Notations from Best to Worst

![[Time_Complexity__Big_O_Notations_Order.png]]

- **Best** -> [[#O(1) - Constant Time]]
- **Good** -> [[#O(log n) - Logarithmic Time]]
- **Fair** -> [[#O(n) - Linear Time]]
- **Bad** -> [[#O(n log n) - Log-linear (or Quasilinear) Time]]
- **Worst** -> [[#O(n x) - Polynomial Time (e.g., O(n 2) - Quadratic, O(n 3) - Cubic)]]
- **Worst** -> [[#O(2 n) - Exponential Time]]
- **Worst** -> [[#O(n!) - Factorial Time]]

___
## Asymptotic Notations

Source: https://www.youtube.com/watch?v=1OTX-WXQHCQ

`Asymptotic Notations are used to compare multiple Algorithms at once using the same Data`. There are 3 types of Asymptotic Notations:
- Big O
- Big Omega Ω
- Big Theta θ

![[Big_O_Omega_Theta_GRAPH.png]]

### Big O
- **Definition:** A function f(n) is said to be [O(g(n))] (Big O of g(n)) if and only if there exists a constant `c` & a constant `n_0`, such that [0 <= f(n) <= c.(g(n))].
- In simple terms, if we are able to find a value of n which deserves to be called an n_0. And after this, for all the values of n that are greater than n_0, if `g(n).c >= f(n)`, then we can say the function [f(n) = O(g(n))] (Big O for g(n)).
	- g(n) is basically the ***function that is inside the Big O like O(g(n)) => O(n), O(log n), O(n log n), O(1), etc.***. And `c` is a constant.
	- f(n) is Time & n is the Input Data Size.
	- The above statement states that if there is a constant `c` which when gets multiplied to the `g(n)` their result will always be either equal or greater than the time i.e. `f(n)` for all the values where `n` is greater than or equal to `n_0`, it will fulfill this condition [0 <= f(n) <= c.(g(n))].
	- `Toh agar hum c aur n_0 ki values ka ek koi aisa combination dhund lete hai jissase fir n ki value chahe kitni hi n_0 se badhi kyu na aa jaye fir bhi ye Condition [0 <= f(n) <= c.(g(n))] fulfill hogi toh hum ye keh skenge ki Function f(n) is said to be (Big O of g(n)) [O(g(n))] but agar aisa koi combination hume nahi mila toh ye kahenge ki Function f(n) can't be said as (Big O of g(n)) [O(g(n))]`
	- Example,
```
		f(n) = 1 + n^3
		g(n) = n^4
		So, we need to find a Constant `c` and `n_0`.

		Condition: 0 <= f(n) <= c . g(n)
		Let's put the values and check the validity of the Equation.
			0 <= 1 + n^3 <= n^4 . c
		Starting from n = 1 & c = 1,
			0 <= 1 + 1^3 <= 1^4 . 1
			0 <= 2 >= 1    (This fails the condition)
		Now, n = 2 & c = 1,
			0 <= 1 + 2^3 <= 2^4 . 1
			0 <= 9 <= 16    (This Validates the Condition)
		So, we can say that if c = 1 and n_0 = 2 then for all the values where n >= n_0, the Condition will always be TRUE.
```

### Big Omega Ω

The definition & functionality of Big Omega Ω is very similar to Big O, with just a single change.
Definition: A function f(n) is said to be Big Omega Ω of g(n), if and only if there exists a constant `c` and a constant `n_0`, such that the following condition remains True:

		Condition:  0 <= c.g(n) <= f(n)

Now, here, it is said that if we are able to find a constant value for c, such that whenever the value of n is greater than the value of second constant `n_0`, the function `f(n)` will always be greater than or equal to `c.g(n)`.

### Big Theta θ

This type of Asymptotic Notation combines the functionalities of both Big O & Big Omega Ω in it, to provide us tighter boundaries around the function f(n) i.e. time.
Definition: A function f(n) is said to be Big Theta θ of g(n), if and only if there exists a group of constants like - 
	- Constant **c1** (representing Big Omega Ω) [Gives Lower Boundary]
	- Constant **c2** (representing Big O) [Gives Upper Boundary]
	- Constant **n_0**
such that the following condition remains True:

		Condition:   0 <= c1.g(n) <= f(n) <= c2.g(n)

Equations Derivation:
```
Equation for Big O -> 0 <= f(n) <= c.g(n)
Equation for Big Omega Ω -> 0 <= c.g(n) <= f(n)

So, by combining them, we get:
Equation for Big Theta θ -> 0 <= c1.g(n) <= f(n) <= c2.g(n)
```

Note: Whenever, we are required to compare two algorithms/functions performance based on their Time Complexity, it's best to use Big Theta θ, as it combines both Big O & Big Omega Ω. And therefore, gives function f(n) tighter boundaries.
___
## Best, Worst, and Expected Cases:

Source: https://www.youtube.com/watch?v=5g7K86jYto8&pp=0gcJCcMJAYcqIYzv

If we are asked to evaluate the `Time Complexity` or the `Order Of` an Algorithm/Function, then firstly we are required to know about the `Best, Worst & the Expected Cases` for the Time Complexity.
Let's understand this concept with the help of an Example Function.
```
In a Function, we get a variable `a` that has an integer value and a sorted array that has multiple integer values in it in increasing order.

Our task is to check if the value `a`, is available in the array or not.

array = [2, 4, 6, 8, 10]

n = len(array)

Also, let's say that the number of times the function has to run is equal to the number of times `k` time will be taken.
```

### Using Algo 1
**Algorithm 1** also means the approach 1 of solving this Problem Statement. In this approach, we are going to apply the simple & basic solution i.e. to use a `for` loop on the Array of size `n` to iterate over each value and check if the value matches with the value of `a`.

#### Best Case:
As per the Time Complexity, it would be the best case if the first value of the array itself is the value of `a`. In that way, the function will only have to run 1 time i.e. 1k.
Therefore, we can say that for the best case, the Time Complexity of the function is O(1) i.e. constant.

#### Worst Case:
Now, the worst case would definitely will be the case if value of `a` would be the last value of the Array. So, the function will have to run all the iterations to match with the last value. Therefore, if time taken would be `nk` i.e. if 1k = 1 iteration, then as the length of the array is `n`, so time taken for it will be `nk`. Or can be said as O(n) i.e. linear.

#### Expected Case:
The Expected Case is also known as the Average Case for the time taken by the Function in terms of Time Complexity.
```
Average Case = [(Sum of all possible runtimes) / (No. of possible runtimes)]
array = [2, 4, 6, 8, 10]
Sum of all possible runtimes = [(Runtime if a = 2) + (Runtime if a = 4) + (Runtime if a = 6) + (Runtime if a = 8) + (Runtime if a = 10) + (Runtime if a = 10)]
Note: we are adding `Runtime if a = 10`, 2 times as there is also a case if the value of `a` is not found in the Array. Therefore, that will also be counted as a possible runtime.
=> [1k + 2K + 3K + 4K + 5K + 5k]
=> 20k

Average Case = [(20k) / (5 + 1)]  (Adding 1 for the extra case)
=> 10k/3 (Now, 10/3 is a constant)
Therefore, in terms for Time Complexity, the Average Case of Time Complexity for this function will be O(n) i.e. linear.
```
Now, in this example, the array was quite small, and therefore, it was easy to calculate the Average Case. But in real-world problems, the case might be different, so there instead of taking all the values into consideration while calculating the `Sum of Possible Runtimes`, we will take something like [2, 4, 6, ...., n]. And so, for the nth value, the possible time taken will be `nk`. So, using this and formulas from Arithmetic & Geometry Progression, we calculate & fine the final value of g(n) for the Big O/Omega/Theta Function.

### Using Algo 2
**Algorithm 2** i.e. the approach 2 of solving this Problem Statement. In this approach, we are going to use a different technique to find the matching value with `a`.
Step 1: We will check if the value of `a` equals to either the first or the last value of the Array.
Step 2: If not matched, we will find the medium of the Array i.e. the middle value of the Array. If `n` is even, then we will consider both the center values and check if the value of whether `a` is less than the `center 1` value or is greater than the `center 2 value`. 
Step 3: Suppose, it's less than the `Center 1` value, then we will break the Array and keep only the part where value of `a` falls. Then, again we will find the medium and continue with the same steps until we find the value of `a`.
Now, let's further discuss this Algorithm under the Best & the Worst Cases.
#### Best Case:
Under the Best Case, it would be best if the value of `a` matches with either the first or the last value of the Array, such that only 1 iteration of the function will run.
Therefore, Time Complexity for the Best Case would be O(1) i.e. Constant.

#### Worst Case:
Now, under the Worst Case, let's say the value of `a` = 4.
So, in the first step, the function will check the value of `a` with the first and the last values of the Array i.e. 2 & 10. As the values won't match, we'll move to the second step.
Now, the medium of the Array is `6`. And the value of `a` i.e. 4 is less than the medium. So, we will break the Array into two parts and keep only `[2, 4, 6]` part for further checking.
Now, the medium is 4, and so is the value of `a`. So, hence the values matched.
So, if we count the number of iterations for the Worst Case using Algo 2, we will get 3 iterations.
And, compared to the Algo 1's Worst Case of making the 6 iterations, 3 is just half.
Similarly, let's suppose if we had an Array of size `n = 100`, and even if the value of `a` didn't exist, let's count the number of iterations it could have taken to completely check the Array using Algo 2 approach.
```
Iteration 1: Value of `a` neither matched with the first or the last values of the index.
Iteration 2: As per the Medium each part will have ~50 values.
Iteration 3: As per the Medium each part will have ~25 values.
Iteration 4: As per the Medium each part will have ~12 values.
Iteration 5: As per the Medium each part will have ~6 values.
Iteration 6: As per the Medium each part will have ~3 values.
Iteration 7: As per the Medium each part will have ~1 values.
```
So, in ~7 iterations, we got to know that the value of `a` doesn't exist in the Array, whereas with Algo 1, it would have taken ~100 iterations.
If, we look closely, for both of the above examples, when we used `Algorithm 2`, the number of iterations were very close to the log(n) (Log_base_2 means that how many times can the number n be divided by 2 to exhaust the value to ~1.)
So, based on this logic, it can be said that even for the Worst Case Scenario while using Algo 2, the Time Complexity will be O(log(n)) i.e. Logarithmic Time, which is better than the Linear Time i.e. O(n) of Time Complexity.

---

Source: https://www.youtube.com/watch?v=STL8ESuETmM&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=5

## Other Sources:

- Understanding Big-O Notation (by Coen Goedegebure, 2017) - https://www.coengoedegebure.com/understanding-big-o-notation/
- Big-O Notation Tutorial (GeeksforGeeks) - https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/
- DSA using Python in Hindi (MySirG.com) - https://www.youtube.com/playlist?list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs
- Time & Space Complexity - DSA Series (Shradha - Apna College) - https://www.youtube.com/watch?v=PwKv8fOcriM
- Hindi Data Structures And Algorithms Tutorial (by Code Basics Hindi) - https://www.youtube.com/playlist?list=PLPbgcxheSpE3NlJ30EDpxNYU6P2Jylns8
- Data Structure and Algorithms in Python (by Montukeshwar Vaishnaw) - https://www.youtube.com/playlist?list=PL13aQMQVPecA33n8w9S-cwD9geQsY8JhU
