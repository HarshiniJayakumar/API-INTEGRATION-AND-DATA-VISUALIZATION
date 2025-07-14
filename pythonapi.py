import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import collections
from textblob import TextBlob
from datetime import datetime, timedelta
 
api= "1c66e5044da04d70be2523b0f093b0df"

#Available countries
countries= {
    "ae": "UAE", "ar": "Argentina", "at": "Austria", "au": "Australia", "be": "Belgium", "bg": "Bulgaria",
    "br": "Brazil", "ca": "Canada", "ch": "Switzerland", "cn": "China", "co": "Colombia", "cu": "Cuba",
    "cz": "Czech Republic", "de": "Germany", "eg": "Egypt", "fr": "France", "gb": "United Kingdom", "gr": "Greece",
    "hk": "Hong Kong", "hu": "Hungary", "id": "Indonesia", "ie": "Ireland", "il": "Israel", "in": "India",
    "it": "Italy", "jp": "Japan", "kr": "South Korea", "lt": "Lithuania", "lv": "Latvia", "ma": "Morocco",
    "mx": "Mexico", "my": "Malaysia", "ng": "Nigeria", "nl": "Netherlands", "no": "Norway", "nz": "New Zealand",
    "ph": "Philippines", "pl": "Poland", "pt": "Portugal", "ro": "Romania", "rs": "Serbia", "ru": "Russia",
    "sa": "Saudi Arabia", "se": "Sweden", "sg": "Singapore", "si": "Slovenia", "sk": "Slovakia", "th": "Thailand",
    "tr": "Turkey", "tw": "Taiwan", "ua": "Ukraine", "us": "United States", "ve": "Venezuela", "za": "South Africa"
}
nametocode = {}
for k,v in countries.items():
    nametocode[v.lower()]=k
print("Available countries:\n", "  ".join(countries.values()))
country= input("Enter the country: ").strip().lower()
keyword = input("Enter a keyword (e.g. petrol, politics, weather): ").strip().lower()

if country not in nametocode:
    print("Country not here.")
    exit()
else:
    code = nametocode[country]
    
#Fetching top headlines
url = f"https://newsapi.org/v2/top-headlines?country={code}&apiKey={api}"
response = requests.get(url)
print("Response:",response.status_code)
data = response.json()
articles = data.get("articles", [])

#Fallback:Using Keyword
if not articles and keyword:
    print("No Top Headlines")
    print("Searching for the Keyword globally")
    url = f"https://newsapi.org/v2/everything?q={keyword}&sortBy=popularity&apiKey={api}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])

if not articles:
    print("Articles not found.")
    exit()

print("\n Headlines:")
for i, article in enumerate(articles[:5], 1):
    print(f"{i}. {article['title']}")
    print(f"Sources:{article['source']['name']}")
    print(f"URL:{article['url']}")

sources=[]
for article in articles:
    sourceandname=article['source']['name']
    sources.append(sourceandname)
source_count = collections.Counter(sources)


#Sentiment Analysis
df = pd.DataFrame(articles)
df['publishedAt'] = pd.to_datetime(df['publishedAt'])
df['title'] = df['title'].fillna('')
df['sentiment'] = df['title'].apply(lambda x: TextBlob(x).sentiment.polarity)
def sentimenttype(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['type_of_sentiment'] = df['sentiment'].apply(sentimenttype)
sentiment_counts = df['type_of_sentiment'].value_counts()


print("\n Keyword trend over last 10 days")
start_date = datetime.now() - timedelta(days=10)
all_articles = []
for i in range(10):
    day = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
    url = f"https://newsapi.org/v2/everything?q={keyword}&from={day}&to={day}&sortBy=popularity&apiKey={api}"
    response = requests.get(url)
    data = response.json()
    for article in data.get("articles", []):
        article['day'] = day
        all_articles.append(article)

if not all_articles:
    print(" Articles not found for the keyword over last 10 days.")
    exit()

df_trend = pd.DataFrame(all_articles)
df_trend['day'] = pd.to_datetime(df_trend['day'])
df_trend['title'] = df_trend['title'].fillna('')
df_trend['sentiment'] = df_trend['title'].apply(lambda x: TextBlob(x).sentiment.polarity)
df_trend['type_of_sentiment'] = df_trend['sentiment'].apply(sentimenttype)

daily_counts = df_trend.groupby('day').size().reset_index(name='count')
overall_sentiment_analysis = df_trend['type_of_sentiment'].value_counts()

fig,axs=plt.subplots(2,2,figsize=(16,10))

#Bar plot of source count
x=list(source_count.values())
y=list(source_count.keys())
sns.barplot(x=x, y=y,ax=axs[0,0],legend=False)
axs[0,0].set_title("Reports  from source")
axs[0,0].set_xlabel("Count")
axs[0,0].set_ylabel("Source Name")

#Bar Plot of Sentiment analysis of News Headlines
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values,ax=axs[0,1])
axs[0,1].set_title("Sentiment Analysis of News Headlines")
axs[0,1].set_xlabel("Sentiment")
axs[0,1].set_ylabel("Number of Articles")

#Line plot of keyword trend over last 10 days
axs[1,0].plot(daily_counts['day'],daily_counts['count'],marker='o',color='purple')
axs[1,0].set_title(f"Keyword: '{keyword}' trend over Last 10 Days")
axs[1,0].set_xlabel("Date")
axs[1,0].set_ylabel("Mentions")
axs[1,0].tick_params(axis='x',rotation=45)
axs[1,0].grid(True)

#Pie chart for overall sentiment
axs[1,1].pie(overall_sentiment_analysis.values,labels=overall_sentiment_analysis.index,autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral', 'lightgray'])
axs[1,1].set_title(f"Overall Sentiment analysis for '{keyword}'")
axs[1,1].axis('equal')

plt.tight_layout()
plt.show()
















