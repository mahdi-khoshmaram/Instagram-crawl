save_dir = ''
json_name = f'dataset_{save_dir}.json'




months = {
    "01":"January", "02": "February", "03":"March", "04":"April", "05":"May", "06":"June",
    "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"
        }

# ---------------------------------------------------------------------------------------------

import json 
from tqdm import tqdm

videos = {}

with open(json_name, 'r', encoding='utf-8') as fh:
    data = json.load(fh)

length = len(data)
for i in range(length):
    try:
        videos[data[i]["timestamp"]] = data[i]['videoUrl']
    except:
        continue

# I sort dictionary
videos = {k:videos[k] for k in sorted(videos, reverse = True)}

# ------------------------------------------------------------------------------------------------

# downloading phase
import requests
import os


def save_videos_from_links(videos, save_dir=save_dir):
    id = 1
    for t, link in tqdm(videos.items()):

        year = t.split('-')[0]
        month = months[t.split('-')[1]]
        sub_dir = f"{year}-{month}"


        try:
            response = requests.get(link, stream=True)
            if response.status_code == 200:

                date = t.split('T')[0]
                time = t.split('T')[1].split('.')[0].split(':')

                file_name = f"{date}_{time[0]}_{time[1]}_{time[2]}"

                os.makedirs(f'{save_dir}/{sub_dir}', exist_ok=True)

                path = f'{save_dir}/{sub_dir}/{file_name}.mp4'

                if os.path.exists(path):
                    print(f"video {file_name} already exists, skipping...")
                    continue

                with open(path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                    print(f"video {id} saved as {path}")

                    id += 1
            else:
                print(f"Failed to download video {id}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


save_videos_from_links(videos)

    

