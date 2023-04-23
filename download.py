import yt_dlp
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

video_id = config.get('Url', 'video_id')

video_url = "https://www.youtube.com/watch?v=" + video_id

options = {
    "format": "bestaudio/best",
    "extractaudio": True,
    "audioformat": "mp3",
    "outtmpl": "audio.mp3",
}

ydl = yt_dlp.YoutubeDL(options)

info_dict = ydl.extract_info(video_url, download=False)
audio_url = info_dict.get("url", None)
if audio_url is not None:
    ydl.download([audio_url])
