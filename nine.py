from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

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