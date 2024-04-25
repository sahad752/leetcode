
from collections import defaultdict
import re


class Twitter:
    def __init__(self) -> None:
        self.tweetmap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        return []

    def getNewsFeed(self, userId: int) -> None:
        return []

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


Twitter().follow(1,2)
Twitter().follow(1,3)



