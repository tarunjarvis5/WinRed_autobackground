import sys
import redditbackground

print("Enter subredditname :")
subredditName = input()
page = input("Select the subreddit filter (Hot,Top,or New) : ")
page = page.lower()
print("Setting your background as the top image of /r/" + subredditName + "...")
image = redditbackground.setBackgroundFromSubreddit(subredditName,page)
print("Done!")
print("===== Image Details =====")
print("Title: " + image["title"])