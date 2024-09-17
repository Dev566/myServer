import yt_dlp as youtube_dl

        
def get_details_facebook_video(url):
    print(f"Downloading Facebook video from {url}")
    ydl_opts = {
        'skip_download': True,  # Do not download the video, just extract info
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            # Extract metadata from the URL
            info_dict = ydl.extract_info(url, download=False)
            return info_dict
        except Exception as e:
            print(f"Error occurred: {e}")
            return {}