from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Give 5 ficticious names of a company that makes {text}.",
        ),
        ("human", "{text}"),
    ]
)

_model = ChatOpenAI(openai_api_key="")

chain = _prompt | _model
