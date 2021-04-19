from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=nqVqaK3gjBw').streams.first().download()


