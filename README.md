# YouTube Audio Downloader (yt.py)

Este script permite baixar áudio de vídeos ou playlists do YouTube de forma simples e configurável.

## Funcionalidades

- Download de vídeos únicos ou playlists completas
- Conversão automática para diferentes formatos de áudio (mp3, wav, m4a, flac)
- Configuração de qualidade de áudio
- Controle do número máximo de vídeos a baixar de uma playlist
- Acompanhamento em tempo real do progresso do download
- Gestão automática de caminhos para o FFMPEG
- Interface amigável por linha de comando

## Requisitos

- Python 3.6 ou superior
- Pacotes necessários:
  - yt-dlp
  - ffmpeg (binário externo)

## Instalação

1. Instale as dependências:
```bash
pip install yt-dlp
```

2. Instale o FFMPEG:
   - Windows: Baixe em https://ffmpeg.org/download.html e especifique o caminho usando `--ffmpeg-path`
   - Linux: `sudo apt install ffmpeg` (ou comando equivalente para sua distribuição)
   - Mac: `brew install ffmpeg`

## Uso Básico

```bash
python yt.py URL_DO_VIDEO
```

Exemplo:
```bash
python yt.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Opções Disponíveis

| Opção | Descrição | Padrão |
|-------|-----------|--------|
| `url` | URL do vídeo ou playlist (obrigatório) | - |
| `-o`, `--output` | Diretório onde os arquivos serão salvos | ./downloads |
| `-f`, `--format` | Formato de áudio (mp3, wav, m4a, flac) | mp3 |
| `-q`, `--quality` | Qualidade do áudio em kbps | 192 |
| `-l`, `--limit` | Limitar número de vídeos em uma playlist | Sem limite |
| `--ffmpeg-path` | Caminho para o executável do ffmpeg | Autodetectado |
| `--best-audio` | Baixa a melhor qualidade de áudio disponível | False |

## Exemplos de Uso

### Baixar um único vídeo
```bash
python yt.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Especificar diretório de saída
```bash
python yt.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -o ./minhas_musicas
```

### Baixar em formato WAV com alta qualidade
```bash
python yt.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -f wav -q 320
```

### Baixar os primeiros 5 vídeos de uma playlist
```bash
python yt.py https://www.youtube.com/playlist?list=PL123456789 -l 5
```

### Especificar caminho do FFMPEG
```bash
python yt.py https://www.youtube.com/watch?v=dQw4w9WgXcQ --ffmpeg-path /caminho/para/ffmpeg
```

### Baixar com a melhor qualidade de áudio disponível
```bash
python yt.py https://www.youtube.com/watch?v=dQw4w9WgXcQ --best-audio
```

## Funcionamento Interno

O script utiliza a biblioteca `yt-dlp` (uma versão aprimorada do youtube-dl) para:

1. Extrair informações do vídeo/playlist
2. Realizar o download do arquivo de áudio
3. Processar o arquivo usando FFMPEG para obter o formato desejado
4. Salvar o resultado no diretório especificado

## Resolução de Problemas

### FFMPEG não encontrado
O script tenta localizar automaticamente o FFMPEG em uma localização padrão:
```
C:\Users\steven_mago\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe
```

Se o FFMPEG não for encontrado, use a opção `--ffmpeg-path` para especificar o caminho correto.

### Erros de download
Se ocorrerem erros durante o download, o script exibirá informações detalhadas. Problemas comuns incluem:
- Conexão com a internet instável
- Vídeo/playlist não disponível ou privado
- Problemas de permissão ao criar arquivos no diretório de saída

## Contribuição

Sinta-se à vontade para contribuir com este script:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b minha-nova-feature`)
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`)
4. Envie para a branch (`git push origin minha-nova-feature`)
5. Crie um Pull Request

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Agradecimentos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Fork avançado do youtube-dl
- [FFmpeg](https://ffmpeg.org/) - Framework de processamento de mídia
