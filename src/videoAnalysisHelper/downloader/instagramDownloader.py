import yt_dlp as youtube_dl

def get_details_instagram_video(url):
    print(f"Downloading Instagram video from {url}")
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

# For later to get video description
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     info_dict = ydl.extract_info(url, download=False)
    #     video_details = {
    #         'title': info_dict.get('title', 'No title available'),
    #         'description': info_dict.get('description', 'No description available'),
    #         'uploader': info_dict.get('uploader', 'No uploader available'),
    #         'uploader_id': info_dict.get('uploader_id', 'No uploader ID available'),
    #         'uploader_url': info_dict.get('uploader_url', 'No uploader URL available'),
    #         'upload_date': info_dict.get('upload_date', 'No upload date available'),
    #         'view_count': info_dict.get('view_count', 'No view count available'),
    #         'like_count': info_dict.get('like_count', 'No like count available'),
    #         'dislike_count': info_dict.get('dislike_count', 'No dislike count available'),
    #         'duration': info_dict.get('duration', 'No duration available'),
    #     }
    #     return video_details