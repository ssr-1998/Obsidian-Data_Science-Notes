
Important Topics to Cover:

- POS (Part-Of-Speech) Tagging

- Hidden Markov Model

- Parsing

	- Constituency Parsing

	- Dependency parsing

- Named Entity Recognition (NER) Tagging

	- IOB Labelling

	- Custom NER

		- Conditional Random Field (CRF)

		- Sequence Labelling

### What is Syntactic Processing

***It is a subset of NLP that deals with the syntax of the language.***

**Syntax**: A set of rules that govern the arrangement of words and phrases to form a meaningful and well-formed sentence.

Arrangement of words in a sentence plays a crucial role in better understanding the meaning of the sentence. These arrangements are governed by a set of rules that we refer to as ‘syntax’, and the process by which a machine understands the syntax is referred to as ***Syntactic processing***.

### How Syntactic Processing is more advance than Lexical Processing

To understand this, let's take the help of below specified three Example Sentences:

- Is EdTech UpGrad company an.

- EdTech is an company UpGrad.

- **UpGrad is an EdTech Company.**

All of these sentences have the same set of words, but only the third one is syntactically or grammatically correct and comprehensible. 

One of the most important things that you need to understand here is that in Lexical Processing, all of the three sentences provided above are similar to analyze because all of them contain exactly the same tokens, and when you perform Lexical Processing steps such as stop words removal, stemming, lemmatization and TFIDF or countvectorizer creation, you get the same result for all of the three sentences. The basic Lexical Processing techniques would not be able to identify the difference between the three sentences.
Therefore, more sophisticated Syntactic Processing Techniques are required to understand the relationship between individual words in a sentence.

### Parts-Of-Speech & POS Tagging

To understand POS Tagging, we must know Parts Of Speech.

`Parts Of Speech` are basically the Tags, we can assign to each word in a Sentence which specify the Role of each Word in the Sentence. Like, `Parts of Speech` such as Noun, Verb, Adjective, Adverb, etc.

These Parts of Speech Tags when are assigned to each Word in a System are then called POS Tags that help Machine to understand the Role / Relevance of each word in the Sentence.

For Example,

"People elected Joe Biden to lead USA"

Here, `Lead` is used in the Sentence. Generally, Lead has two Pronunciation & Meanings i.e.

- Lead -> Metal
- Lead -> Leadership

For a Machine, word Lead can mean anything. As it doesn't have the knowledge to distinguish among the two meanings.
So, to make it Distinguish among the two, we use POS Tags.

POS Tags will enable Machine to learn the Role of the Word in a Sentence.

> POS Tags are defined based on how they relate to the Neighboring Words.

#### Major POS Tags in the English Language

1. Open Class: These are Open Class because New Words are added everyday under below Tags. Like Google was not a Verb two Decades ago, but now we use Google as a Verb almost everyday.
	1. Noun
	2. Verb
	3. Adjective
	4. Adverb
	5. Interjection
2. Closed Class: There fall under Closed Class as no new numbers for Numerals or new Determiners are introduced everyday or even every Year. These will have Fixed Items for almost a Century or more.
	1. Proposition
	2. Pronoun
	3. Numerals
	4. Conjunction
	5. Articles
	6. Determiners


