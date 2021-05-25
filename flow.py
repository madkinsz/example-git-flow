from prefect.storage import GitHub
from prefect import task, Flow

@task(log_stdout=True)
def say_hello():
   print("Hello world!")

with Flow("hello-world") as flow:
   say_hello()

flow.storage = GitHub(repo="madkinsz/example-git-flow", path="flow.py", ref="self-defined-flow")

# To register flow, run: `prefect register -p flow.py --project default`
