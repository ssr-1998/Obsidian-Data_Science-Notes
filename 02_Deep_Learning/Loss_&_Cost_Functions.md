
# Index
1. [[#Diff b/w Loss & Cost Functions]]
2. [[#REGRESSION]]
	- [[#Mean Squared Error]]
	- [[#Mean Absolute Error]]
	- [[#Huber Loss]]
3. [[#CLASSIFICATION]]
	- [[#Cross Entropy]]
		- [[#Binary Cross Entropy (For Binary Class Classification)]]
		- [[#Categorical Cross Entropy (For Multi Class Classification)]]

# Diff b/w Loss & Cost Functions

Difference among Loss & Cost Functions is regarding the no. of records.

- Loss Function is calculated for each individual record.

- Cost Function uses the same formula as Loss Function do, but it is calculated for a batch of records.

# REGRESSION

## Mean Squared Error

- Loss Function = (1/2)\*((y - y')^2)

- Cost Function = (1/(2\*n))\*(Summation of ((y - y')^2) from 1 to n)

- we can see that (y - y')^2 equation is nothing but (a - b)^2, which means it can value as (a^2 + b^2 - 2ab) which also means that this is a Quadratic Equation.

- If we plot all the possible combinations of any Quadratic Equation, we know that it will give us a Parabola i.e. U-shape Curve.

- Advantages:
	- It is Differentiable, which means that we can take a derivative of this equation.
	- It has only One Local or Global Minima.
	- It converges faster.

- Disadvantages:
	- Not Robust to Outliers i.e. Sensitive to Outliers. It is because it uses a Quadratic Equation i.e. it squares the Error we get which can also be referred as Penalizing the Error.

## Mean Absolute Error

- Loss Function = (1/2)\*(|y - y'|)

- Cost Function = (1/(2\*n))\*(Summation of (|y - y'|) from 1 to n)

- If we Plot all the possible combinations of any Absolute Equation, it will give us a V-shape Curve.

- Advantages:
	- It is Roboust to Outliers.

- Disadvantages:
	- It is Time Consuming.
		As it is not a Quadratic Equation, therefore we will have to take sub-gradient of this Equation.
		Sub-Gradient basically means that we will have to divide the V-shape Curve part-by-part & then calculate the slope of the line as it can be different for both sides of V-Shape Curve. This is required to Update Neurons Weight & therefore becomes Time Consuming. 

## Huber Loss

- It is a combination of MAE & MSE.

- Loss Function:
	- Delta is a Hyperparameter which is used in Huber Loss. It is a number which is stated as a threshold loss value which will be considered as a Decision Maker whether a Calculated Loss is a Large Loss or a Small Loss & based on that it will allot them the specified formula.
	- For Example, if Delta is 50, then if the calculated loss is less than the Delta Loss then we will use MSE Function which also means that MSE will not be applied for any Outlier Based Dataset as if it gets Large Calculated Loss, it will show big changes as it is sensitive to Outliers.
	- In case (Calculated Loss >= Delta Loss), the Huber Loss will apply a formula which is based on MAE Loss.

	- If |y - y'| <= Delta, Formula will be (1/2)\*((y - y')^2)
	- Otherwise, ((Delta \* |y - y'|) - ((1/2) \* Delta^2))

# CLASSIFICATION

## Cross Entropy

### Binary Cross Entropy (For Binary Class Classification)

- It is the same loss function that we use in Logistic Regression i.e. Log Loss.

- Formula:
	- (-y \* log(y')) - ((1 - y) \* log(1 - y'))

	OR

	- If y == 0, then formula = -log(1 - y')
	- If y == 1, then formula = -log(y')

- For calculating the y' for Binary Cross Entropy, we should strictly be using Sigmoid Activation Function in the Output Layer.

### Categorical Cross Entropy (For Multi Class Classification)

- In this, the first step is that the Categorical Cross Entropy will perform One-Hot Encoding on the Categorical Feature.
	This will give them multiple columns containing 0 & 1 values for each class.

- Formula:
	- (Xi, Yi) = (-) (Summation of (Yij \* LOGe(Y'ij)) for j from 1 to c i.e. Categories)
		here, i = rows & j = columns from the dataset of the One-Hot Encoded Output Variable.

		Calculations for Yij:
			For Example,
			Consider there is a dataset having 3 rows & 3 Columns.

		If i = 1, that means row 1:
			Y1 = [Y11, Y12, Y13] == [Y11, Y12, Y13, ..., Y1c] basically stating the Y1 will be equal to the summation of all the values of Y up to the no. of Categories which is represented by c.

		So, we can say:
			- Yij = 1 (if element is in Class)
			- Yij = 0 (Otherwise)

		Calculations for Y'ij:
			We use SoftMax Activation Function to get this.
