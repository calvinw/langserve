from langserve.client import RemoteRunnable
from data_utils import read_csv_to_dicts

chain = RemoteRunnable("http://localhost:8000/together")

# answer=chain.invoke({"input": "What is the value of z when x=3.3, the mean 4 and the standard deviatoin is 15"})
# print(answer.content)


questions = read_csv_to_dicts("app/test_data.csv")

inputs = []
outputs = []

for item in questions:
  inputs.append({"input": item["input"]})
  outputs.append({"output": item["output"]})

#responses=chain.batch(inputs)

# print(inputs)
# print(outputs)

num_inputs=len(inputs)

for i in range(len(questions)):
    llm_response=chain.invoke(inputs[i])

    question = inputs[i]['input']
    output = outputs[i]['output']

    print(question)
    print(llm_response.content)
    print(output)
    print("--------------")
