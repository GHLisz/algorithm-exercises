'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

from collections import defaultdict
from heapq import heappush, heappop


class MiniTwitter:
    def __init__(self):
        # do intialization if necessary
        self.map = defaultdict(list)
        self.follow_id = defaultdict(list)
        self.time = 0

    def postTweet(self, user_id, tweet_text):
        """
        @param: user_id: An integer
        @param: tweet_text: a string
        @return: a tweet
        """
        # write your code here
        new_tweet = Tweet.create(user_id, tweet_text)
        self.map[user_id].append((self.time, new_tweet))
        self.time += 1
        return new_tweet

    def getNewsFeed(self, user_id):
        """
        @param: user_id: An integer
        @return: a list of 10 new feeds recently and sort by timeline
        """

        # write your code here
        heap = []
        for follow in self.follow_id[user_id]:
            for time, tweet in self.map[follow]:
                heappush(heap, (-time, tweet))
        for time, tweet in self.map[user_id]:
            heappush(heap, (-time, tweet))
        n = len(heap)
        result = []
        i = 0
        while i < 10 and i < n:
            time, tweet = heappop(heap)
            result.append(tweet)
            i += 1
        return result

    def getTimeline(self, user_id):
        """
        @param: user_id: An integer
        @return: a list of 10 new posts recently and sort by timeline
        """
        # write your code here
        heap = []
        for time, tweet in self.map[user_id]:
            heappush(heap, (-time, tweet))
        result = []
        i = 0
        n = len(heap)
        while i < 10 and i < n:
            time, tweet = heappop(heap)
            result.append(tweet)
            i += 1
        return result

    def follow(self, from_user_id, to_user_id):
        """
        @param: from_user_id: An integer
        @param: to_user_id: An integer
        @return: nothing
        """
        # write your code here
        if to_user_id not in self.follow_id[from_user_id]:
            self.follow_id[from_user_id].append(to_user_id)

    def unfollow(self, from_user_id, to_user_id):
        """
        @param: from_user_id: An integer
        @param: to_user_id: An integer
        @return: nothing
        """
        # write your code here
        if to_user_id in self.follow_id[from_user_id]:
            self.follow_id[from_user_id].remove(to_user_id)
