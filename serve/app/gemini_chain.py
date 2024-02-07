from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import  FewShotChatMessagePromptTemplate
import os

from data_utils import read_csv_to_dicts

from models import GOOGLE_MODEL

# Lets read the training for our few shot examples
examples = read_csv_to_dicts("app/training_data.csv")

# This is a prompt template used to format each individual example.
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Here are some examples for you to follow. Only give the answer in the format like in these examples. Do not try to answer the question, just return the formatted string."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

model = ChatGoogleGenerativeAI(model=GOOGLE_MODEL,
                              convert_system_message_to_human = True,
                              temperature=0.0,
                              google_api_key=os.environ["GOOGLE_API_KEY"])

chain = final_prompt | model
