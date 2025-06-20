Source: https://blog.dailydoseofds.com/p/11-essential-distributions-that-data
# Table of Contents:
1. [[#Data Types]]
	1. [[#Qualitative Data (Categorical Data)]]
		1. [[#Nominal Data]]
		2. [[#Ordinal Data]]
	2. [[#Quantitative Data (Numerical Data)]]
		1. [[#Discrete Data]]
		2. [[#Continuous Data]]
2. [[#Types Of Distributions]]
	1. [[#Normal Distribution (Gaussian Distribution)]]
	2. [[#Bernoulli Distribution]]
	3. [[#Binomial Distribution]]
	4. [[#Poisson Distribution]]
	5. [[#Exponential Distribution]]
	6. [[#Gamma Distribution]]
	7. [[#Beta Distribution]]
	8. [[#Uniform Distribution]]
	9. [[#Log-Normal Distribution]]
	10. [[#Weibull Distribution]]
# Data Types
Data types refer to the categories of data based on its characteristics, properties, and the type of information it represents.

There are mainly two Data Types:
1. Qualitative
2. Quantitative
## Qualitative Data (Categorical Data)
It is a non-numerical data and describes characteristics of an object, person, or phenomenon. It is often collected through Surveys, Interviews, Focus Groups, and Observations.

There are two sub-categories:
1. Nominal Data
2. Ordinal Data
### Nominal Data
Categorical Data or Categories that doesn't have any order / rank, comes under Nominal Data Category.
Examples: Gender (Male & Female), Marital Status (Single / Married / Divorced), and Occupation (Teacher / Engineer / Doctor)
### Ordinal Data
Categorical Data that has a natural order or ranking, but the differences between the categories are not equal, comes under Ordinal Data Category.
Examples: Education Level (High School / Diploma / Bachelor's / Master's) and Satisfaction Rating (Very Satisfied / Satisfied / Neutral / Dissatisfied)

## Quantitative Data (Numerical Data)
It is a numerical data and can be measured or counted. It provides insight into quantities, amounts, or magnitudes. Quantitative data is often collected through experiments, surveys, and sensors.

There are two sub-categories:
1. Discrete Data
2. Continuous Data
### Discrete Data
It refers to specific and distinct values that can be counted. The Binary Data comes under Discrete Data Category because it has only two possible values, often represented as 0 or 1, yes or no, or true or false.
Examples: Number of children in a family, Number of cars sold in a month, and Number of Days in a Month.
### Continuous Data
It can take any value within a certain range or interval. The Ratio and Interval Data comes under Continuous Data Category because both have equal intervals between consecutive values.
Examples: Height in meters (e.g., 1.5 m, 2.0 m, 2.5 m) & Temperature in Fahrenheit (e.g., 32°F, 64°F, 96°F).
# Types Of Distributions

![[Pasted image 20240910225417.png]]
## Normal Distribution (Gaussian Distribution)

![[Pasted image 20240910221729.png]]

- Uses Continuous Data
- Forms a Symmetric Bell-Shaped Curve
- It is parameterized by two parameters—mean and standard deviation.
- Example: Height of individuals.
## Bernoulli Distribution

![[Pasted image 20240910222004.png]]

- A Discrete Probability Distribution that models the outcome of a binary event.
- It is used in **Logistic Regression**.
- It is parameterized by one parameter i.e. the probability of success.
- Example: Modeling the outcome of a single coin flip.
## Binomial Distribution

![[Pasted image 20240910222132.png]]

- A discrete probability distribution that represents the number of successes in a fixed number of independent Bernoulli trials.
- It is a **Bernoulli Distribution** repeated multiple times.
- It is parameterized by two parameters—the number of trials and the probability of success.
## Poisson Distribution

![[Pasted image 20240910222325.png]]

- A discrete probability distribution that models the number of events occurring in a fixed interval of time or space.
- It is parameterized by one parameter—lambda, the rate of occurrence.
- Example: Analyzing the number of goals a team will score during a specific time period.
## Exponential Distribution

![[Pasted image 20240910222432.png]]

- A continuous probability distribution that models the time between events occurring in a **Poisson Distribution Process**.
- It is parameterized by one parameter—lambda, the average rate of events.
- Example: Analyzing the time between goals scored by a team.
## Gamma Distribution

![[Pasted image 20240910222539.png]]

- It is a variation of the exponential distribution.
- A continuous probability distribution that models the waiting time for a specified number of events in a Poisson process.
- It is parameterized by two parameters—alpha (shape) and beta (rate).
- Example: Analyzing the time it would take for a team to score, say, three goals.
## Beta Distribution

![[Pasted image 20240910222805.png]]

- It is used to model probabilities, thus, it is bounded between [0,1].
- Differs from Binomial in this respect that in Binomial, probability is a parameter.
- But in Beta, the probability is a random variable.
## Uniform Distribution

![[Pasted image 20240910222843.png]]

- All outcomes within a given range are equally likely.
- It can be continuous or discrete.
- It is parameterized by two parameters: a (minimum value) and b (maximum value).
- Example: Simulating the roll of a fair six-sided die, where each outcome (1, 2, 3, 4, 5, 6) has an equal probability.
## Log-Normal Distribution

![[Pasted image 20240910223007.png]]

- A continuous probability distribution where the logarithm of the variable follows a normal distribution.
- It is parameterized by two parameters—mean and standard deviation.
- Example: Typically, in stock returns, the natural logarithm follows a normal distribution.
## Weibull Distribution

![[Pasted image 20240910224543.png]]

- It is a Continuous Probability Distribution and models the waiting time for an event.  
- Often employed to analyze time-to-failure data.
- It is parameterized by two parameters i.e. the Shape Parameter (k) & the Scale Parameter (Lambda).
- The Probability Density Function of a **Weibull** Random Variable is given in the above image showing it's formula where shape & scale parameters are > 0.
- Examples: Maximum one-day rainfalls & the time a User spends on a Web Page.

***Next: Implementation of above listed Distributions in Jupyter Notebook.***
