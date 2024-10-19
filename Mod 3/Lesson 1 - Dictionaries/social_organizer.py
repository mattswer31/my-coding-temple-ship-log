# Exercise 2: Social Media Content Organizer

class AlreadyExists(Exception):
    pass

def add_platform(platform):
    try:
        if platform in social_media:
            raise AlreadyExists
        else:
            social_media[platform] = {}
    except AlreadyExists:
        print(f"{platform} already exists")

def add_post_type(platform, type):
    try:
        if type in social_media[platform]:
            raise AlreadyExists
        else:
            social_media[platform] = {type : []}
    except AlreadyExists:
        print(f"{type} already exists on {platform}.")

def add_post(platform, type, post):
    try:
        social_media[platform].get(type).append(post)
    except KeyError:
        print("error")

def display_all():
    for platform, posts in social_media.items():
        print(f"{platform} posts:")
        for type, post in posts.items():
            print(f"{type}: {post}")

# dict {platform : {Type : [post, post, post]}}
social_media = {
    "facebook" : {
        "Video" : ["cats purring", "dogs playing"],
        "Image" : ["grad photo", "birthday party"]
    },
    "twitter" : {
        "Text" : ["tv announcement", "game update"],
        "Image" : ["sports meme", "fanart"]
    }
}  

add_platform("instagram")
add_platform("instagram")
add_post_type("instagram", "image")
add_post_type("instagram", "image")
add_post("instagram", "image", "selfie")
add_post("instagram", "image", "group photo")
display_all()