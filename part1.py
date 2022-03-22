# # print(reddit.read_only)

# # # continued from code above

# # for submission in reddit.subreddit("learnpython").hot(limit=10):
# #     print(submission.title)

# # # Output: 10 submissions


# import praw

# reddit = praw.Reddit(
#     client_id="8kehSoJC7UFPVRcF3XaYKw",
#     client_secret="OIe6E4qiuKONKrtXsOlcNX9rrq4BRA",
#     user_agent="redditdev scraper by u/watchful1.",
#     username="jason_ze0241",
#     password="Wangyanzeyang41",
# )

# # print(reddit.read_only)
# # Output: False

# # assume you have a reddit instance bound to variable `reddit`
# subreddit = reddit.subreddit("redditdev")

# # print(subreddit.display_name)
# # # Output: redditdev
# # print(subreddit.title)
# # # Output: reddit development
# # print(subreddit.description)
# # Output: a subreddit for discussion of ...


# # assume you have a Subreddit instance bound to variable `subreddit`
# for submission in subreddit.hot(limit=10):
#     print(submission.title)
#     # Output: the submission's title
#     print(submission.score)
#     # Output: the submission's score
#     print(submission.id)
#     # Output: the submission's ID
#     print(submission.url)
#     # Output: the URL the submission points to or the submission's URL if it's a self post

# # assume you have a Submission instance bound to variable `submission`
# redditor1 = submission.author
# # print(redditor1.name)
# # # Output: name of the redditor

# # # assume you have a Reddit instance bound to variable `reddit`
# # redditor2 = reddit.redditor("bboe")
# # print(redditor2.link_karma)
# # Output: u/bboe's karma

# top_level_comments = list(submission.comments)
# all_comments = submission.comments.list()

# # assume you have a Reddit instance bound to variable `reddit`
# submission = reddit.submission(id="39zje0")
# submission.comment_sort = "new"
# top_level_comments = list(submission.comments)

# import pprint

# # assume you have a Reddit instance bound to variable `reddit`
# submission = reddit.submission(id="39zje0")
# # print(submission.title)  # to make it non-lazy
# # pprint.pprint(vars(submission))


import praw
reddit = praw.Reddit(
    client_id="8kehSoJC7UFPVRcF3XaYKw",
    client_secret="OIe6E4qiuKONKrtXsOlcNX9rrq4BRA",
    password="Wangyanzeyang41",
    user_agent="testscript by u/fakebot3",
    username="jason_ze0241",
)
sub = 'csMajors'
submissions = reddit.subreddit(sub)
keyword = input("Which companies are you looking for?")

for i in submissions.search(f"{keyword} OA", limit=1):
    print(i.title)
    print(i.selftext)
