import requests
from newspaper import Article

session = requests.Session()

def getnews(article_url): #Returns the content of the article

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
    try:
        response = session.get(article_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
            return [article.title, article.text]
            
        else:
            print(f"Failed to fetch article.")
    except Exception as e:
        print(f"Error occurred while fetching article at {article_url}: {e}")
