
# Index
1. [[#Types of Activation Functions]]
	- [[#Sigmoid Activation Function]]
	- [[#Tan-H Activation Function (Also Known as Hyperbolic Tangent Function)]]
	- [[#ReLU (Rectified Linear Unit)]]
	- [[#Leaky ReLU]]
	- [[#ELU (Exponential Linear Units)]]
	- [[#PReLU (Parametric Rectified Linear Unit)]]
	- [[#COMPARISON among ReLU, Leaky ReLU & Parametric ReLU]]
	- [[#SoftMax Activation Function]]
2. [[#Techniques to select one or more Activation Functions for Problem Statement]]
	- [[#For Binary Class Classification]]
	- [[#For Multi Class Classification]]
	- [[#For Regression]]

# Types of Activation Functions
## Sigmoid Activation Function

- Value for Sigmoid Activation Function falls between 0 to 1 whereas value for its Differential varies between 0 to 0.25.

- formula = 1 / (1 + e^(-x))

- Advantages:

	- If we look at the Sigmoid Curve, we can observe that their is a very smooth gradient i.e. smooth curvature when the values goes from 0 to 1. This prevents the possibility of Output Values to `jump`.

	- As it values between 0 to 1, hence it basically normalizes the output of each neuron.

	- Another advantage is that it provide clear predictions i.e. very close to 0 or 1.

- Disadvantages:

	- As Sigmoid Function uses Exponential (e) in its formula, we say it as Exponential Function which therefore results in increasing the time complexities for this Function. So, it takes more time.

	- Sigmoid Function is not Zero-centered which means that its centre doesn't go through Zero due to which it is not very efficient in Updating Weights.

	- Prone to Gradient Saturation / Vanishing Gradient Problem.

## Tan-H Activation Function (Also Known as Hyperbolic Tangent Function)

- Value for Tan-H Activation Function falls between -1 to 1 whereas value for its Differential varies between 0 to 1.

- Formula = (e^x - e^(-x)) / (e^x + e^(-x))

- Vanishing Gradient Problem may come into picture for this Activation Function as well but it will most probably come up for a very Deep Neural Network.

- Tan-H & Sigmoid are relatively Similar because,
	- When the Input is large or small, the output is almost smooth & the gradient is small, which is not good to update weight.

	- The difference among the two functions, is the output interval. The Output Interval of the Tan-H is 1.

	- Tan-H is zero-centric, which is better than Sigmoid.

- In general Binary Classification Problems, the Tan-H function is used for the Hidden Layer & the Sigmoid Function is used for the Output Layer. However, these are not static & the selection should be done based on the analysis of the specified problem.

## ReLU (Rectified Linear Unit)

- Value for ReLU Activation Function falls between 0 to Infinity whereas value for its Differential varries between 0 to 1.

- formula = max(0, x)

- One of the most used Activation Function in the Industry.

- Advantages:

	- When the Input is Positive, there is no Vanishing Gradient Problem.

	- Much Faster than Sigmoid & Tan-H in both Forward & Backward Propagation, as we are not performing any Exponential Operation.

	- ReLU Function has only a Linear Relationship.

- Disadvantages:

	- When the Input is a Negative Value, the ReLU is completely INACTIVE, which means that if a negative number is entered, the ReLU will DIE.
		Due to this, in Forward Propagation Process, it is not a problem. Some areas are sensitive & some are insensitive.
		But in Backward Propagation if you enter a negative value, the Gradient will completely be Zero, which then has the same problem as Sigmoid & Tan-H Functions have.

	- The output of ReLU Function is either ZERO or a Positive Number, which means that the ReLU is also not a Zero-Centric Activation Function.

## Leaky ReLU

- To solve the Dead ReLU Problem, people proposed to use 0.01\*X instead of 0.

- Formula = max(a\*x, x), where a = 0.01

- Output Value Range for Leaky ReLU highly depends upon the value of a.

- Theoretically, Leaky ReLU is better than ReLU, but it hasn't been fully proven that Leaky ReLU is always better than ReLU.

## ELU (Exponential Linear Units)

- formula = 
	- if x > 0, then the formula is x. We will only carry forward the value of x.
	- Otherwise, Alpha\*(e^x - 1)

- ELU is also proposed to solve the problems of ReLU, which also means that it has all the advantages of ReLU itself.

- No Dead ReLU Problem.

- The Mean Output of the ELU is close to 0, zero-centered.

- (Disadvantage) It is slightly more Computationally Intensive compared to ReLU.

- There is currently no good evidence in practice that ELU is always better than ReLU.

## PReLU (Parametric Rectified Linear Unit)

- In the negative region, PReLU has a small slope, which can also avoid the problem of Dead ReLU.

- Compared to ELU, PReLU is a Linear Operation in the negative region.

- Formula = 
	- if x > 0, then the formula is x. We will only carry forward the value of x.
	- otherwise, it is a\*x

	Can be also written as:

	- f(x) = max(0, x) + a\*min(0, x)

## COMPARISON among ReLU, Leaky ReLU & Parametric ReLU

- Taking a Standard formula to represent all ReLUs:

	- f(x) = max(0, x) + a\*min(0, x)

	- if a == 0, it becomes ReLU

	- if a > 0, it becomes Leaky ReLU

	- if a is a learnable parameter, it becomes Parametric ReLU.

## SoftMax Activation Function

- This should be applied for Multi Class Classification Problem in the Output Layer.

- Formula:
	SoftMax(z) = (e^(Zi)) / (Summation of (e^(Zj)) for j from 1 to k)
		where k is the total no. of weights that are linked to the particular Output Neuron
		Z is Weight
		i is the current Weight in the iteration
		j refers to all the weights up to the count of k

	For Example,
		Consider there is one Hidden Layer & it consists of 3 Neurons. Thus the Output Layer Neuron, will be linked to all the three Hidden Layer Neurons & therefore will be having some weights. Those weights are [10, 20, 30]

	So, the formula for the:
		1st iteration = (e^10) / Sum(e^10, e^20, e^30)
		2nd iteration = (e^20) / Sum(e^10, e^20, e^30)
		3rd iteration = (e^30) / Sum(e^10, e^20, e^30)

- The Output for this equation will always be in the form of Probability & the Sum of Probabilities for all the number of Neurons of the Output Layers will be equal to 1.

- Therefore, whichever Neuron's Probability will be the highest, that Class will be given as the final output.

# Techniques to select one or more Activation Functions for Problem Statement

## For Binary Class Classification
- Always use Sigmoid for Output Layer
- For Hidden Layer, use ReLU. If Convergence does not occur then use either PReLU or ELU. (For most of the cases, ReLU will perform good.)

## For Multi Class Classification
- For Hidden Layer, use ReLU. If Convergence does not occur then use either PReLU or ELU. (For most of the cases, ReLU will perform good.)
- For Output Layer, use SoftMax Activation Function.

## For Regression
- For Hidden Layer, use ReLU. If Convergence does not occur then use either PReLU or ELU. (For most of the cases, ReLU will perform good.)
- For Output Layer, always use Linear Activation Function.
