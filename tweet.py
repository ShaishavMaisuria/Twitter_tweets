"""
This is the twitter scraping class which scraps the data using authenication and it also prints the
scraped data on console and in the file
"""
from tweepy import API
from tweepy import cursor
from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler

import authenticationKeys

class TwitterAuthStreamer():
    """
    It is class for getting fresh tweets using streamer class
    """
    def AuthStream_tweets(self, list_of_hastags_from_twitter, fileName_with_fresh_tweets):
        #it authenitcates the authenication using keys and tokes and also works with stramListener class
        listenObject = streamListener()
        authenication = OAuthHandler(authenticationKeys.ConsumerKey,
                                     authenticationKeys.ConsumerSecret)  # use in case for the authentication with using consumer key
        authenication.set_access_token(authenticationKeys.AccessToken,
                                       authenticationKeys.AccessTokenSecret)  # use in case for the authentication with using access tokens are given to the key objects of consumer
        streaming = Stream(authenication,
                           listenObject)  # listener is used for the deciding what to do with the data and to get if any errors

        streaming.filter(track=list_of_hastags_from_twitter)



class streamListener(StreamListener):
    """
    this class print the sthe tweets obtained on the console or in output
    """

    def __init__(self,fileName_with_fresh_tweets):
        self.fileName_with_fresh_tweets=fileName_with_fresh_tweets

    # using this class for getting the raw data and print the raw data from the twitter api we have. Also it checks for the error.
    def on_data(self, raw_data):
        try:
            print(raw_data)
            with open(self,fileName_with_fresh_tweets,'a') as twitter_file:
                twitter_file.write(raw_data)
                return True

        except BaseException as e:
            print("Error in the Data $s"% str(e))
            return True
    def on_error(self, status_code):
        print(status_code)




if __name__ == "__main__":

    hashtag_list=["donald trump", "hillary clinton","barack obama", "bernie sanders"]
    fileName_with_fresh_tweets="twitterTweets.json"
    streamTwitter = TwitterAuthStreamer()
    streamTwitter.AuthStream_tweets(list_of_hastags_from_twitter, fileName_with_fresh_tweets)

    




