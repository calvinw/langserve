from langserve.client import RemoteRunnable
runnable = RemoteRunnable("http://localhost:8000/company-name")

answer=runnable.invoke("dogs")
print(answer)
