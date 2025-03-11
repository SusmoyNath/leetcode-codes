from typing import List
import heapq
import collections

class Twitter:
    
    def __init__(self):
        self.timestamp = 0  # Global timestamp
        self.tweets = collections.defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.following = collections.defaultdict(set)  # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Post a tweet with a global timestamp."""
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1  # Increment timestamp

    def getNewsFeed(self, userId: int) -> List[int]:
        """Return the 10 most recent tweets from the user and their followees."""
        min_heap = []
        users_to_check = self.following[userId] | {userId}  # Self and followees

        for user in users_to_check:
            if self.tweets[user]:  # If the user has tweets
                for tweet in self.tweets[user][-10:]:  # Take only last 10 tweets
                    heapq.heappush(min_heap, tweet)
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)  # Keep only the top 10 most recent tweets

        return [tweetId for _, tweetId in sorted(min_heap, reverse=True)]  # Sort in descending order

    def follow(self, followerId: int, followeeId: int) -> None:
        """User follows another user."""
        if followerId != followeeId:  # Prevent self-following
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """User unfollows another user."""
        self.following[followerId].discard(followeeId)  # Remove followee if exists
