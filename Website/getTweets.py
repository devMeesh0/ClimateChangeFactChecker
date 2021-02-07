import os
import snscrape.modules.twitter as sntwitter
import MySQLdb
from MySQLdb.cursors import DictCursor
import requests
import json

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

    """keywordsMisrepresent = ["wetter than normal", "snow", "outside", "forecast", "weather", "so much for", "freez",
                            "cold", "ClimateChangeiscalledSeasons", "short-term", "short term", "sea level", "ice",
                            "melt", "hot", "arctic", "cool", "FalseAlarm", "eagle", "bird", "hawk", "windturbine",
                            "wind turbine", "windmill", "wind mill", "insect", "endanger", "electric car",
                            "electric vehicle", "tesla", "battery powered car", "battery powered vehicle", "lithium",
                            "trace", "barely", "atmosphere", "coal", "electric", "tax", "pollut", "keystone",
                            "pipeline", "paris", "job", "greenhouse", "temp", "net zero", "impossib", "trillion",
                            "decept"]"""

    keywordsAdhominem = ["demonrat", "demorat", "democrat", "biden", "kamala", "republican", "tories", "tory", "labor",
                         "boris", "barack", "obama", "kerry", "trump", "AOC", "ocasio", "greta", "thunberg", "liberal",
                         "conservative", "treason", "trudeau", "pelosi", "woke", "trump", "GEOTUS", "poc", "of color",
                         "left", "right", "prince", "king", "queen", "lgbt", "california", "bernie", "sheep", "wake up",
                         "fascist", "nazi"]

    keywordsConspiracy = ["ElectionVirus", "Condemic", "voterf_r_a_u_d", "GreatCull", "CCPBidenFamily", "chemtrail",
                          "genocide", "COVID19", "TheGreatReset", "VoterFraud", "ElectionFraud", "election",
                          "vote""great reset", "fraud", "weather modification", "cannibalism", "FriendsOfScience",
                          "slave", "jew", "judeo", "bolshev", "communist", "commie", "MSM", "BLM", "Black Lives Matter",
                          "antifa", "globalist", "UN ", " UN", "deepstate""deep state", "NWO", "new world order",
                          "hollywood", "plandemic", "pandemic", "soros", "plan", "StopTheSteal", "ccp", "china",
                          "PrisonPlanet", "Lockdown", "hoax", "covid", "corona", "virus", "engineer", "concentration",
                          "vaccin", "bank", "emergency", "cult", "Agenda21", "Agenda2030"]

    """for i in range(len(keywordsMisrepresent)):
        if tweet.lower().find(keywordsMisrepresent[i].lower()) != -1:  # aka it has been found
            misrepresent += 1"""

    for j in range(len(keywordsAdhominem)):
        if tweet.lower().find(keywordsAdhominem[i].lower()) != -1:  # aka it has been found
            adhominem += 1

    for k in range(len(keywordsConspiracy)):
        if tweet.lower().find(keywordsConspiracy[i].lower()) != -1:  # aka it has been found
            conspiracy += 1

    conspiracy *= 1.5  # to account for wackos
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


def checkForDenial(tweetStr):
    json_response = requests.get("http://localhost:5000/predict", params={'data': tweetStr})
    response = json.loads(json_response.text)
    return int(response) == 0


tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for tag in HASHTAGS:
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('{}'.format(tag)).get_items()):
        if i > 5:
            break

        if checkForDenial(tweet.content):
            tweets_list1.append([(tweet.url).encode("utf-8"), (tweet.content).encode("utf-8"), tweet.date,
                             (tweet.user.username).encode("utf-8"),
                             checkKeywords(tweet.content)])
            i = i-1  # counter-act iteration

connection = MySQLdb.connect(user=db_user, passwd=db_password, db="heroku_8d712e26b0e3972",
                             host="us-cdbr-east-03.cleardb.com", cursorclass=DictCursor)
cursor1 = connection.cursor()

sql = "INSERT INTO tweettable (tweeturl, tweettext, date, username, category) VALUES (%s, %s, %s, %s, %s)"
for i in range(len(tweets_list1)):
    val = (tweets_list1[i][0], tweets_list1[i][1], tweets_list1[i][2], tweets_list1[i][3], tweets_list1[i][4])
    cursor1.execute(sql, val)

connection.commit()
