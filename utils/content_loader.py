from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader
import requests

def load_web_content(url):

    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, 'html.parser')
    # text = ' '.join([elem.get_text() for elem in soup.find_all(['h1', 'h2', 'h3', 'p'])])
    # return text

    loader = WebBaseLoader(url)

    doc = loader.load()

    return doc
