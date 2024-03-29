from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import  FewShotChatMessagePromptTemplate
import os

from data_utils import read_csv_to_dicts
from data_utils import convert_to_json

from models import TOGETHER_MODEL

# Lets read the training for our few shot examples
examples = read_csv_to_dicts("app/training_data.csv")

# This is a prompt template used to format each individual example.
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("user", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert at identifying the problem type in elementary statistics. Here are some examples of what you should do."),
        few_shot_prompt,
        ("user", "{input}"),
    ]
)

model = ChatOpenAI(
        temperature=0.0,
        model= TOGETHER_MODEL,
        openai_api_key=os.environ["TOGETHER_API_KEY"],
        openai_api_base="https://api.together.xyz/v1/"
    )


chain = final_prompt | model
