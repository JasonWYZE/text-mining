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


from turtle import pos
import praw
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
from thefuzz import fuzz
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt





reddit = praw.Reddit(
    client_id="8kehSoJC7UFPVRcF3XaYKw",
    client_secret="OIe6E4qiuKONKrtXsOlcNX9rrq4BRA",
    password="Wangyanzeyang41",
    user_agent="testscript by u/fakebot3",
    username="jason_ze0241",
)
sub = 'csMajors'
submissions = reddit.subreddit(sub)
keyword = input("Which companies are you looking for? >>>>>>>")


index = 0
text = ""
for i in submissions.search(f"{keyword} OA", limit=100):
    text += i.selftext


text = text.lower()

stopwords = nltk.corpus.stopwords.words("english")
word_list =  nltk.word_tokenize(text)
word_list = [w for w in word_list if w.lower() not in stopwords]
word_list = [w for w in word_list if w.lower() not in string.punctuation]
word_list = [w for w in word_list if w.lower()!="i"]
word_list = [w for w in word_list if w.lower()!="oa"]

for i in word_list:
    if(not i.isalpha() or i.isnumeric()  or i == keyword ):
        word_list.remove(i)


fd = nltk.FreqDist(word_list)
fd.tabulate(10)

easy_level = fd["easy"] # frequency of the word "easy" 
hard_level = fd["hard"]  # frequency of the word "hard"


def averagDict(d):
#This function will calculate average of a list of dict 
    average_dict = {}
    neg_sum = 0
    neu_sum = 0
    pos_sum = 0
    for i in d:
        neg_sum += i['neg']
        neu_sum += i['neu']
        pos_sum += i['pos']

    average_dict['neg'] = round(neg_sum/len(d),4)   # average negative 
    average_dict['neu'] = round(neu_sum/len(d),4)   # average neutral
    average_dict['pos'] = round(pos_sum/len(d),4)   # average positive

    return average_dict

sentiment_score = []
for i in submissions.search(f"{keyword} OA", limit=100):
    score = SentimentIntensityAnalyzer().polarity_scores(i.selftext)
    sentiment_score.append(score)


print(averagDict(sentiment_score))


string_text = []
#Text similarity 
for i in submissions.search(f"{keyword} OA", limit=100):
    string_text.append(i.selftext)

similarity_ratio = []
for i in range(0,len(string_text)-1):
    for j in range(i+1,len(string_text)):
        similarity_ratio.append(fuzz.ratio(string_text[i],string_text[j]))

def similarity(l):
    count = 0
    for i in l:
        if(i < 75):
            count+=1
    if count > 0.75*len(l):
        return ("At least 75 percentage contexts are not similar")
    return "At least 75 percentage contexts are similar"

print(similarity(similarity_ratio))


