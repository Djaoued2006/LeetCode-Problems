#leetcode problem:  355. Design Twitter

class Tweet:
    def __init__(self, userId , tweetId):
        self.userId = userId
        self.tweetId = tweetId

class Action:
    def __init__(self , followerId , followeeId):
        self.follower = followerId
        self.followee = followeeId

class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = []


    def postTweet(self, userId: int, tweetId: int) -> None:
        newTweet = Tweet(userId ,tweetId)
        self.tweets.append(newTweet)

    def getNewsFeed(self, userId: int) -> list[int]:
        UserTweets = []
        count = 0
        for post in self.tweets[::-1]:
            if self.isFollowing(userId , post.userId):
                UserTweets.append(post.tweetId)
                count += 1
            if count == 10:
                break
        
        return UserTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        action = Action(followerId ,followeeId)
        self.following.append(action)
    
    def isFollowing(self, follower: int, followee:int) -> bool:
        if followee == follower:
            return True 
    
        for action in self.following:
            if action.follower == follower and action.followee == followee:
                return True 
        return False
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        for i in range(len(self.following)):
            if self.following[i].follower == followerId and self.following[i].followee == followeeId:
                del self.following[i]
                break