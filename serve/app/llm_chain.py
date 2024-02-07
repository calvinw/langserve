from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import  FewShotChatMessagePromptTemplate
import os
from data_utils import read_csv_to_dicts
from models import OPENAI_MODEL

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

model = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],
                   model=OPENAI_MODEL,
                   temperature=0)

chain = final_prompt | model
