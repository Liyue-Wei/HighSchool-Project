from pytube import YouTube
i = input()
url = []
while True:
    if i=="ap":
        url.append(input())

    elif i=="do":
        try:
            for i in range(0, len(url)):
                yt = YouTube(url[i])
                yt.streams.filter(type="music").first().download()
            break

        except:
            print("error")