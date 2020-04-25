#!/usr/bin/python3 
from instapy import InstaPy 

session = InstaPy(username="godfrey_atima", password="new@daytoday")

#Logging into instagram
session.login()

# like by tags
session.like_by_tags(["programming", "python"], amount=5)

# avoid liking inapropriate post
session.set_dont_like(["naked", "nsfw"])

# to follow some author
session.set_do_follow(True, percentage=50)

# to leave comment
session.set_do_comments(True, percentage=50)

# close the browser & save the logs
session.end()