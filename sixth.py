from langchain_community.graphs import Neo4jGraph
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
url = os.getenv('URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

graph = Neo4jGraph(
    url=url,
    username=username,
    password=password
)

result = graph.query("""
MATCH (m:Movie{title: 'Apollp 13'}) 
RETURN m.title, m.plot, m.poster, m.released
""")

print(result)
print(graph.schema)