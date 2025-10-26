
# Index
1. [[#Need for RNN]]
2. [[#Forward Propagation Over Time]]
3. [[#Back Propagation Over Time]]

# Need for RNN:

Before RNN,  we were using Machine Learning Models like Naive Bayes, Ensemble Techniques, etc. along with the use of some techniques which helps us in converting the Textual Data to Numeric/Vector Space Data to make them ready for Modelling.
But in that way, we were not able to store the Semantic Information of the Text nor we were getting good results in ***Machine Translation / Virtual Assistants*** because the Machine was not able to understand the flow to write/generate text.

So, to solve this, RNN was introduced which helps in handling the Sequence Data & store the Semantic Information.
# Forward Propagation Over Time

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
# Back Propagation Over Time

Backpropagation is similar to what we had discussed in ANN's Back Propagation [[#Back Propagation]]

Here also, using the Chain Rule of Differentiation we will be calculating the Derivation for each Weight that we used in Forward Propagation & then will Subtract the Derivation of the Weight from the Old Weight to get the New Weight Value.

Like to update W":
(Derivative of Loss w.r.t. Derivative of W") = [(Derivative of Loss w.r.t. Derivative of Y^) * (Derivative of Y^ w.r.t. Derivative of W")]

Similarly to Update W for t=4:
(Derivative of Loss w.r.t. Derivative of W) = [(Derivative of Loss w.r.t. Derivative of Y^) * (Derivative of Y^ w.r.t. Derivative of O4) * (Derivative of O4 w.r.t. Derivative of W)]

But here also we face the Vanishing Gradient Problem which we also faced in ANN & discussed thoroughly. [[#Vanishing Gradient Problem / Gradient Saturation / Gradient Dispersion]]

To solve this problem in RNN, researchers came up with Long Short Term Memory (LSTM) Architectures.
