#!/usr/bin/env python3
"""
YouTube Downloader Script
Este script utiliza yt-dlp para baixar vídeos/playlists do YouTube em formato de áudio.
"""

import os
import sys
import argparse
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

def setup_argparse():
    """Configura os argumentos de linha de comando."""
    parser = argparse.ArgumentParser(description='Download de áudio de vídeos do YouTube')
    
    parser.add_argument('url', help='URL do vídeo ou playlist do YouTube')
    parser.add_argument('-o', '--output', default='./downloads', 
                        help='Diretório de saída para os arquivos (padrão: ./downloads)')
    parser.add_argument('-f', '--format', default='mp3', 
                        choices=['mp3', 'wav', 'm4a', 'flac'],
                        help='Formato de áudio (padrão: mp3)')
    parser.add_argument('-q', '--quality', default='192', 
                        help='Qualidade do áudio (padrão: 192)')
    parser.add_argument('-l', '--limit', type=int, default=None,
                        help='Limitar o número de vídeos a baixar da playlist')
    parser.add_argument('--ffmpeg-path', default=None,
                        help='Caminho para o executável do ffmpeg')
    parser.add_argument('--best-audio', action='store_true',
                        help='Baixar a melhor qualidade de áudio disponível')
    
    return parser.parse_args()

def download_from_youtube(url, output_dir='./downloads', audio_format='mp3', 
                         quality='192', limit=None, ffmpeg_path=None, best_audio=False):
    """
    Baixa áudio do YouTube usando yt-dlp.
    
    Args:
        url (str): URL do vídeo ou playlist
        output_dir (str): Diretório onde os arquivos serão salvos
        audio_format (str): Formato do áudio (mp3, wav, etc.)
        quality (str): Qualidade do áudio (kbps)
        limit (int, opcional): Limite de vídeos a baixar da playlist
        ffmpeg_path (str, opcional): Caminho para o executável do ffmpeg
        best_audio (bool): Se True, baixa a melhor qualidade de áudio disponível
    
    Returns:
        bool: True se o download foi bem-sucedido, False caso contrário
    """
    # Criar diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Configurar opções do yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best' if best_audio else 'worstaudio/worst',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': quality,
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'verbose': True,
        'progress_hooks': [progress_hook],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
    }
    
    # Adicionar caminho do ffmpeg se fornecido
    if ffmpeg_path:
        ydl_opts['ffmpeg_location'] = ffmpeg_path
    
    # Limitar o número de vídeos se fornecido
    if limit is not None:
        ydl_opts['playlistend'] = limit
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Mostrar informações sobre o que será baixado
            if 'entries' in info:
                # Playlist
                playlist_title = info.get('title', 'Playlist desconhecida')
                num_videos = min(len(info['entries']), limit or float('inf'))
                print(f"\nBaixando playlist: {playlist_title}")
                print(f"Número de vídeos: {num_videos}\n")
            else:
                # Vídeo único
                print(f"\nBaixando vídeo: {info.get('title', 'Título desconhecido')}\n")
            
            # Realizar o download
            ydl.download([url])
            return True
    
    except DownloadError as e:
        print(f"\nErro durante o download: {e}")
        return False
    except Exception as e:
        print(f"\nErro inesperado: {e}")
        return False

def progress_hook(d):
    """Exibe o progresso do download."""
    if d['status'] == 'downloading':
        percentage = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        filename = os.path.basename(d.get('filename', 'desconhecido'))
        
        print(f"\rBaixando {filename}: {percentage} a {speed}, ETA: {eta}", end='')
    
    elif d['status'] == 'finished':
        print(f"\nDownload concluído. Convertendo para o formato solicitado...")

def main():
    """Função principal que executa o script."""
    args = setup_argparse()
    
    print("\n=== YouTube Audio Downloader ===\n")
    
    # Definir o caminho do ffmpeg padrão se não for fornecido
    if not args.ffmpeg_path and os.path.exists(r"C:\Users\steven_mago\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"):
        args.ffmpeg_path = r"C:\Users\steven_mago\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"
    
    # Resumo das configurações
    print(f"URL: {args.url}")
    print(f"Formato: {args.format}")
    print(f"Qualidade: {args.quality} kbps")
    print(f"Diretório de saída: {os.path.abspath(args.output)}")
    if args.limit:
        print(f"Limite de vídeos: {args.limit}")
    if args.ffmpeg_path:
        print(f"Usando ffmpeg em: {args.ffmpeg_path}")
    print(f"Qualidade de áudio: {'Melhor' if args.best_audio else 'Padrão'}")
    
    # Iniciar download
    print("\nIniciando download...\n")
    success = download_from_youtube(
        args.url, 
        args.output, 
        args.format, 
        args.quality, 
        args.limit, 
        args.ffmpeg_path,
        args.best_audio
    )
    
    if success:
        print("\n✅ Download concluído com sucesso!")
    else:
        print("\n❌ Ocorreram erros durante o download.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
