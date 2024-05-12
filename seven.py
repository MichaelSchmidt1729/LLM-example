from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')


embedding_provider = OpenAIEmbeddings(
    openai_api_key=openai_api_key
)

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url="bolt://34.234.223.41:7687",
    username="neo4j",
    password="east-rubber-retailer",
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)

result = movie_plot_vector.similarity_search("A movie where aliens from Mars land and attack earth.", k=4)
for doc in result:
    print(doc.metadata["title"], "-", doc.page_content)