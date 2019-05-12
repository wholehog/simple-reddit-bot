import praw
import pdb
import re
import os

botname = *** #enter your own username!
reddit = praw.Reddit('bot1') #information is stored in praw.ini file

if not os.path.isfile("comments_replied_to.txt"): #stores comments that the bot has already replied to
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

subreddit = reddit.subreddit("learnpython")
misspellings = ['ypthon', 'ptyhon', 'pyhton', 'pytohn', 'pythno']
double_letters = ['ppython', 'pyython', 'pytthon' 'pythhon', 'pythoon', 'pythonn']
#for submission in subreddit.stream.comments(): #use to monitor new submissions in real time
for submission in subreddit.new(limit=100):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments:
        if comment.id not in comments_replied_to:
            for word in misspellings + double_letters:
                if re.search(word, comment.body, re.IGNORECASE):
                    reply = comment.body + '   ' + comment.permalink
                    reddit.redditor(botname).message('You misspelled \'Python\'!', reply)
                    comments_replied_to.append(comment.id)
                    print('sent')

#bot only sends a message to itself because sending a lot of automated
#messages to other users might violate sitewide rules

with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")

input('Press ENTER to exit')
