class User:
    def __init__(self):
        self.following = []
        self.posts = []

class Twitter:

    def __init__(self):
        self.time = 0
        self.users = defaultdict(User)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].posts.append((tweetId,self.time))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = self.users[userId].posts.copy()

        for user_following in self.users[userId].following:
            allTweets.extend(self.users[user_following].posts)
        heapq.heapify(allTweets)
 
        return [x for x,t in heapq.nlargest(10,allTweets,lambda x: x[1])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users[followerId].following and followeeId != followerId:
            self.users[followerId].following.append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId].following and followeeId != followerId:
            self.users[followerId].following.remove(followeeId)
