import praw
from transformers import pipeline

#take the input user name, here my username was used due to script API
user=input()
user=str(user)

#Initializing the API
reddit = praw.Reddit(
    client_id="My Client ID was used",
    client_secret="My secret key was used",
    user_agent="any agent is fine",
)

#This creates a read-only instance as for editing, you will need username and password
reddit.read_only
user = reddit.redditor(user)

#Compile the data needed
posts = [post.title + " " + post.selftext for post in user.submissions.new(limit=100)]
comments = [comment.body for comment in user.comments.new(limit=100)]
complete_text="\n".join(posts + comments)

#Summarizing the complete data compiled
summarization = pipeline("summarization", model="facebook/bart-large-cnn")

max_chunk_length = 1024

# Split the complete_text into chunks so as to suite the model 
chunks = [complete_text[i:i + max_chunk_length] for i in range(0, len(complete_text), max_chunk_length)]

summaries = [summarization(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] for chunk in chunks]

# Combining the summaries
summary_text = " ".join(summaries)

#The prompt to be given to the LLM
prompt=f"""From the following text, generate a user persona:
{summary_text}

    - Personality traits
    - Interests
    - Occupation (if identifiable)
    - Political / philosophical views
    - Writing style
    - Hobbies
    Also cite relevant lines from the data used for each trait."""

#Generating the persona using LLM
llm= ChatGroq(temperature=0, groq_api_key="My API", model_name="llama-3.3-70b-versatile" )
result=llm.invoke(prompt)

#Creating the ouput text file
with open("_persona.txt", "w", encoding="utf-8") as f:
  f.write(result.content)




