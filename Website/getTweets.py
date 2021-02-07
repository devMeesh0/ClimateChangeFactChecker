import os
import snscrape.modules.twitter as sntwitter
import pandas as pd
import MySQLdb
from MySQLdb.cursors import DictCursor

db_password = os.getenv("TWITTER_FACTCHECK_DB_PASS")
db_user = os.getenv("TWITTER_FACTCHECK_DB_USER")


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


def checkKeywords(tweet):
    misrepresent = 0
    adhominem = 0
    conspiracy = 0

    if len(tweet) <= 0:
        return -1

    keywordsMisrepresent = ["wetter than normal","snow","outside","forecast","weather","so much for","freez","cold","ClimateChangeiscalledSeasons","short-term","short term","sea level","ice","melt","hot","arctic","cool","FalseAlarm","eagle","bird","hawk","windturbine","wind turbine","windmill","wind mill","insect","endanger","electric car","electric vehicle","tesla","battery powered car","battery powered vehicle","lithium","trace","barely","atmosphere","coal","electric","tax","pollut","keystone","pipeline","paris","job","greenhouse","temp","net zero","impossib","trillion","decept"]

    keywordsAdhominem = ["demonrat","demorat","democrat","biden","kamala","republican","tories","tory","labor","boris","barack","obama","kerry","trump","AOC","ocasio","greta","thunberg","liberal","conservative","treason","trudeau","pelosi","woke","trump","GEOTUS","poc","of color","left","right","prince","king","queen","lgbt","california","bernie","sheep","wake up","fascist","nazi"]

    keywordsConspiracy = ["ElectionVirus","Condemic","voterf_r_a_u_d","GreatCull","CCPBidenFamily","chemtrail","genocide","COVID19","TheGreatReset","VoterFraud","ElectionFraud","election","vote""great reset","fraud","weather modification","cannibalism","FriendsOfScience","slave","jew","judeo","bolshev","communist","commie","MSM","BLM","Black Lives Matter","antifa","globalist","UN "," UN","deepstate""deep state","NWO","new world order","hollywood","plandemic","pandemic","soros","plan","StopTheSteal","ccp","china","PrisonPlanet","Lockdown","hoax","covid","corona","virus","engineer","concentration","vaccin","bank","emergency","cult","Agenda21","Agenda2030"]

    for i in range(len(keywordsMisrepresent)): #range(len(keywordsMisrepresent - 1)):
        if tweet.lower().find( keywordsMisrepresent[i].lower() ) != -1: #aka it has been found
           misrepresent += 1

    for i in range(len(keywordsAdhominem)):
        if tweet.lower().find( keywordsAdhominem[i].lower() ) != -1: #aka it has been found
            adhominem += 1

    for i in range(len(keywordsConspiracy)):
        if tweet.lower().find( keywordsConspiracy[i].lower() ) != -1: #aka it has been found
            conspiracy += 1

    conspiracy *= 1.5 #to account for wackos
    bestfit = max([misrepresent, adhominem, conspiracy])

    if bestfit == 0:
        return "unsubstant"
    elif bestfit == conspiracy:
        return "conspiracy"
    elif bestfit == misrepresent:
        return "misrepresent"
    elif bestfit == adhominem:
        return "adhominem"
    else:
        return "unsubstant"
    print("Warning: Supposedly unreachable code triggered in function checkKeywords written by Spencer. CTRL+F for Team1280IsBased to find this quickly")
    

tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for tag in HASHTAGS:
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{}'.format(tag)).get_items()):
        if i>5:
            break
        tweets_list1.append([(tweet.url).encode("utf-8"), (tweet.content).encode("utf-8"), tweet.date,
                             (tweet.user.username).encode("utf-8"), 
                             checkKeywords(tweet.content)])
    
# Creating a dataframe from the tweets list above 
# tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'URL', 'Text', 'Username'])


#sql test variables--------------------------------------------

# tweets_list1 = [
#     ["kanishk","is","super", "super", "bad"],
#     ["when","zach","flexes","on", "the haters"]
# ]

#sql test variables--------------------------------------------


connection = MySQLdb.connect(user=db_user, passwd=db_password, db="heroku_8d712e26b0e3972", host="us-cdbr-east-03.cleardb.com", cursorclass=DictCursor)
cursor1 = connection.cursor()

sql = "INSERT INTO tweettable (tweeturl, tweettext, date, username, category) VALUES (%s, %s, %s, %s, %s)"
for i in range(len(tweets_list1)):
    val = (tweets_list1[i][0],tweets_list1[i][1],tweets_list1[i][2],tweets_list1[i][3], tweets_list1[i][4])
    cursor1.execute(sql, val)

# sql = "SELECT * FROM tweettable"

# cursor1.execute(sql)

# result = cursor1.fetchall()
# for x in result:
#     print(x)
connection.commit()


# print(tweets_list1)
# print(tweets_df1.head())

