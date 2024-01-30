from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

_prompt = ChatPromptTemplate.from_messages(
    [
      ("system", """Identify values of x, mu and sigma in following expression:
                    '{text}'
                    Your goal is to return a string to be used in an URL.
                    Dont try to answer the question asked in the text, just identify the value of x, mu and sigma and return the string as follows:

                    x=<<x>>&mu=<<mu>>&sigma=<<sigma>>

                    where you replace <<x>> with the value of x
                    where you replace <<mu>> with the value of mu
                    where you replace <<sigma>> with the value of sigma

                    mu is sometimes called the mean
                    sigma is sometimes called the standard deviation
                 """
      ),
      ("human", "{text}"),
    ]
)

_model = ChatOpenAI(openai_api_key="",
                    temperature=0)

chain = _prompt | _model
