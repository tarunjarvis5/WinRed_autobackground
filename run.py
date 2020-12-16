import sys
import redditbackground

print("Enter subredditname :")
subredditName = input()

page = input("Select the subreddit filter (Hot,Top,or New) : ")
page = page.lower()
if page not in ["hot","top","new"] :
    sys.exit("Input****Error****")

save = input("Do you want to download and save the image? (y/n) : ")
if save not in "yn":
    sys.exit("Input****Error****")
elif save == "yn" :
    sys.exit("Input****Error****")

print("Setting your background as the top image of /r/" + subredditName + "...")
image = redditbackground.setBackgroundFromSubreddit(subredditName,page,save)
print("Done!")
print("===== Image Details =====")
print("Title: " + image["title"])