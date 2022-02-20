from fileinput import filename
from yt_dlp import YoutubeDL

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')

ydl_opts = {
        'format': '140[filesize<15M]',
        #'postprocessors': [{
        #    'key': 'FFmpegExtractAudio',
        #    'preferredcodec': 'm4a',
        #    'preferredquality': '192',
        #}],
        'outtmpl': '/music/%(title)s-%(id)s.%(ext)s',
    'logger': MyLogger(),
    'progress_hooks': [my_hook]
    }

def downloadVideo(link):
    try:
        li = ["sex"]
        li[0] = link
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            return ydl.prepare_filename(info)
    except:
        print("cannot download")
        return 1
                

downloadVideo('https://www.youtube.com/watch?v=ruQRvlNp-xQ')

