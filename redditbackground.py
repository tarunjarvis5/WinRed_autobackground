import urllib.request
import json
import sys
import ctypes
import time
import os

def setBackgroundFromSubreddit(subredditName,page,save):
	topImagePost = getTopImageFromSubreddit(subredditName,page)
	imageFilename = storeImageInStoredBackgroundsFolder(topImagePost)
	setImageAsBackground(imageFilename)
	if save == "n" :
		time.sleep(3)
		DeleteImage(imageFilename)
	return topImagePost

def getTopImageFromSubreddit(subredditName,page):
	topImagePosts = getTopImagePostsFromSubreddit(subredditName,page)
	topPost = topImagePosts[0]["data"]
	return topPost

def getTopImagePostsFromSubreddit(subredditName,page):
	if page == 'top' :
		subredditPostsUrl = "https://www.reddit.com/r/" + subredditName + "/top.json"
	elif page == 'hot' :
		subredditPostsUrl = "https://www.reddit.com/r/" + subredditName + "/hot.json"
	elif page == 'new' :
		subredditPostsUrl = "https://www.reddit.com/r/" + subredditName + "/new.json"

	while True:
		try:
			postsAsJsonRawText = urllib.request.urlopen(subredditPostsUrl).read()
			break
		except urllib.error.HTTPError as err:
			time.sleep(5)

	decodedJson = json.loads(postsAsJsonRawText.decode('utf-8'))
	posts = decodedJson["data"]["children"]
	return posts

def storeImageInStoredBackgroundsFolder(image):
	createStoredBackgroundsFolderIfNotExists()
	imageFilename = "bg_" + image["title"] + ".jpg"
	open("stored_backgrounds/" + imageFilename, "wb").write(urllib.request.urlopen(image["url"]).read())
	return imageFilename

def createStoredBackgroundsFolderIfNotExists():
	if not os.path.exists("stored_backgrounds"):
		os.makedirs("stored_backgrounds")

def setImageAsBackground(imageFilename):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, getFullPathOfImage(imageFilename) , 0)

def getFullPathOfImage(imageFilename):
	return os.path.dirname(os.path.realpath("stored_backgrounds/" + imageFilename)) + "\\" + imageFilename

def DeleteImage(imageFilename):

	if os.path.exists(getFullPathOfImage(imageFilename)) :
		os.remove(getFullPathOfImage(imageFilename))
	else :
		print("Image does not exist")


