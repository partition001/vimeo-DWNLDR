import os

# Function to download a video based on the provided URL and destination folder
def download_video(url, download_directory):
    from vimeo_downloader import Vimeo

    try:
        v = Vimeo(url)
        best_stream = v.best_stream
        filename = f"{v.metadata.title}.mp4" if v.metadata.title else "video.mp4"
        video_path = best_stream.download(download_directory, filename=filename)
        print(f"Video successfully downloaded: {video_path}")
    except Exception as e:
        print(f"Error while downloading the video: {e}")

# Prompt the user to enter the video URL
video_url = input("Enter the video URL: ")

# Prompt the user to choose the destination folder
download_directory = input("Enter the destination folder path (leave empty for current directory): ")
if not download_directory:
    download_directory = os.getcwd()  # Use the current working directory

# Download the video
download_video(video_url, download_directory)
