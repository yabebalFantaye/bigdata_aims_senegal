#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import argparse
import sys

print 'code name is: ',sys.argv[0]

if len(sys.argv) > 1:
    filename=sys.argv[1]
else:
    filename='tweets.json'

print 'saving data to file: ',filename
fhandle=open(filename,'w')


if len(sys.argv) > 2:
    TweetKeyword=[sys.argv[i+2] for i in range(len(sys.argv)-2)]
else:
    TweetKeyword=['Africa','big data']


print 'TweetKeywords are: ',TweetKeyword


#Variables that contains the user credentials to access Twitter API 
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret =os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACESS_TOKEN_SECRET')



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        fhandle.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: first argument to this code
    stream.filter(track=TweetKeyword)
