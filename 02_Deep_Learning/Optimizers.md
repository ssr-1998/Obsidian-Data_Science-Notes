
# Index
1. [[#Types of Optimizers]]
	- [[#Gradient Descent / Batch Gradient Descent]]
	- [[#Stochastic Gradient Descent]]
	- [[#Mini-Batch Stochastic Gradient Descent]]
	- [[#Mini-Batch SGD with Momentum]]
	- [[#AdaGrad (Adaptive Gradient Descent)]]
	- [[#Adadelta & RMSPROP]]
	- [[#Adam Optimizer]]

# Types of Optimizers

## Gradient Descent / Batch Gradient Descent

- Trains the Neural Network for all the no. of records in a Single Batch whether the dataset consists of 1K records or 1000K records.

- Therefore, to load & train such heavy dataset in a single go, it requires Huge Amount of RAM or maybe GPUs as well.

- That's why its biggest Disadvantage is that it Resource Extensive.

## Stochastic Gradient Descent

- Trains the Neural Network for one record at a time.

- Due to which, Huge RAM issue which we were having for Batch Gradient Descent won't arise here.

- But, it will now have to perform Huge No. of Iterations for each record to be trained, which will definitely take very long time & thus Convergence will be very slow.

## Mini-Batch Stochastic Gradient Descent

- We get to select the no. of records we want to Train in a single Batch i.e. Batch Size.

- Therefore, it is Resource Intensive.

- Convergence will be Better.

- Time Complexity will Improve.

- Still it has Noise while jumping to the next appropriate Weight in Gradient Descent Curve.

## Mini-Batch SGD with Momentum

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

## AdaGrad (Adaptive Gradient Descent)

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

## Adadelta & RMSPROP

- To overcome the disadvantage of Adagrad i.e. chances of making negligible changes to the (Learning Rate with eta).

- For this, we will apply Exponential Weighted Average in (Learning Rate with eta) formula as well. Which will then help us to control the rate of changes to the (Learning Rate with eta).

- formula for Weight updating: W_t = W_(t - 1) - ((Learning Rate with eta) \* (Derivative of Loss w.r.t. Derivative of [Old_Weight or W_(t - 1)]))

	(Learning Rate with eta) = (Learning Rate) / SQRT(S_dw_t i.e. Smoothed Value of Derivative w.r.t. t + Epsilon)
		where,
		- Epsilon is a small number such that if Alpha_t or (Alpha w.r.t. t) becomes 0, the denominator should not become 0 & should not make the output as Infinity.
	
	S_dw_t = (Beta \* (S_dw_(t - 1))) + ((1 - Beta) \* (Derivative of Loss w.r.t. Derivative of W_(t - 1)))
		where, t refers to all the previous versions of Currently Updating Weight.

- (Disadvantage) Doesn't have the Smoothing Weight Updating Technique.

## Adam Optimizer

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
