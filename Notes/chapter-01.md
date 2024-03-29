<strong>
<p align="justify">

# Natural Language Processing

<img width="40%" src="./../imgs/nlp_venn-diagram.png"/>


- NLP stands for Natural Lanhguage Processing. It is a branch of Computer Science and more specifically the branch of AI concerned with giving comuters the ability to understand text and spoken words in much the same way as Human beings can.
- NLP has two components:
  
  - NLU (Natural Language Understanding) - To interpret the statements and understand it's meaning
  - NLG (Natural Language Generation) - To Generate text and speech, after understand a certain given input

- NLP is about chacterizing, categorizing, comparing, converting and creating  any output suh as words, characters, sentences, documents and conversations or bringing out conclusions from them.
- There's a huge demand in the next few years to scale the existing solutions and to create new solutions for all wwalks of life.
- NLP is sppreadheading the move towards Genral Purpose Technology(GPT) and Artificial General Intelligence(AGI).
- NLP techniques like transformers and Attention are finding applications in other research areas.

- So, basically working with text data has 3 types of Machine Learning Lagorithm associated with it:

  - Natural Language Processing
  - Deep Learning
  - Deep Natural Language Processing

    - Sequence-to-Sequence

- Sequence-to-Sequence models are the most cutting edge, the most powerful models that exist right now for natural language processing, and that's what we will be looking at in the content ahead.

<hr>

### Classical vs Deep Learning Models

- Let's understand this with some examples:

  - If/Else Rules (Chatbot): It's a clear part of NLP. What they entail is a huge list of possible questions and answer to those questions and so once, somebody in the chat, ask that question or we can identify that part of the sentence in the question in the question we have recorded. Then we will give them the correct answer , the answer that is associated with the question.

  - Speech Recognition (Audio Frequency Components Analysis): In essence, what happens is we look at the sound wave of somebody talking, some pre-recorded or some real time audio over human speech, and then we try to identify what waveforms exist in there. This is again a key example of Natural Language Processing.

  - Bag of Words Model (Classification): It is a very popular approach for text analysis or Natural Language Processing. It can be a example for either NLP or DNLP as well. What it does is, there's a bag of words, and for instance, we might have a lot of texts. So, it matches the occurance of certain keyword with either it being a positive result or a negativve result. As a result the model will be able to classify the outcome based on positive or negative result inferred by the text.

  - CNN for Text Recognition (Classification): It is a pretty good example of DNLP model. This method uses Neural Networks for Text recognition and hence used for text processing. So, the way it works is, the words are transformed into matrix and that's done through an operation called embedding of words. And then once they are in a matrix, same principles that apply to image processing using CNNs are applied here. Then they are pooled, max pooled and min pooled their smaple abd then they're flattened and then we have the prediction.

<hr>

### End-to-End Deep Learning Models

- The reason why we are diving into this area is, it will help us understand why Seq2Seq are actually so good because Seq2Seq models are type of End-to-End Deep learning models.
- To understand what's a end-to-end deep learning model, consider this example. Let's say we have a customer calling to the customer centre, the customer is responded by a Voice-based Chatbot that listens to the user input and processes the speech and converting it into text and than the text query is processed by another ML algorithm and it sends the respond back to the Speech Recognition Model and provides the response to the customer by converting text response to speech. This is a pretty good example of end-to-end deep learning model, as it involves use of 2 ML Models, to complete the flow and clearly there's a huge majority that the response might not be correct because, there's a misconnect b'w the 2 ML algorithms used in this case.

- It's not 1 algorithm doing all the thing, and there are 2 algorithms with it's training happening seprately, we will run into problems, not nessecarily all the time, but it does happen quite sometime.

<hr>

### Bag of Words Model

- So. let's assume an example, where a guy writes us a email asking, if we are back. The Wikipedia says in general a human uses only 3000 words out of almost 1.7 lakh words only at an average, assuming we use 20000 of the words, we categorize the words as SOS(Start of Statement), EOS(End of Statement), general words and than the remaining are special words.
- So, let's assume that these 20,000 words are represented by an array or list of size 20,000. and we convert the sentence we recieved in the mail to a vector. Now our model needs to be trained to a dataset where for every statement is tested against it's response.

- Now, once we have the data ready we're going to apply a model to create our bag of words. One of the models we can apply here to create our bag of words is logisitic regression. Once trained, it's likely that the model can yeild, what's likely to yield a yes, and what is likely to be a no. This is a NLP based approach.
- Also, instead of a logisitc regression we can use a Neural Network cause we have a vector of 20,000 words, we can feed them as input to the input layer and obtain the output accordingly. This is an example of DNLP approach.

<hr>

### Seq2Seq Architecture

- Before, diving deep into the Seq2Seq Model, we shoudl know about the issues with Bag of Words Model:

  - Fixed Size Input - The Test data must have size same as that of the training data.
  - Doesn't take word order into account.
  - Fixed Size Output

- The Solution to the problem is Recurrent Neural Networks. RNNs are of various types:

  - one-to-one
  - one-to-many
  - many-to-one
  - many-to-many

- Here every single box is not one cell, it's actually a whole layer of neurons is represented by a single box. when working with a quite a huge text, than in such case many-to-many RNNs are the most effective. Because every time we will have a variable length input, and hence a variable length output.
- To understand this better, let's move back to the understanding the approach back. Let's suppose the sentece is "Hello Kirill, Checking if you are back to  Oz.". So, what we are gonna do is, we take each signle word, and we code them. So, we're going to create a different route this time. One way to create it is we take those from that big vector of 20,000, and we only take the position of every word i.e. what is the position of those words in that collection of 20,000 words. This is how we construct the vector and the length of vector depends on the number of words in the input text.

  <img width="50%" src="../imgs/seq2seq_1.png"/>

- So, we're going to create our neural network with the text. But just keep in mind that in a machine sense, we do need to have numbers and it is possible to construct the vector of numbers from our email. And the vector size would be the same as the length of the mail. It will have SOS at the start and EOS at end. We drop SOS becuase, it's not that important. every sentence will start with SOS. While EOS is important because it will dictate that the output will terminate. So, now what we will do is we wil feed these values into our RNN.

- As soon as we would encounter an EOS. It will start to process the statement. As it is a RNN, we can feed in any number of words. The inputs here are like parameters in the algorithm which is adjusted to the length of our input. Once, it is done, the network is going to start predicting approach. So, for every predicition, there are 20,00 possible outcomes, here we mean to say that for every word there's a probability of (1/20000) of any word appearing in the output. So, the end result will spit out a probability score for the options that it has, and it assigns probabilities to different words that it can pick up, and than pick the one with highest probabilty. It's upto the Neural Network to generate the right response, based on the training it has been through. So, the output generaed goes as a feedback for the next output which is what actually happens in a LSTM based model. This will make sure we're taking into account not just a memory that's flowing through, but we're using the output we generated before and that will help us help the neural netowrk preserve understand the meaning.

  ![](../imgs/1600px-Long_Short-Term_Memory.svg.png)

- The Seq2Seq Model is based on Encoder-Decoder kind of architecture, where the input is encoded and the decoder decodes the upcoming response by taking the preceeding output as a feedback for the further output to be generated. So, basically we have 2 RNNs attached to each other.

<hr>

### Seq2Seq Training

  <img width="70%" src="../imgs/seq2seq_2.png"/>

- Now, we have got an encoder and decoder which resembles a RNN. The difference b/w training and applying is that in this case, there's a specific end result, with certain probability. For training, we look at similar different  sentences. And we will have a full response already provided, as we already know the end result and that will allow us to train the result.

- So, as the model gets trained, with the inputs, we need to update these parameters throught our training in order for neural network to learn from the training data by updating the weights. So, as soon as the input data is processed through training happening in a iterative process is going to look at different options that it can split out.

- So, through the process of back propagation, this Seq2Seq Model is going to make sure that the probablity of getting a certain word is highest at this certain position. And accordingly it's going to update the weights and parameters of the network. Than what happens next is, it moves to the next word in the sentence, and the preceeding output is given as feedback along with the next word in the sentence and accordingly another word will be chosen which has the highest probabilty to occur at that position and similarly this will continue untill the sentence is obtained.

<hr>

### Greddy Decoding

- We feed in the input to the network and then it produces the first word by picking up the one with highest probabilty. The next time it again picks up the next word with highest probabilty and this continues till EOS. And the reason it's called greedy is because every time we just  pick up the word with the highest probabilty.

<hr>

### Beam Search Decoding

- Instead of just looking at one word with the highest probability, rather we look at 3-5 words with highest probability of occuring at a certain position which is fed back to the algorithm, which again picks up 3-5 words with highest probability for each of the precceding outcome generated, we again feed it back to the neural network which again produces set of output with highest probaility for each of the precceding outcome and this is how we get the results.

  So, we pick up the most relevant outcome by looking at the highest joint probabilty across the whole bean or the branch with the highest score.

  The difference in this case is that in greddy algorithm, we don't even consider looking into other branches, and just go ahead with a single approach by only picking up the one's with highest probability and no other options. Here, in Beam Search Decoding, we don't give emphasis on individual score of a word, rather we focuse more on Overall Joint Probability.

  There's a method called `Truncating the Beams` where the algorithm simply stops looking at the joint/branch with lowest Joint Probabilty and just throws it away, and than only goes ahead with the branches with High Joint Probabilty.

<hr>

### Attention Mechanism
  <img width="70%" src="../imgs/seq2seq_3.png"/>

- So, before discussing about the Attention mechanism, let's first understand what's the flaws in the existing Seq2Seq Model. In the Seq2Seq, we feed in the data to the input Layers in the Neural network and than the input layer stores the complete infomation about the input and hence, in the last input layer of the Neural Network a lot of information is stored at once. And than it also, needs to be carried out to the further layers of the Neural Network so as to have the information processed.

- So, this approach looks good only for smaller texts, but as the text input grows longer this becomes more and more bulky process as the data needs to be stored and carried through each layer of the network. So, the attention mechanism is based on the fact that each decoder layer of the Neural Network decides which input needs to be given more weightage as it has the complete access of the data. And through the step called the `Softmax function` the weights are distributed and the sum of weights assigned to all the input parameters must equal 1. So, these weights are taken and we make something called `Context vector`. The Context Vector is obtained by mutiplying the weights with the value in each input neural network or vector and is done every time before giving the input to the next layer in the Neural network along with the feedback. And than we feed this Context Vector to the Decoding Layer, and than we get the output, this output ss given as feedback to the next layer in the neural network along with a reevaluated Context Vector and hence accordingly the final output is generated.

- The attention mechanism is a component in deep learning neural networks that allows the network to focus on specific parts of the input during processing. The idea is inspired by the way humans selectively focus on different parts of a scene when performing a task.

- In a neural network with an attention mechanism, the network learns to assign weights to different parts of the input, based on their relevance to the current task. These weights are then used to compute a weighted sum of the input, which forms the basis for further processing by the network.

- The attention mechanism is commonly used in natural language processing tasks, such as machine translation and language modeling. In these tasks, the attention mechanism allows the network to focus on different parts of the input sequence (e.g., words in a sentence) as it generates the output sequence.

- The attention mechanism has been shown to improve the performance of neural networks in a variety of tasks, by allowing them to selectively focus on the most important parts of the input.

</p>
</strong>
