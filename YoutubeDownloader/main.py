from pytube import Playlist
import os

# ------------------YOUTUBE PLAYLIST DOWNLOADER------------------


def youtube_playlist_downloader(playlist, folder):
    # looping through all the videos in the playlist and downloading them as mp4 and then converting to mp3
    video_number = 0
    for video in playlist.videos:
        video_number += 1
        # download video as mp4
        out_file = video.streams.filter(only_audio=True).first().download(output_path=folder)
        # convert to mp3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        # result of great success
        print(str(video_number)+'.'+video.title + " has been successfully downloaded.")


if __name__ == '__main__':
    # destination folder of downloads
    folder = 'C:\\Users\\osfpg\\Desktop'  # my dir
    # the playlist to be downloaded
    playlist = Playlist("https://www.youtube.com/playlist?list=PLsezUnEDzFMVgl3hXQJBrEFb8P3CunBm6")  # example playlist

    youtube_playlist_downloader(playlist, folder)




