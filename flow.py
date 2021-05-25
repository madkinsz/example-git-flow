from prefect.hello_world import hello_flow
from prefect.storage import GitHub

hello_flow.storage = GitHub(repo="madkinsz/example-git-flow", path="flow.py")

# To register flow, run: `prefect register -p flow.py --project default`
