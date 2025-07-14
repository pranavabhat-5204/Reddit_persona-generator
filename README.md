# Reddit_persona-generator

So I completed the tasks in 3 steps:
1. Post and Comment extraction
2. Text summarization so that the LLM's Rate limit is not exceeded for the free version
3. Persona generation using ChatGroq

Required libraries:
Pip install praw, transformers, from langchain_groq import ChatGroq

1. Post and Comment extraction
For this you just have to enter the input user name along with the developer's ID and secret key.
I have kept the limit to the latest 100 posts and 100 comments as I have to capture's user's latest persona. This also uses less time during future steps.

2. Text summarization
I had to add this step to capture more information. Because to use this complete data without summarization is not possible under my Chatgroq free API plan. So this step gives the better persona generation but takes about 6 mins to run in my 16GB Ryzen 7 integrated processor.
This gives the most important features of the text.

3.Persona generation using ChatGroq
Here you need to put the Chatgroq API and connect to this LLM using Langchain. The summarized text is included with a prompt made for persona generation. This should be run to give the output text.
This text is saved into a text file which is attached as output


   
