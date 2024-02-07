from langserve.client import RemoteRunnable
from data_utils import read_csv_to_dicts

#chain = RemoteRunnable("http://localhost:8000/openrouter")
chain = RemoteRunnable("http://localhost:8000/openrouter")

# answer=chain.invoke({"input": "What is the value of z when x=3.3, the mean 4 and the standard deviatoin is 15"})
# print(answer.content)


questions = read_csv_to_dicts("app/test_data.csv")
#questions = questions[:10]

inputs = []
outputs = []

for item in questions:
  inputs.append({"input": item["input"]})
  outputs.append({"output": item["output"]})

responses=chain.batch(inputs)

for response in responses:
  print(response.content)

#
# # print(questions)
# # print(answers)
#
# # # Loop through the questions and print them one at a time
# for i in range(len(questions)):
#   if responses[i].content != outputs[i]["output"]:
#     print(inputs[i]["input"])
#     print("llm answer:")
#     print(responses[i].content)
#     print("correct answer:")
#     print(outputs[i]["output"])
#     print("--------------------------")
