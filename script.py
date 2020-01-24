import tweepy
import csv
from textblob import TextBlob

consumer_key = '5WvumnRui2JfqCghofZyeDaap'
consumer_secret = 'OHikANulDusE0GAUxhAJLGsF677ONJ4JGxfeqYgUlE4MQ79il5'

access_token = '3034340154-mlvKqPEAVVgYrRbRDGsdVgfaM4h8AHlHMBUmBCs'
access_token_secret = 'G3JGPFXyxwJUIfatLP1xaDrpfHJb8kxIm76IuCyjtbLF5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Virat Kohli')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself
lines=[['' for i in range(5)] for j in range(3)]

lines[0][0]="Tweet"
lines[1][0]="polarity"
lines[2][0]="subjectivity"

for tweet,i in zip(public_tweets,range(1,5)):
    analysis = TextBlob(tweet.text)
    lines[0][i]=tweet.text
    lines[1][i]=float(analysis.sentiment.polarity)
    lines[2][i]=float(analysis.sentiment.subjectivity)
    print(tweet.text+'\n')

with open('Twitter.csv','w') as writefile:
	writer = csv.writer(writefile)
	writer.writerow([unicode(s).encode("utf-8") for s in lines])

writefile.close()
   