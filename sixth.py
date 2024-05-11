from langchain_community.graphs import Neo4jGraph

import os
from dotenv import load_dotenv
load_dotenv()
url = os.getenv('url')
username = os.getenv('username')
password = os.getenv('password')

graph = Neo4jGraph(
    url=url,
    username=username,
    password=password
)

result = graph.query("""
MATCH (m:Movie{title: 'Toy Story'}) 
RETURN m.title, m.plot, m.poster
""")

print(result)