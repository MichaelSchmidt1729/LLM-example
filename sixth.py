from langchain_community.graphs import Neo4jGraph
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
url = os.getenv('url')
username = os.getenv('username')
password = os.getenv('password')

graph = Neo4jGraph(
    url="bolt://34.234.223.41:7687",
    username="neo4j",
    password="east-rubber-retailer"
)

result = graph.query("""
MATCH (m:Movie{title: 'Apollp 13'}) 
RETURN m.title, m.plot, m.poster, m.released
""")

print(result)
print(graph.schema)