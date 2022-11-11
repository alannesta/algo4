"""
https://leetcode.com/problems/design-twitter/
典中典
"""
from typing import List, Dict, Optional
import heapq
from datetime import datetime


class Twitter:
    def __init__(self):
        self.user_tracker: Dict[int, User] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.user_tracker:
            user = self.user_tracker[userId]
            user.post_tweet(tweetId)
        else:
            user = User(userId)
            user.post_tweet(tweetId)
            self.user_tracker[userId] = user

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.user_tracker:
            user = self.user_tracker[userId]
            return user.get_feed()
        else:
            return []

    # 这道题user not exist yet的handle很烦人, 其它还好
    def follow(self, followerId: int, followeeId: int) -> None:
        # Optional: handle user does not exist yet
        if followerId in self.user_tracker:
            user = self.user_tracker[followerId]
        else:
            user = User(followerId)
            self.user_tracker[followerId] = user

        if followeeId in self.user_tracker:
            user.follow(self.user_tracker[followeeId])
        else:
            n_user = User(uid=followeeId)
            self.user_tracker[followeeId] = n_user
            user.follow(n_user)

    # 这道题user not exist yet的handle很烦人, 其它还好
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_tracker:
            user = self.user_tracker[followerId]
            user.unfollow(self.user_tracker[followeeId])


class User:
    def __init__(self, uid):
        self.uid = uid
        self.following: Dict[int, User] = {uid: self}
        self.tweets: Optional[Tweet] = None  # linked list

    def post_tweet(self, tid: int) -> None:
        tweet = Tweet(tid)
        if not self.tweets:
            self.tweets = tweet
        else:
            # append to head
            tweet.next = self.tweets
            self.tweets = tweet

    def get_feed(self) -> List[int]:
        following = self.following.values()
        min_heap = []
        top_10_tweets = []
        for user in following:
            if user.tweets:
                heapq.heappush(min_heap, (-user.tweets.timestamp, user.tweets))
        while min_heap:
            # NOTES: use heappop not pop
            most_recent_tweet = heapq.heappop(min_heap)
            top_10_tweets.append(most_recent_tweet[1].tid)
            if most_recent_tweet[1].next:
                heapq.heappush(min_heap, (-most_recent_tweet[1].next.timestamp, most_recent_tweet[1].next))
            if len(top_10_tweets) == 10:
                break

        return top_10_tweets

    def follow(self, user: 'User'):
        self.following[user.uid] = user

    def unfollow(self, user: 'User'):
        if user.uid in self.following:
            self.following.pop(user.uid)


class Tweet:
    def __init__(self, tid, next=None):
        self.tid = tid
        self.timestamp = datetime.now().timestamp()
        self.next = next

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
