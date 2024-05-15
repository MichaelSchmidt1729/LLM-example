from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

"""
load_dotenv(".env")
url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
embedding_model_name = os.getenv("EMBEDDING_MODEL")
# Remapping for Langchain Neo4j integration
os.environ["NEO4J_URL"] = url

logger = get_logger(__name__)

so_api_base_url = "https://api.stackexchange.com/2.3/search/advanced"

embeddings, dimension = load_embedding_model(
    embedding_model_name, config={"ollama_base_url": ollama_base_url}, logger=logger
)

# if Neo4j is local, you can go to http://localhost:7474/ to browse the database
neo4j_graph = Neo4jGraph(url=url, username=username, password=password)
"""

chat_llm = ChatOpenAI(openai_api_key=openai_api_key)

embedding_provider = OpenAIEmbeddings(openai_api_key=openai_api_key)

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    url="bolt://34.234.223.41:7687",
    username="neo4j",
    password="east-rubber-retailer",
    index_name="moviePlots",
    embedding_node_property="embedding",
    text_node_property="plot",
)

plot_retriever = RetrievalQA.from_llm(
    llm=chat_llm,
    retriever=movie_plot_vector.as_retriever()
)

result = plot_retriever.invoke(
    {"query": "A movie where a mission to the moon goes wrong with Tom Hanks"}
)

print(result)