import openai
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Define a prompt template for story generation
prompt_template = PromptTemplate(
    input_variables=["prompt"],
    template="Write a creative and engaging story based on the following prompt: {prompt}"
)

# Initialize the OpenAI language model
llm = ChatGroq(temperature=0, api_key="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", model_name="mixtral-8x7b-32768")

# Create an LLMChain for story generation
story_chain = LLMChain(prompt=prompt_template, llm=llm)

# Function to generate a story based on a given prompt
def generate_story(prompt):
    story = story_chain.run(prompt=prompt)
    return story

# Streamlit web interface
st.title("Story Generator")
st.write("Enter a prompt to generate a creative story:")

# Input prompt from user
user_prompt = st.text_input("Story Prompt", "")

# Generate story button
if st.button("Generate Story"):
    if user_prompt:
        story = generate_story(user_prompt)
        st.write("Generated Story:\n")
        st.write(story)
    else:
        st.write("Please enter a prompt to generate a story.")

# Run the Streamlit app
if __name__ == "__main__":
    st.write("Welcome to the Story Generator App! Enter a prompt above to get started.")