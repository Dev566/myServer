import re
from .downloader import facebookDownloader
from .downloader import youtubeDownloader
from .downloader import instagramDownloader
from .downloader import tiktokDownloader

def download_video(url, output_dir = '.', downloaded_video = 'downloaded_video'):
    # regex for url matching
    youtube_pattern = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+'
    facebook_pattern = r'(https?://)?(www\.)?facebook\.com/.+'
    instagram_pattern = r'(https?://)?(www\.)?instagram\.com/p/.+'
    tiktok_pattern = r'(https?://)?(www\.)?tiktok\.com/@.+/video/.+'


    # switch statement for video downloading
    if re.match(youtube_pattern, url):
        youtubeDownloader.download_youtube_video(url, output_dir, downloaded_video)
    elif re.match(facebook_pattern, url):
        facebookDownloader.download_facebook_video(url, output_dir, downloaded_video)
    elif re.match(instagram_pattern, url):
        instagramDownloader.download_instagram_video(url, output_dir, downloaded_video)
    elif re.match(tiktok_pattern, url):
        tiktokDownloader.download_tiktok_video(url, output_dir, downloaded_video)
    else:
        print("Unsupported URL")
        
