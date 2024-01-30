from langchain_community.chat_models import ChatOpenAI

_model = ChatOpenAI(openai_api_key="",
                    temperature=0)

chain = _model
