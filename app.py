import requests
import streamlit as st

class NewsAPI:
    def __init__(self):
        self.api_key = st.secrets["news_api_key"]
        self.base_url = "https://newsapi.org/v2/"

    def get_top_headlines(self, country='us', category=None):
        url = f"{self.base_url}top-headlines"
        params = {
            'apiKey': self.api_key,
            'country': country
        }

        if category:
            params['category'] = category
        response = requests.get(url, params=params)
        return response.json()
    
def get_everything(self, query, from_date=None, to_date=None, language='en'):
    url = f"{self.base_url}everything"
    params = {
        'apiKey': self.api_key,
        'q': query,
        'language': language
    }
    if from_date:
        params['from'] = from_date
    if to_date:
        params['to'] = to_date
    response = requests.get(url, params=params)
    return response.json()

def get_sources(self, category=None, language='en', country=None):
    url = f"{self.base_url}sources"
    params = {
        'apiKey': self.api_key,
        'language': language
    }
    if category:
        params['category'] = category
    if country:
        params['country'] = country
    response = requests.get(url, params=params)
    return response.json()

# Streamlit UI
st.title("News API Explorer")

news_api = NewsAPI()

st.header("Top Headlines")
country = st.text_input("Country Code", value='us')
category = st.text_input("Category (optional)")
if st.button("Get Top Headlines"):
    headlines = news_api.get_top_headlines(country, category)
    st.json(headlines)

st.header("Everything")

query = st.text_input("Query")
from_date = st.text_input("From Date (YYYY-MM-DD, optional)")
to_date = st.text_input("To Date (YYYY-MM-DD, optional)")
language = st.text_input("Language", value='en')
if st.button("Get Everything"):
    everything = news_api.get_everything(query, from_date, to_date, language)
    st.json(everything)

st.header("Sources")
category = st.text_input("Category (optional)", key="sources_category")
language = st.text_input("Language", value='en', key="sources_language")
country = st.text_input("Country Code (optional)", key="sources_country")
if st.button("Get Sources"):
    sources = news_api.get_sources(category, language, country)
    st.json(sources)

