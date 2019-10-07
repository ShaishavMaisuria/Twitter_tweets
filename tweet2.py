"""
This the second part. is the twitter scraping class which scraps the data using authenication and it also prints the
scraped data on console and in the file
"""
from tweepy import API
from tweepy import cursor
from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler

import authenticationKeys

"""
This is the class helps to authenticate everyhing inside the class
"""
class TwitterAuthentication():

    def authentication_api(self):
        authentication = OAuthHandler(authenticationKeys.ConsumerKey,
                                     authenticationKeys.ConsumerSecret)  # use in case for the authentication with using consumer key
        authentication.set_access_token(authenticationKeys.AccessToken,
                                       authenticationKeys.AccessTokenSecret)  # use in case for the authentication with using access tokens are given to the key objects of consumer
        return authentication

class TwitterAuthStreamer():
    """
    It is class for getting fresh tweets using streamer class
    """
    def __init__(self):
        self.twitter_Authentication  =  TwitterAuthentication()

    def AuthStream_tweets(self, list_of_hastags_from_twitter, fileName_with_fresh_tweets):
        # it authenitcates the authenication using keys and tokes and also works with stramListener class
        listenObject = streamListener(fileName_with_fresh_tweets)
        authentication=self.twitter_Authentication.authentication_api()
        streaming = Stream(authentication,
                           listenObject)  # listener is used for the deciding what to do with the data and to get if any errors

        streaming.filter(track=list_of_hastags_from_twitter)


class streamListener(StreamListener):
    """
    this class print the sthe tweets obtained on the console or in output
    """

    def __init__(self, fileName_with_fresh_tweets):
        self.fileName_with_fresh_tweets = fileName_with_fresh_tweets

    # using this class for getting the raw data and print the raw data from the twitter api we have. Also it checks for the error.
    def on_data(self, raw_data):
        try:
            print(raw_data)
            f=open(fileName_with_fresh_tweets, 'a')
            f.write(raw_data)
            return True
        except BaseException as e:
            print("Error On_Data %s" %(str(e)))
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    list_of_hastags_from_twitter = ["donald trump", "hillary clinton", "barack obama", "bernie sanders"]
    fileName_with_fresh_tweets = "twitterTweets.txt"
    streamTwitter = TwitterAuthStreamer()
    streamTwitter.AuthStream_tweets(list_of_hastags_from_twitter, fileName_with_fresh_tweets)






