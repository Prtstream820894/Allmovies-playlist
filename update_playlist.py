import requests

# Aapke 4 Cloudflare Workers ke links
PLAYLIST_URLS = [
    "https://allmovieslist.poonamchouhan076.workers.dev/",
    "https://old-shape-1bd3.poonamchouhan076.work",
    "https://divine-moon-058f.poonamchouhan076.workers.dev/",
    "https://hdhub4u-lake-f103.poonamchouhan076.work"
]

def fetch_and_merge():
    combined_content = "#EXTM3U\n"
    
    for url in PLAYLIST_URLS:
        try:
            print(f"Fetching from: {url}")
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                text = response.text.strip()
                # Har playlist ka #EXTM3U hata kar baaki ka raw data safely extract karenge
                lines = text.splitlines()
                playlist_data = []
                for line in lines:
                    if line.strip() and not line.startswith("#EXTM3U"):
                        playlist_data.append(line)
                
                if playlist_data:
                    combined_content += "\n".join(playlist_data) + "\n"
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # Final merged file ko save karna (Jaise 'playlist.m3u')
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(combined_content)
    print("Playlist successfully merged and saved as playlist.m3u!")

if __name__ == "__main__":
    fetch_and_merge()
  
