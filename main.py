import os
import sys

import constants
from langchain.document_loaders import TextLoader
# from langchain.document_loaders import DirectoryLoader 
# Above line is for a whole directory
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import textNews
from textNews import getnews

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# while True:
#     query = input("Query: ")
#     if query.upper() != "EXIT":
#         loader = TextLoader("context.txt")
#         index = VectorstoreIndexCreator().from_loaders([loader])

#         print(index.query(query, llm = ChatOpenAI()))
#     else:
#         sys.exit()

link = input("Enter link to summarize: ")
body = textNews.getnews(link)[1]
print("\n------------------------------------------------\n")
with open('context.txt', 'w') as file:
    file.write(body)
loader = TextLoader("context.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query("Please summarise the text given in bullet points", llm = ChatOpenAI()))


