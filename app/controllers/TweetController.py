from flask import jsonify, request
from flask.views import MethodView
from app.model import Tweet, User

class TweetController(MethodView):
    def get(self, user_id):
        user = User.objects.get_or_404(user_id=user_id)
        tweets = Tweet.objects(user__in=[user.id] + user.following)[:10]
        response = [{'tweet_id': tweet.tweet_id, 'content': tweet.content} for tweet in tweets]
        return jsonify(response), 200

    def post(self, user_id):
        data = request.get_json()
        if 'content' not in data:
            return jsonify({'error': 'Content is required for posting a tweet'}), 400

        user = User.objects.get_or_404(user_id=user_id)
        tweet = Tweet(user=user, tweet_id=len(Tweet.objects) + 1, content=data['content'])
        tweet.save()
        return jsonify({'message': 'Tweet posted successfully.'}), 201

    def follow(self, follower_id, followee_id):
        data = request.get_json()
        if 'followee_id' not in data:
            return jsonify({'error': 'Followee ID is required for following.'}), 400

        follower = User.objects.get_or_404(user_id=follower_id)
        followee = User.objects.get_or_404(user_id=data['followee_id'])
        follower.following.append(followee)
        follower.save()
        return jsonify({'message': 'User followed successfully.'}), 200

    def unfollow(self, follower_id, followee_id):
        data = request.get_json()
        if 'followee_id' not in data:
            return jsonify({'error': 'Followee ID is required for unfollowing.'}), 400

        follower = User.objects.get_or_404(user_id=follower_id)
        followee = User.objects.get_or_404(user_id=data['followee_id'])

        if followee in follower.following:
            follower.following.remove(followee)
            follower.save()
            return jsonify({'message': 'User unfollowed successfully.'}), 200
        else:
            return jsonify({'message': 'User was not following the specified followee.'}), 404
