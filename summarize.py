import os 
import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
import getNews


os.environ["OPENAI_API_KEY"] = constants.APIKEY

def summarizeNews(link): #Summarizes the news article using Vector Indexes
    body = getNews.getnews(link)[1] #I have seperated the getnews function for code organisation
    with open('context.txt', 'w') as file:
        file.write(body)
    loader = TextLoader("context.txt")
    index = VectorstoreIndexCreator().from_loaders([loader])

    return str(index.query("Please summarise the text given", llm = ChatOpenAI()))
