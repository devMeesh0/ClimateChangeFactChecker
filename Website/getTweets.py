import os
import snscrape.modules.twitter as sntwitter
import pandas as pd


HASHTAGS = [
    "#ClimateChangeHoax",
    "#climatechangehoax",
    "#ClimateChangeNotReal",
    "#climatechangenotreal",
    "#ClimateChangeIsFalse",
    "#climatechangeisfalse",
    "#GlobalWarmingHoax",
    "#tcot",
    "#ccot",
    "#tlot",
    "#pjnet",
    "#rednationrising",
    "#votered"
]


# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for tag in HASHTAGS:
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{}'.format(tag)).get_items()):
        if i>5:
            break
        tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# responses = []

# for tag in HASHTAGS:
#     os.system("snscrape --format --max-results 5 --since 2020-06-01 twitter-search \"{}\" >> text-query-tweets.json".format(tag))

# tweets_df = pd.read_json('text-query-tweets.json', lines=True)

print(tweets_df1.head())
