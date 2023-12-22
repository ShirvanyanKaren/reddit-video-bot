# lets pull some data from reddit api print it

import praw
import json
import os
import time
import datetime
import requests
import sys
import re
import random
# import config as cfg 
import configparser
from voiceover import getVoiceover
from createmovie import createClip
from screenshot import getScreenShot

config = configparser.ConfigParser()
config.read('config.ini') 

client_id = config['Reddit']['client_id']
client_secret = config['Reddit']['client_secret']
password = config['Reddit']['password']
user_agent = config['Reddit']['user_agent']
username = config['Reddit']['username']
subreddits_c = config['subreddit']

working_dir = config['Directory']['path']
output_dir = working_dir + config['Directory']['output_file']
used_posts = f"{output_dir}/{config['Directory']['used_posts']}"
voicer_overs = f"{output_dir}/Voiceovers"
screenshots = f"{output_dir}/Screenshots"
json_dir = f"{output_dir}/posts.json"

# import our reddit instance
reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        password=password,
                        user_agent=user_agent,
                        username=username)






def randomPosts(number):
    subreddit_list = list(subreddits_c.values())
    random_subreddit = random.choice(subreddit_list)
    print("the random subreddit is: " + random_subreddit)
    subreddit = reddit.subreddit(random_subreddit)
    hot_posts = subreddit.hot(limit=number)
    return hot_posts


# for submission in hot_posts:
#     len = len(submission.selftext)
#     print("the length is: " + str(len))
#     while len < 100 and not checkIfUsed(submission.id):
#         len = len(submission.selftext)
#         print("the length is: " + len)
#         hot_posts = subreddit.hot(limit=1)




files_finder = {}

def getPosts(used_posts, number):
    print("getting posts")
    hot_posts = randomPosts(number)
    with open(used_posts, 'a') as f:
        print("opened file")
        for submission in hot_posts:
            if not checkIfUsed(submission.id) and len(submission.selftext) > 100 and submission.over_18 == False:
                f.write(submission.id + '\n')
                text = submission.title + submission.selftext
                voFilePath = f"{voicer_overs}/{submission.id}.mp3"
                scFilePath = f"{screenshots}/{submission.id}.png"
                getVoiceover(voFilePath, text)
                getScreenShot(submission.url, submission.id, scFilePath)
                addToDict(submission, voFilePath, scFilePath)
                print("wrote to file")
    with open(json_dir, 'a') as f:
        json.dump(files_finder, f)
    print(files_finder)
    createMovie()
    return files_finder

def createMovie():
    for key, value in files_finder.items():
        # time.sleep(30)
        print("creating movie")
        print(value['screenshot'])
        print(value['voiceover'])
        createClip(value['screenshot'], value['voiceover'], f"{key}-{value['title']}")
        print("created movie")     
    
def addToDict(submission, voFilePath, scFilePath):
    files_finder[submission.id] = {}
    files_finder[submission.id]['title'] = submission.title
    files_finder[submission.id]['url'] = submission.url
    files_finder[submission.id]['voiceover'] = voFilePath
    files_finder[submission.id]['screenshot'] = scFilePath
    print("wrote to file")
    # return files_finder
               


def checkIfUsed(post_id):
    with open(used_posts, 'r') as f:
        for line in f:
            if post_id in line:
                return True
        return False
    


def getPostGivenUrl(url):
    print("getting post")
    submission = reddit.submission(url=url)
    if len(submission.selftext) > 100:
        text = submission.title + submission.selftext
        voFilePath = f"{voicer_overs}/{submission.id}.mp3"
        scFilePath = f"{screenshots}/{submission.id}.png"
        getVoiceover(voFilePath, text)
        getScreenShot(submission.url, submission.id, scFilePath)
        addToDict(submission, voFilePath, scFilePath)
        print("wrote to file")
    with open(json_dir, 'a') as f:
        json.dump(files_finder, f)
    print(files_finder)
    createMovie()
    return files_finder

# getPosts(used_posts)

def menu():
    while True:
        print("1. Get posts")
        print("2. Get post given url")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            number = input("Enter number of posts: ")
            number = int(number)
            getPosts(used_posts, number)
        elif choice == "2":
            url = input("Enter url: ")
            getPostGivenUrl(url)
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice")
menu()


 











