import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommendation System",layout="wide")
load_dotenv()
@st.catch_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences")
if query:
    with st.spinner("Fetching Recommendation for you"):
        response = pipeline.recommend(query)
        st.markdown('###Recommendations')
        st.write(response)
         


