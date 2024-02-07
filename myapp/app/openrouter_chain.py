from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import  FewShotChatMessagePromptTemplate

from data_utils import read_csv_to_dicts
from data_utils import convert_to_json

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

model = ChatOpenAI(
        temperature=0.0,
        #model="openchat/openchat-7b:free",
        model="mistralai/mistral-7b-instruct:free",
        openai_api_key='',
        openai_api_base="https://openrouter.ai/api/v1"
    )


chain = final_prompt | model
