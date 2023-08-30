import os 
import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
import getNews


os.environ["OPENAI_API_KEY"] = constants.APIKEY

def summarizeNews(bullet, link): #Summarizes the news article using Vector Indexes
    try:
        body = getNews.getnews(link)[1] #I have seperated the getnews function for code organisation
        with open('context.txt', 'w') as file:
            file.write(body)
        loader = TextLoader("context.txt")
        index = VectorstoreIndexCreator().from_loaders([loader])

        if bullet:
            return str(index.query("Please summarise the text given in bullet point form", 
                                   llm = ChatOpenAI()))
        else:
            return str(index.query("Please summarise the text given", llm = ChatOpenAI()))
    except TypeError:
        return "I was unable to read that link. Did you put one in?"
