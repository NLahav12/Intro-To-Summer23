

def create_youtube_video(title, description):
	new_video = {
	"title" : title,
	"description" : description,
	"likes" : 0,
	"dislikes" : 0,
	"comments" : {}
	}
	return new_video

def like(video):
	if "likes" in video:
		video["likes"] += 1
	return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"] += 1
	return video 

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

new_title = "nadav"
new_description = "lahav"
new_youtube_video = create_youtube_video(new_title, new_description)
for i in range(5):
	like(new_youtube_video)
new_username = input("what is the username that comments: ")
new_comment = input("what is the comment: ")

add_comment(new_youtube_video, new_username, new_comment)
print(new_youtube_video)






