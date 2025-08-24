
# Index
1. [[#Subsets of Artificial Intelligence]]
2. [[#History of Neural Networks]]
3. [[#Perceptron]]
	- [[#Introduction]]
	- [[#From Krish Naik's Video]]
	- [[#Inside Hidden Layer Neuron's Process]]
	- [[#Perceptron's Drawback]]
4. [[#Neural Networks Inspired from the Human Brains]]
5. [[#Forward Propagation]]
6. [[#Back Propagation]]
	- [[#Meaning]]
	- [[#Formula for Updating the Weights]]
	- [[#Chain Rule of Differentiation]]
	- [[#Vanishing Gradient Problem / Gradient Saturation / Gradient Dispersion]]
7. [[#Loss & Cost Functions]]
	- [[#Diff b/w Loss & Cost Functions]]
	- [[#REGRESSION]]
		- [[#Mean Squared Error]]
		- [[#Mean Absolute Error]]
		- [[#Huber Loss]]
	- [[#CLASSIFICATION]]
		- [[#Cross Entropy]]
			- [[#Binary Cross Entropy (For Binary Class Classification)]]
			- [[#Categorical Cross Entropy (For Multi Class Classification)]]
8. [[#Types of Activation Functions]]
	- [[#Sigmoid Activation Function]]
	- [[#Tan-H Activation Function (Also Known as Hyperbolic Tangent Function)]]
	- [[#ReLU (Rectified Linear Unit)]]
	- [[#Leaky ReLU]]
	- [[#ELU (Exponential Linear Units)]]
	- [[#PReLU (Parametric Rectified Linear Unit)]]
	- [[#COMPARISON among ReLU, Leaky ReLU & Parametric ReLU]]
	- [[#SoftMax Activation Function]]
	- [[#Techniques to select one or more Activation Functions for Problem Statement]]
		- [[#For Binary Class Classification]]
		- [[#For Multi Class Classification]]
		- [[#For Regression]]
9. [[#Types of Optimizers]]
	- [[#Gradient Descent / Batch Gradient Descent]]
	- [[#Stochastic Gradient Descent]]
	- [[#Mini-Batch Stochastic Gradient Descent]]
	- [[#Mini-Batch SGD with Momentum]]
	- [[#AdaGrad (Adaptive Gradient Descent)]]
	- [[#Adadelta & RMSPROP]]
	- [[#Adam Optimizer]]
10. [[#CNN]]
	- [[#CNN vs Human Brain]]
	- [[#Convolution Operation]]
		- [[#Pointers on Image Data]]
		- [[#Step 1 ***Min Max Scaling***]]
		- [[#Step 2 ***Convolution, Filters & Stride***]]
		- [[#Step 3 Padding]]
	- [[#Pooling]]
	- [[#Flattening Layer]]
11. [[#Recurrent Neural Network (RNN)]]
	- [[#Need for RNN]]
	- [[#Forward Propagation Over Time]]
	- [[#Back Propagation Over Time]]
12. [[#Long Short Term Memory (LSTM)]]

### Subsets of Artificial Intelligence

![[Pasted image 20240414091851.png]]

- ***AI*** - An application which can do its own task without any human intervention.
- ***ML*** - Provides Statistical Tools to analyze, visualize, prediction, forecasting, clustering on the data.
- ***DL*** - Mimic Human Brains i.e. how we human beings lean things.
- ***DS*** - Data Science covers everything over here, A Data Scientist might work as a Data Analyst/ML Engineer/DL Engineer.
### History of Neural Networks

#### Perceptron

##### Introduction

It all started with `Rosenblatt’s Perceptron`. 

A single perceptron has certain inputs, weights and biases. The weighted sum of these weights & inputs combined with the biases forms the output of the perceptron, as shown in the diagram below.

![[Pasted image 20240414092224.png]]

The perceptron convergence theorem guarantees that if classes are linearly separable, the perceptron will learn a linear boundary within finite steps.
##### From Krish Naik's Video

There will be a single hidden layer of Neurons to process the information & pass it to the output layer for final verdict.

Neurons in Input Layer = Number of Input Variables we have in Data.

Weights: Weight basically says that how much the Neurons should get activated or deactivated. (Eg: If Hot Object is placed on Hand, Neurons inside hand will signal Brain this information & the hidden layers will process it & pass the processed information to output layer for the final verdict which will be how quickly the body should react to remove that hot object.)

###### Inside Hidden Layer Neuron's Process

a) For all the no. of inputs, there are weights that are assigned to them & in the first step we basically take the Summation of all XiWi i.e. Summation[X1W1, X2W2, X3W3, ..., WnWn]. This is also represented as W^Tx (W transpose x) {Also known as Linear Regression Equation}
	Bias is also added in this step so if by mistake we pass the weights as 0, the summation should not end up as 0 instead the Bias (constant/intercept in linear regression) will add some value to it.
	![[Pasted image 20240414095607.png]]

b) Activation Function over y [Activation_Function(Sigma(XiWi) + Bias)] - There are perhaps three activation functions you may want to consider for use in hidden layers; they are: `Rectified Linear Activation (ReLU)`, `Logistic (Sigmoid)` &  `Hyperbolic Tangent (Tan-H)`.

Sigmoid Activation Function is used for Binary Classification as it returns either 0 to 1.
Equation.
	(1 / (1 + e^(-y)))
		- `^()` means to the power of e
		- y = Sigma XiWi + Bias

Linear Activation Function is used for Regression problems.

For each Neuron of Hidden Layer the above two steps will be preformed & each will generate some output i.e. Oi.
Once, we get Oi from each Neuron of Hidden Layer, we send it to Output layer again with a weight & Bias.

> Note that the hidden and output layers can contain biases because they contain neurons that perform a linear or non-linear transformation.

Hence in Output Layer as well, the above mentioned two steps will be performed.
And based on the Threshold, the Model Classifies the Output.

#### Perceptron's Drawback

Although Perceptron’s convergence theorem guaranteed that two linearly separable classes can be separated using a single straight line, the XOR problem required two straight lines to separate two classes.
As you can see in the diagram below, a single line cannot separate two classes, as it would require more than one line to do so, which means that we would require more than one perceptron for separation.

![](https://images.upgrad.com/431db171-372a-4122-ab59-7a41cf9836b9-3.png)

After this, the Artificial Intelligence fell into an era called `AI Winter`, where no development was further done.

But...

Later on it again got attraction due to some of the most prominent figures who were responsible for the revival of Artificial Intelligence are `Yan Lecun`, `Geoffrey Hinton`, `Yoshua Bengio` & `Andrew Ng`.

- [Yan Lecun](https://en.wikipedia.org/wiki/Yann_LeCun) is the founding father of Convolutional Neural Networks.
- [Andrew Ng](https://en.wikipedia.org/wiki/Andrew_Ng) is the co-founder of Google Brain and is known for his video series on Deep Learning.

### Neural Networks Inspired from the Human Brains

Human Brain:
![](https://images.upgrad.com/9fdfbb41-ab2b-4afa-a974-9df6ad8ea19d-4.png)

Neural Networks:
![](https://images.upgrad.com/5147cb5e-0792-43bf-95f7-794fd31f3344-5.png)

***Comparison between Human Brain Parts & Neural Network Parts***
![[Pasted image 20240414093243.png]]

### Forward Propagation

It is basically the Straight/Right flow of the Model Steps i.e. Forward Propagation only refers to the process under which we take input from the Input Layer then multiply each with Random/Optimized Weights, sum them all up & add Bias after which the result goes into the Activation Function to get Activated & moves forward towards the Output Layer.

So, basically it is referred to as the Process of how Deep Learning Model Architecture Works from 

> Input -> Hidden -> Output Layers respectively.

**Steps: [ Input Layer -> Weights Added -> Bias Added -> Activation Function ]**

### Back Propagation

***Note:***
- Weight Updating Formula, Chain Rule of Differentiation/Derivation are all performed under Back Propagation by the use of Optimizers.

#### Meaning
Back Propagation is referred to as moving backward in the Process with the aim of optimizing each & every Weight we are having in the model to finally Minimize the Loss Function i.e. Error.

Steps: [ Loss Function -> Optimizers -> Weights Updating ]

#### Formula for Updating the Weights

Weight Updating Formula = Old_Weight - Learning_Rate( Derivative of Loss with respect to Derivative of Old_Weight )

![[DL__Weight_Updation_Formula.png]]

(Derivative of Loss w.r.t Derivative of Old_Weight) is actually the Slope of Gradient Descent (curve b/w Loss Function & Weights) which helps in finding the Direction of Weights i.e. whether they Increase or Decrease.

>Formula for Updating the Biases: It is same as Weights Updating Formula.

#### Chain Rule of Differentiation

This means that the Derivation of Y w.r.t Derivation of X can be linked through other Derivatives of Variables such as Z, Q, etc.
(Derivative of Y w.r.t Derivative of X) = (Derivative of Y w.r.t. Derivative of Z) * (Derivative of Z w.r.t. Derivative of X)

For Example,
![[Chain_Rule_of_Differentiation_EXAMPLE.png]]
As per this Example Image, if we are needed to find the (Derivative of Loss w.r.t. Derivative of W1_OLD)
Then as per the Chain Rule, the Formula will be:

(Derivative of Loss w.r.t. Derivative of W1_OLD) = 
[(Derivative of Loss w.r.t. Derivative of O31) * (Derivative of O31 w.r.t. Derivative of W4) * (Derivative of W4 w.r.t. Derivative of O21) * (Derivative of O21 w.r.t. Derivative of W2) * (Derivative of W2 w.r.t. Derivative of O11) * (Derivative of O11 w.r.t. Derivative of W1)]  + [(Derivative of Loss w.r.t. Derivative of O31) * (Derivative of O31 w.r.t. Derivative of W5) * (Derivative of W5 w.r.t. Derivative of O22) * (Derivative of O22 w.r.t. Derivative of W3) * (Derivative of W3 w.r.t. Derivative of O11) * (Derivative of O11 w.r.t. Derivative of W1)]

![[Chain_Rule_of_Differentiation_EXAMPLEs_SOLUTION.png]]

#### Vanishing Gradient Problem / Gradient Saturation / Gradient Dispersion

With the use of Chain Rule now we know how we can find the (Derivative of Loss w.r.t. Derivative of W1) but one important point to note down is that ==***Derivation/Differentiation of Sigmoid Activation Function always ranges between 0 - 0.25***==
which basically means that as per the Chain Rule if there are many Hidden Layers & for all the Outputs of Hidden Layer Neurons if Sigmoid Activation Function is applied then for almost all the Derivations among Chain Rule will have a maximum of 0.25 value which in short will result in a small value. And as per the Weight Updating Formula, we know that we multiply the (Derivative of Loss w.r.t. Derivative of W1) with a Learning Rate which also is a very small value.

Weight Updating Formula = Old_Weight - Learning_Rate( Derivative of Loss with respect to Derivative of Old_Weight )

Hence, this means that in the above Formula, to get new Weight when we will subtract a small value from the old weight their will not be any major change in the weight which might result in getting the approximately same Weight again & again. This Problem is known as VANISHING GRADIENT PROBLEM.
To handle this in Multi-Layer Neural Network it is important to select different types of Activation Functions instead of all being the same or only Sigmoid.

### Loss & Cost Functions
	
#### Diff b/w Loss & Cost Functions

Difference among Loss & Cost Functions is regarding the no. of records.
- Loss Function is calculated for each individual record.
- Cost Function uses the same formula as Loss Function do, but it is calculated for a batch of records.

#### REGRESSION

##### Mean Squared Error

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

##### Mean Absolute Error

- Loss Function = (1/2)\*(|y - y'|)

- Cost Function = (1/(2\*n))\*(Summation of (|y - y'|) from 1 to n)

- If we Plot all the possible combinations of any Absolute Equation, it will give us a V-shape Curve.

- Advantages:
	- It is Roboust to Outliers.

- Disadvantages:
	- It is Time Consuming.
		As it is not a Quadratic Equation, therefore we will have to take sub-gradient of this Equation.
		Sub-Gradient basically means that we will have to divide the V-shape Curve part-by-part & then calculate the slope of the line as it can be different for both sides of V-Shape Curve. This is required to Update Neurons Weight & therefore becomes Time Consuming. 

##### Huber Loss

- It is a combination of MAE & MSE.

- Loss Function:
	- Delta is a Hyperparameter which is used in Huber Loss. It is a number which is stated as a threshold loss value which will be considered as a Decision Maker whether a Calculated Loss is a Large Loss or a Small Loss & based on that it will allot them the specified formula.
	- For Example, if Delta is 50, then if the calculated loss is less than the Delta Loss then we will use MSE Function which also means that MSE will not be applied for any Outlier Based Dataset as if it gets Large Calculated Loss, it will show big changes as it is sensitive to Outliers.
	- In case (Calculated Loss >= Delta Loss), the Huber Loss will apply a formula which is based on MAE Loss.

	- If |y - y'| <= Delta, Formula will be (1/2)\*((y - y')^2)
	- Otherwise, ((Delta \* |y - y'|) - ((1/2) \* Delta^2))

#### CLASSIFICATION

##### Cross Entropy

##### Binary Cross Entropy (For Binary Class Classification)

- It is the same loss function that we use in Logistic Regression i.e. Log Loss.

- Formula:
	- (-y \* log(y')) - ((1 - y) \* log(1 - y'))

	OR

	- If y == 0, then formula = -log(1 - y')
	- If y == 1, then formula = -log(y')

- For calculating the y' for Binary Cross Entropy, we should strictly be using Sigmoid Activation Function in the Output Layer.

##### Categorical Cross Entropy (For Multi Class Classification)

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

### Types of Activation Functions

#### Sigmoid Activation Function

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

#### Tan-H Activation Function (Also Known as Hyperbolic Tangent Function)

- Value for Tan-H Activation Function falls between -1 to 1 whereas value for its Differential varies between 0 to 1.

- Formula = (e^x - e^(-x)) / (e^x + e^(-x))

- Vanishing Gradient Problem may come into picture for this Activation Function as well but it will most probably come up for a very Deep Neural Network.

- Tan-H & Sigmoid are relatively Similar because,
	- When the Input is large or small, the output is almost smooth & the gradient is small, which is not good to update weight.

	- The difference among the two functions, is the output interval. The Output Interval of the Tan-H is 1.

	- Tan-H is zero-centric, which is better than Sigmoid.

- In general Binary Classification Problems, the Tan-H function is used for the Hidden Layer & the Sigmoid Function is used for the Output Layer. However, these are not static & the selection should be done based on the analysis of the specified problem.

#### ReLU (Rectified Linear Unit)

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

#### Leaky ReLU

- To solve the Dead ReLU Problem, people proposed to use 0.01\*X instead of 0.

- Formula = max(a\*x, x), where a = 0.01

- Output Value Range for Leaky ReLU highly depends upon the value of a.

- Theoretically, Leaky ReLU is better than ReLU, but it hasn't been fully proven that Leaky ReLU is always better than ReLU.

#### ELU (Exponential Linear Units)

- formula = 
	- if x > 0, then the formula is x. We will only carry forward the value of x.
	- Otherwise, Alpha\*(e^x - 1)

- ELU is also proposed to solve the problems of ReLU, which also means that it has all the advantages of ReLU itself.

- No Dead ReLU Problem.

- The Mean Output of the ELU is close to 0, zero-centered.

- (Disadvantage) It is slightly more Computationally Intensive compared to ReLU.

- There is currently no good evidence in practice that ELU is always better than ReLU.

#### PReLU (Parametric Rectified Linear Unit)

- In the negative region, PReLU has a small slope, which can also avoid the problem of Dead ReLU.

- Compared to ELU, PReLU is a Linear Operation in the negative region.

- Formula = 
	- if x > 0, then the formula is x. We will only carry forward the value of x.
	- otherwise, it is a\*x

	Can be also written as:

	- f(x) = max(0, x) + a\*min(0, x)

#### COMPARISON among ReLU, Leaky ReLU & Parametric ReLU

- Taking a Standard formula to represent all ReLUs:

	- f(x) = max(0, x) + a\*min(0, x)

	- if a == 0, it becomes ReLU

	- if a > 0, it becomes Leaky ReLU

	- if a is a learnable parameter, it becomes Parametric ReLU.

#### SoftMax Activation Function

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

#### Techniques to select one or more Activation Functions for Problem Statement

##### For Binary Class Classification
- Always use Sigmoid for Output Layer
- For Hidden Layer, use ReLU. If Convergence does not occur then use either PReLU or ELU. (For most of the cases, ReLU will perform good.)

##### For Multi Class Classification
- For Hidden Layer, use ReLU. If Convergence does not occur then use either PReLU or ELU. (For most of the cases, ReLU will perform good.)
- For Output Layer, use SoftMax Activation Function.

##### For Regression
- For Hidden Layer, use ReLU. If Convergence does not occur then use either PReLU or ELU. (For most of the cases, ReLU will perform good.)
- For Output Layer, always use Linear Activation Function.

### Types of Optimizers

#### Gradient Descent / Batch Gradient Descent

- Trains the Neural Network for all the no. of records in a Single Batch whether the dataset consists of 1K records or 1000K records.

- Therefore, to load & train such heavy dataset in a single go, it requires Huge Amount of RAM or maybe GPUs as well.

- That's why its biggest Disadvantage is that it Resource Extensive.

#### Stochastic Gradient Descent

- Trains the Neural Network for one record at a time.

- Due to which, Huge RAM issue which we were having for Batch Gradient Descent won't arise here.

- But, it will now have to perform Huge No. of Iterations for each record to be trained, which will definitely take very long time & thus Convergence will be very slow.

#### Mini-Batch Stochastic Gradient Descent

- We get to select the no. of records we want to Train in a single Batch i.e. Batch Size.

- Therefore, it is Resource Intensive.

- Convergence will be Better.

- Time Complexity will Improve.

- Still it has Noise while jumping to the next appropriate Weight in Gradient Descent Curve.

#### Mini-Batch SGD with Momentum

- To reduce the Noise we have in Mini-Batch SGD, researchers came up with this Optimizer.

- Here, we use Momentum to get a smoothing effect while jumping to the next best Weight for Neural Network.
	This we achieve by using Exponential Weighted Average by making some changes in the (Derivative of Loss w.r.t Derivative of Weight) in Weight updating formula.

- Weight updating formula earlier used => New_Weight = OLD_Weight - (Learning_Rate * ( Derivative of Loss with respect to Derivative of Old_Weight ))

- To understand the Derivation of New formula,
	Let's suppose the Name of the Weight for one Neuron Connection as T like earlier we used to name it as W1.
	The Value for this weight will be termed as A, which will be calculated based on `Mini-Batch SGD` to provide base for a new yet modified & smoothed Weight for the Neuron.
	
	Here, we will be showing the calculation for the updating of only one weight such as W1, which in this case is T & values A.
	Now, we know that due to multiple Epochs, we will get multiple Versions of the Same Neuron Connection Weight.
	So, we will calculate the next version of Weight based on previous Optimizer:

	Versions							                T1	T2	T3	...	Tn
	Values as per Mini-Batch SGD		A1	A2	A3	...	An
	Smoothed Values of Weights			A1	 ?	     ?	    ...	 ?

	So, we can say that the Value for Weight Version T1 = A1
	Now, using Exponential Weighted Average, we will write a new formula for getting the next best Smoothed Weight for T2.
		(Smoothed Value of T2) = (Beta \* (Value of T1)) + ((1 - Beta) \* (A2))
			where Beta is a Hyperparameter which will act as an Importance(weightage in %age) that should be given to the earlier Version of Neuron Weight i.e. T1.

	Such that, the new Version of Neuron Weight will actually be more connected to the Earlier Version Weight & less connected to the A2 i.e. Mini-Batch SGD Predicted Weight Version.

	Likewise for T3,
			(Smoothed Value of T3) = (Beta \* (Smoothed Value of T2)) + ((1 - Beta) \* (A2))

	So, the final new formula for Weight Updating using Exponential Weighted Average will be:

	W_T2 = W_T1 - (Learning Rate) \* (Smoothed Value of the Derivative)

	(Smoothed Value of Derivative w.r.t T2) = (Beta \* (Smoothed Value of Derivative w.r.t T1)) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of (Smoothed Value of T1)))

	In General, this above equation can be written as:

	W_t = W_(t - 1) - ((Learning Rate) \* (V_dw_t i.e. Smoothed Value of Derivative w.r.t. t))

	V_dw_t == (Smoothed Value of Derivative w.r.t. T2) = (Beta \* (V_dw_(t - 1))) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of W_(t - 1)))

	where,
		t is representing T2 or any T based on the Iteration.
		(t - 1) is representing T1 or any previous version of T.

- Advantages:
	- Reduces the Noise.
	- Uses Mini-Batch SGD for batch size.
	- Quicker Convergence.

#### AdaGrad (Adaptive Gradient Descent)

- In this Optimizer the Learning Rate which is being used in the Weight Updating Formula since starting is Adaptive in Nature instead of a Fixed Nature.

- Learning Rate is used to maintain the Speed of the Convergence & till now it used to be a Fixed Value which we used to provide to the Neural Network. But now, in this Optimizer, the Learning Rate will be having an Adaptive Nature i.e. it will become smaller & smaller as we move towards the Global Minima.

- formula for Weight updating: W_t = W_(t - 1) - ((Learning Rate with eta) \* (Derivative of Loss w.r.t. Derivative of [Old_Weight or W_(t - 1)]))

	(Learning Rate with eta) = (Learning Rate) / SQRT(Alpha_t + Epsilon)
		where,
		- Epsilon is a small number such that if Alpha_t or (Alpha w.r.t. t) becomes 0, the denominator should not become 0 & should not make the output as Infinity.
	
	Alpha_t = (Summation of (Derivative of Loss w.r.t. Derivative of W_t) for i from 1 to t)^2
		where, t refers to all the previous versions of Currently Updating Weight.
	
	So, if we try to understand this, with more & more Epochs, the number of versions for each Neuron Connection Weight are going to increase & therefore the Summation in Alpha_t will also increase.
	As Alpha_t is going to increase, we know that it's in Denominator of the formula for (Learning Rate with eta) which means that the (Learning Rate with eta) will decrease after each Epoch.
	As the (Learning Rate with eta) decreases after every Epoch, we will get the Adaptive Nature for the Learning Rate.

- (Disadvantage) With more & more Epochs, the Alpha_t can be a Huge Number & due to which there can be a chance that (Learning Rate with eta) will become a very small number. Such that, the Change in the Old & New Weights will be negligible.

- (Disadvantage) Doesn't have the Smoothing Weight Updating Technique.

#### Adadelta & RMSPROP

- To overcome the disadvantage of Adagrad i.e. chances of making negligible changes to the (Learning Rate with eta).

- For this, we will apply Exponential Weighted Average in (Learning Rate with eta) formula as well. Which will then help us to control the rate of changes to the (Learning Rate with eta).

- formula for Weight updating: W_t = W_(t - 1) - ((Learning Rate with eta) \* (Derivative of Loss w.r.t. Derivative of [Old_Weight or W_(t - 1)]))

	(Learning Rate with eta) = (Learning Rate) / SQRT(S_dw_t i.e. Smoothed Value of Derivative w.r.t. t + Epsilon)
		where,
		- Epsilon is a small number such that if Alpha_t or (Alpha w.r.t. t) becomes 0, the denominator should not become 0 & should not make the output as Infinity.
	
	S_dw_t = (Beta \* (S_dw_(t - 1))) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of W_(t - 1)))
		where, t refers to all the previous versions of Currently Updating Weight.

- (Disadvantage) Doesn't have the Smoothing Weight Updating Technique.

#### Adam Optimizer

- Created to overcome disadvantage of Adadelta & RMSPROP i.e. they both were missing the Smoothing Weight updating Technique.

- As this Optimizer is combining the ***Smoothening Weight Updating Technique*** & ***Smoothening Adaptive Learning Rate*** from ***Mini Batch SGD with Momentum*** & ***AdaDelta*** respectively.

- Formula's:
	Weight Updating =>
		W_t = W_(t - 1) - ((Learning Rate with ETA) \* V_dw_t)
		V_dw_t = (Beta \* V_dw_(t - 1)) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of W_(t - 1)))
		(Learning Rate with ETA) = Learning_Rate / SQRT(S_dw_t + Epsilon)
		S_dw_t = (Beta \* S_dw_(t - 1)) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of W_(t - 1)))

	Bias Updating =>
		B_t = B_(t - 1) - ((Learning Rate with ETA) \* V_db_t)
		V_db_t = (Beta \* V_db_(t - 1)) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of B_(t - 1)))
		(Learning Rate with ETA) = Learning_Rate / SQRT(S_db_t + Epsilon)
		S_db_t = (Beta \* S_db_(t - 1)) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of B_(t - 1)))
- Adam Optimizer computes Adaptive Learning Rates for each Parameter. In addition to Storing an Exponentially Decaying Average of Past Squared Gradients, it also keeps an Exponentially Decaying Average of Past Gradients, similar to Momentum.

### CNN

#### CNN vs Human Brain

- In Human Brain, there is a part named Cerebral Cortex which consists of another part of the part that is named as Visual Cortex.

- Visual Cortex is responsible for receiving, segmenting & integrating of Visual Information which it receives from the Retina.
	The Processed Information of Visual Cortex is subsequently sent to other regions of the Brain to be Analyzed & Utilized.
	There may be Multiple Layers of Visual Cortex in Cerebral Cortex that are responsible for performing many different actions like detection of moving objects, type of beings and many other things.

#### Convolution Operation

- Multiple Steps are performed under the Convolution Operation. We will discuss each one by one.

##### Pointers on Image Data

- Any image is of two type either `Black & White` or `RGB i.e. Red-Green-Blue`.

- Images contain Multiple Pixels & each Pixel ranges between 0 to 255.
	0 refers to Black
	255 refers to White

- For `Black & White` Image, the image size is represented as 5x5 i.e. 5 rows & 5 columns of a matrix each representing a pixel.

- For RGB Image, the Image Size is represented as 5x5x3 i.e. 5 rows, 5 columns & 3 Channels (Red-Green-Blue).

##### Step 1: Min Max Scaling

- `Min Max Scaling` is applied on the Input Image which converts each pixel value between 0 to 1 by dividing each Pixel Value by 255.

##### Step 2: Convolution, Filters & Stride

- Example of Input & Filter for better understanding.

	![[Pasted image 20240414134347.png]]

- There are multiple types of Filter that we can apply on the Input Images to extract Features from the Input Image.

- Operation happens this way that we put the Filter on top of the Input Image, as the filter is of 3x3 it will be first applied to the Top Corner 3x3 Pixel Values of the Input Image, like for 
	***1st iteration:***

	![[Pasted image 20240414134721.png]]

	A variable named `Stride` is used here which specifies the number of pixel row jumps should be between each Iteration to the left of the Input Image.

	***2nd Iteration (Stride = 1):***

	![[Pasted image 20240414134832.png]]

	***3rd Iteration (Stride = 1):***

	![[Pasted image 20240414134906.png]]

	***4th Iteration (Stride = 1):***

	![[Pasted image 20240414135222.png]]
	
	now as the Filter has reached the last row to the right, it will slide down to column no. 2 & start same 4 iteration from there. In the end we get:

	![[Pasted image 20240414135304.png]]

	and now we ***Inverse the Min Max Scaling*** on the Result Matrix which gives us:

	![[Pasted image 20240414135341.png]]

	this happened because to Inverse the effect of `Min Max Scaling`, the Minimum Value will be converted to 0 & the Maximum Value will be converted to 255.

	So, if we try to visualize this resultant image, we can see that on both vertical edges we get White Color & in middle we get all Black. So, this is how the Convolution Operation helps us in Extracting Important Features using many different Filter/Kernels.

	Also we can observe that Input Matrix was (6x6), Filter Matrix was (3x3) & the Resultant Matrix was (4x4) which we got.

	So, to calculate the Output Matrix Size, we can use below formula:

	$((n - f) + 1)/s$

	where,
		n refers to the Input Matrix Size
		f refers to the Filter Matrix Size
		s refers to the Stride Value

	Like, $((6 - 3) + 1)/1 = 4$

##### Step 3: Padding

- Taking above Example forward, we can observe another point is that the size of the Output Matrix got Shrinked after applying the Filter using Convolution Operation.

- Shrinking of Image Matrix also means that we lost some information in the Output Image compared to the Input Image.

- To prevent this, Padding is used. Padding is like providing an extra layer of Protection to the Image Matrix.

- For this, we basically add more row & columns to the Input Image Matrix on the outside due to which after performing the Convolution Operation, the Output Image Matrix will also be having the same Size as we Originally had for the Input Image.

- Using Above Example to explain:

	Output Matrix Size Calculation Formula is updated to:

	$(((n + 2P) - f) + 1)/s$

	So, using this we can also find the no. of layers to be added for Padding.

	$Output Matrix Layer = ((Input Size + (2*Padding Layers)) - Filter Size) + 1$

		$6 = (((6 + 2P) - 3) + 1)/1$
		$5 = ((6 + 2P) - 3)$
		$5 = 2(3 + P) - 3$
		$8 = 2(3 + P)$
		$8/2 = 3 + P$
		$4 = 3 + P$
		$P = 1$
	
	So, we need to add 1 Layer of Padding to get Same Output & Input Sizes.

	There are multiple ways to add pixel values in the Padding Layers. Some are:

	- Adding all pixel values as 0.

	- Copying the nearest Pixel Value.

- Now, we know how Convolution Operation Works but here Filters play an important role. As for the Example, the Filter Matrix was Hard Coded, but in reality the Filter Matrix Values do modify.

- Like in ANN, we used to update the Weights & Biases using Backward Propagation. Here in CNN, we also update the Filter Matrix Values using the Backward Propagation and for this we apply the Activation Function i.e. ReLU on each Pixel Value of the Output Image Matrix.

- So, in the end we can say that the Convolution Operation consists of an Input Image on which we apply `Min Max Scaling` & we add Padding if necessary, after which we can apply one or many Filter Operations on the Input Image to extract specific Features from the Image & then we inverse the `Min Max Scaling` on the Output Image Matrix. After this, we in the end apply the Activation Function on the Output Image Matrix.

	NOTE: The above Convolution Operation is just a summary & there can be multiple Convolution Operations in a single Convolution Neural Network (CNN).

#### Pooling

- We know that there can be many Filters in a single Convolution Operation & there can be many Convolution Operations in a Single CNN Architecture.

- There is a term called `Location Invariant` which specifically says that there can be multiple Objects in a single Image & as we proceed towards the next Convolution Operation in CNN the Model should be able to extract more & more clearer information/features from the Input Image. This means that it wants the Model to extract better & more clearer information from the Input Images compared to the previous Convolution Operation.

	In short, each Convolution Operation should provide such an output that it will help the next Convolution Operation to extract better & more clearer Information/Features from the Image Data.
	
	And to do so, we use Pooling Techniques.

- Pooling Techniques are used to find & extract the most important features from the Output Image Matrix of the Previous Convolution Operation.
	There are mainly three type of Pooling Techniques:
	- Max Pooling
	- Average Pooling
	- Min Pooling

- Let's say that the Output Image Matrix of Previous Convolution Operation is of 3x3 Size & we want to apply a Max Pooling of 2x2 Size on top of it.

- So, similar to the Convolution Operation, from Top Left of the Output Image Matrix a 2x2 Size Matrix Values will be selected & checked which one is the Max out of all of them. The Max value will be the 1st Value of the Max Pooling Matrix.

- Here in Max Pooling, we generally use (Stride = 2) & such that using the Max Pooling we get the most important feature from the Output Image Matrix from the Previous Convolution Operation.

- So, we can end with this point that after each Convolution Operation a Pooling Technique is applied & as there can be many Filters in each Convolution Operation therefore, there will be multiple corresponding Output Image Matrices. Hence, for each Output Image Matrix from the Previous Convolution Operation, we apply the Pooling Technique & therefore in the end we get many 2x2 or of the specified size Pooled Matrices.
- Important Points:
	- Pooling reduces the width and height of the output, thereby reducing the number of parameters and the amount of computation being done in the Feed Forward Network.
	- Pooling reduces the number of parameters and computation, thus it also controls overfitting.
	- Since pooling takes a statistical aggregate over multiple regions of an image, it makes the network invariant to 'local transformations' (such as the face being tilted a little, or an object being located in a different region than what the training data had seen).

	NOTE: Convolution & Pooling Techniques are used as a Combination in the CNN. Such that, we can repeat both many no. of times again & again in the Neural Network.

#### Flattening Layer

- In this, we simply just Flatten & Join each and every Pooled Matrix.

- After Flattening we simply take it as an Input Layer to the Dense Layered Neural Network just like we had in the ANN.

- For Example,

	Following are the Pooled Matrices:

	[[5, 6],	    [[2, 8],	    [[7, 9],
	[8, 3]]		[1, 6]]		[3, 4]]

	***Input Layer:***
	[5, 6, 8, 3, 2, 8, 1, 6, 7, 9, 3, 4]

### Recurrent Neural Network (RNN)

#### Need for RNN:

Before RNN,  we were using Machine Learning Models like Naive Bayes, Ensemble Techniques, etc. along with the use of some techniques which helps us in converting the Textual Data to Numeric/Vector Space Data to make them ready for Modelling.
But in that way, we were not able to store the Semantic Information of the Text nor we were getting good results in ***Machine Translation / Virtual Assistants*** because the Machine was not able to understand the flow to write/generate text.

So, to solve this, RNN was introduced which helps in handling the Sequence Data & store the Semantic Information.
#### Forward Propagation Over Time

We have an input which can have any number of dimensions or any number of features.
As RNN is especially designed to work on Sequential Data, therefore here we will discuss RNN with respect to a Sentence.

Now, let's take an example of Solving a problem for Sentiment Analysis.

Input will definitely be a Sentence having multiple Words and as we Tokenize each Sentence. We will have multiple Features/Dimensions at each record of the Dataset.

Let's say,
Sentence 1 - The food is bad

So, after converting text to numbers there will be four dimensions for this record which will account for the Sentence 1.

In Simple Neural Networks, if we recall we used to decide the number of neurons for the Input Layer based on the No. of Dimensions. And in the end after the Output layer, we used to get a Final Output.
But, in RNN, we process 1 Dimension/Feature at a time and therefore for RNN to complete training for 1 Record of the Dataset, it will have to complete training for each Dimension/Feature of that Sentence/Record.
Like in our case, for Sentence 1, it will run 4 Times.

Also in RNN, apart from the final output which we get from the Output Layer, we also get another output which summarizes the RNN Learning for that Token and is being provided again to the RNN for the next Token's Training. This helps in securing the Sequential Information of the Sentence as a whole.

***Important Point to Note here is that, for each Sentence we Train only 1 RNN but that 1 RNN is actually trained 4 times for each Token of the Sentence with same Hidden Layer Neurons, same Weights and same Activation Functions.***

Let's now have a detailed discussion on the Forward Propagation Over Time of RNN for Sentence 1

Sentence 1 = The + food + is + bad

X_1 = X_11 + X_12 + X_13 + X_14

RNN Architecture:

	Input --> Hidden Layer --> Output Layer

Aliases:
- W -> Weight which is between the Input & the Hidden Layer.
- W' -> Weight which gets multiplied with the Output of the Previous Tokens Final Output.
- W" -> Weight which is between the Hidden Layer & the Output Layer.
- Ot -> Output for the time i.e. (O1, O2, O3, ..., Ot)
- t -> Time
- Fnc -> Activation Funcion

As we have 4 Dimensions for the Sentence 1 therefore, we will run Forward Propagation 4 times for each token.

For t = 1
	O1 = Fnc((X11 * W) + (O0 * W'))

For t = 2
	O2 = Fnc((X12 * W) + (O1 * W'))

For t = 3
	O3 = Fnc((X13 * W) + (O2 * W'))

For t = 4
	O4 = Fnc((X14 * W) + (O3 * W'))

After the Training is done for all the 4 Tokens till t=4, we will proceed towards the Output Layer where the O4 will be multiplied with W" and an Activation Function will be applied such as Sigmoid or Softmax or any other Activation Function which will classify the Output and give us the final output i.e. Y^.

Note:
- There are various ways to initialize weights (W, W')
- O0 is just a Zero Padded Values Matrix or Some Random Initialized Values Matrix such that the Flow for the calculation of the Output for each token doesn't change.
#### Back Propagation Over Time

Backpropagation is similar to what we had discussed in ANN's Back Propagation [[#Back Propagation]]

Here also, using the Chain Rule of Differentiation we will be calculating the Derivation for each Weight that we used in Forward Propagation & then will Subtract the Derivation of the Weight from the Old Weight to get the New Weight Value.

Like to update W":
(Derivative of Loss w.r.t. Derivative of W") = [(Derivative of Loss w.r.t. Derivative of Y^) * (Derivative of Y^ w.r.t. Derivative of W")]

Similarly to Update W for t=4:
(Derivative of Loss w.r.t. Derivative of W) = [(Derivative of Loss w.r.t. Derivative of Y^) * (Derivative of Y^ w.r.t. Derivative of O4) * (Derivative of O4 w.r.t. Derivative of W)]

But here also we face the Vanishing Gradient Problem which we also faced in ANN & discussed thoroughly. [[#Vanishing Gradient Problem / Gradient Saturation / Gradient Dispersion]]

To solve this problem in RNN, researchers came up with Long Short Term Memory (LSTM) Architectures.

### Long Short Term Memory (LSTM)

Refer [[Understanding LSTM Networks (Colah's Blog).pdf]]

Important Pointers:
- An LSTM cell does indeed have gating mechanism. It includes three gates: the forget gate, update gate, and the output gate.
- An LSTM is similar to an RNN layer except that the RNN cells are replaced with LSTM cells.
- An LSTM does have an explicit cell state.
- An RNN does allow for an easier flow of gradients called as the ‘constant error carousel’.
- The LSTM cell is able to solve the problem of vanishing gradients because the Gradient is propagated from the cell state ct to the previous cell state ct−1 without any weights involved directly between ct and ct−1 which ensures that at least some gradient is always propagated **backwards in time**
---

Understand about Network Architectures:
1. AlexNet
2. VGGNet/ GoogleNet
3. Inception Network
4. ResNet
5. Siamese
6. SSD/ Yolo

Transfer Learning can be used when:
- We have a massive dataset in one domain and a smaller dataset in other similar domain.
- We have a pre-trained model in one domain and a massive dataset in other similar domain
- We have a pre-trained model in one domain and a smaller dataset in another similar domain
