from yt_dlp import YoutubeDL



def download_playlist(playlist_url, limit=None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    if limit is not None:
        ydl_opts['playlistend'] = limit
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
   


playlist_url = 'https://www.youtube.com/watch?v=V7xQd3yt590&list=RDV7xQd3yt590&start_radio=1&rv=V7xQd3yt590&t=3'
download_playlist(playlist_url,limit=3)
