from langchain_community.graphs import Neo4jGraph


graph = Neo4jGraph(
    url="bolt://34.234.223.41:7687",
    username="neo4j",
    password="east-rubber-retailer"
)

result = graph.query("""
MATCH (m:Movie{title: 'Toy Story'}) 
RETURN m.title, m.plot, m.poster
""")

print(result)
print(graph.schema)