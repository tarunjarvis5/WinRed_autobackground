import sys
import redditbackground

print("Enter subredditname :")
subredditName = input()
page = input("Select the subreddit filter (Hot,Top,or New) : ")
page = page.lower()
save = input("Do you want to download and save the image? (y/n) : ")
print("Setting your background as the top image of /r/" + subredditName + "...")
image = redditbackground.setBackgroundFromSubreddit(subredditName,page,save)
print("Done!")
print("===== Image Details =====")
print("Title: " + image["title"])