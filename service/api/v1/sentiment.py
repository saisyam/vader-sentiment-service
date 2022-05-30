from fastapi import APIRouter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .schemas import Input, Output


router = APIRouter()

def sentiment_scores(sentence):
    sentiment = ""
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    if sentiment_dict['compound'] >= 0.05 :
        sentiment = "Positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment = "Negative"
    else :
        sentiment = "Neutral"
    
    return sentiment

@router.post("/sentiment", response_model=Output, tags=["Vader Sentiment Analysis"])
def vader_sentiment(inputs: Input):
    
    sentiment = sentiment_scores(inputs.sentence)

    return {
        "sentence": inputs.sentence,
        "sentiment": sentiment,
    }