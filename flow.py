from prefect.hello_world import hello_flow
from prefect.storage import GitHub

hello_flow.storage = GitHub(repo="madkinsz/example-git-flow", path="flow.py")

if __name__ == "__main__":
   hello_flow.register("default")

