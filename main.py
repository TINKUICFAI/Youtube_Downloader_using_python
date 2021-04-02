from pytube import YouTube
url=input("Please enter youtube vedio url")
videos=YouTube(url).streams.all()
number=1
for video in videos:
    print(f"{number} for {video}")
    print(" ")
    number+=1
user_input=int(input("Enter your chice"))
videos = video[user_input-1]
videos.download("Desktop")
print("File Downloadwd successfully")
#YouTube()