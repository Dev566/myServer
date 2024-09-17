import re
from .downloader import facebookDownloader
from .downloader import youtubeDownloader
from .downloader import instagramDownloader
from .downloader import tiktokDownloader

def fetch_url_details(url):
    # regex for url matching
    youtube_pattern = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+'
    facebook_pattern = r'(https?://)?(www\.)?facebook\.com/.+'
    instagram_pattern = r'(https?://)?(www\.)?instagram\.com/.+'
    tiktok_pattern = r'(https?://)?(www\.)?tiktok\.com/@.+/video/.+'
    print(url)
    

    # switch statement for video downloading
    if re.match(youtube_pattern, url):
        return youtubeDownloader.get_details_youtube_video(url)
    elif re.match(facebook_pattern, url):
        return facebookDownloader.get_details_facebook_video(url)
    elif re.match(instagram_pattern, url):
        return instagramDownloader.get_details_instagram_video(url)
    elif re.match(tiktok_pattern, url):
        return tiktokDownloader.get_details_tiktok_video(url)
    else:
        print("Unsupported URL")
        
