import tweepy
import pandas as pd

def RONBsearch():
    search_str = "RONBupdates"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAEkCYwEAAAAAFnxYsFf0039kr22Q0FrbWnKJbvQ%3Da1WpeWeoIqnIpHS4bilKXq4NXq1CMyhHlRN9kZKwD2y9ql3iKX"
    auth = tweepy.OAuth2BearerHandler(bearer_token)
    api = tweepy.API(auth)
    no_of_tweets = 50
    tweets = []
    # retweets = []
    likes = []
    retweets_count = []

    for i in tweepy.Cursor(api.search_tweets,q = search_str, tweet_mode="extended").items(no_of_tweets):
        tweets.append(i.full_text)
        likes.append(i.favorite_count)
        retweets_count.append(i.retweet_count)
    
    tweet_dict = {
        'tweets': tweets,
        'likes' : likes,
        'retweets_count': retweets_count
    }
    tweet_df = pd.DataFrame(tweet_dict)
    df = tweet_df[tweet_df.likes != 0].sort_values('likes',ascending=False)
    df.reset_index(drop=True,inplace=True)
    
    return df.to_dict() 