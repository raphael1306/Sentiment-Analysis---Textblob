from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt')

url = 'goodnewspilipinas.com/overseas-filipino-nurse-dan-lester-dabon-named-top-100-healthcare-leader/'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)