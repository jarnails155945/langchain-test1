from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

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

# Example usage
if __name__ == "__main__":
    user_prompt = "A young boy discovers a hidden world beneath his city."
    story = generate_story(user_prompt)
    print("Generated Story:\n")
    print(story)
