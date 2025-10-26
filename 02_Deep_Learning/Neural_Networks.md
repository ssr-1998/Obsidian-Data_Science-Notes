
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
8. [[#Types of Optimizers]]
9. [[#CNN]]
10. [[#Recurrent Neural Network (RNN)]]
11. [[#Long Short Term Memory (LSTM)]]

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

[[Loss_&_Cost_Functions]]
### Types of Optimizers

[[Optimizers]]
### CNN

[[Convolutional_Neural_Networks]]
### Recurrent Neural Network (RNN)

[[Recurrent_Neural_Networks]]
### Long Short Term Memory (LSTM)

[[Long_Short_Term_Memory]]

---
