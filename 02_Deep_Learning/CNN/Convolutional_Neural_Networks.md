
# Index
1. [[#CNN vs Human Brain]]
2. [[#Convolution Operation]]
	- [[#Pointers on Image Data]]
	- [[#Step 1 Min Max Scaling]]
	- [[#Step 2 Convolution, Filters & Stride]]
	- [[#Step 3 Padding]]
3. [[#Pooling]]
4. [[#Flattening Layer]]

# CNN vs Human Brain

- In Human Brain, there is a part named Cerebral Cortex which consists of another part of the part that is named as Visual Cortex.

- Visual Cortex is responsible for receiving, segmenting & integrating of Visual Information which it receives from the Retina.
	The Processed Information of Visual Cortex is subsequently sent to other regions of the Brain to be Analyzed & Utilized.
	There may be Multiple Layers of Visual Cortex in Cerebral Cortex that are responsible for performing many different actions like detection of moving objects, type of beings and many other things.

## Convolution Operation

- Multiple Steps are performed under the Convolution Operation. We will discuss each one by one.

### Pointers on Image Data

- Any image is of two type either `Black & White` or `RGB i.e. Red-Green-Blue`.

- Images contain Multiple Pixels & each Pixel ranges between 0 to 255.
	0 refers to Black
	255 refers to White

- For `Black & White` Image, the image size is represented as 5x5 i.e. 5 rows & 5 columns of a matrix each representing a pixel.

- For RGB Image, the Image Size is represented as 5x5x3 i.e. 5 rows, 5 columns & 3 Channels (Red-Green-Blue).

### Step 1: Min Max Scaling

- `Min Max Scaling` is applied on the Input Image which converts each pixel value between 0 to 1 by dividing each Pixel Value by 255.

### Step 2: Convolution, Filters & Stride

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

### Step 3: Padding

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

# Pooling

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

# Flattening Layer

- In this, we simply just Flatten & Join each and every Pooled Matrix.

- After Flattening we simply take it as an Input Layer to the Dense Layered Neural Network just like we had in the ANN.

- For Example,

	Following are the Pooled Matrices:

	[[5, 6],	    [[2, 8],	    [[7, 9],
	[8, 3]]		[1, 6]]		[3, 4]]

	***Input Layer:***
	[5, 6, 8, 3, 2, 8, 1, 6, 7, 9, 3, 4]
