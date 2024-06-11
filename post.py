save_dir = ''
json_name = f'dataset_{save_dir}.json'


import json 

image_links = {}
with open(json_name, 'r', encoding='utf-8') as fh:
    data = json.load(fh)


for i in range(len(data)):
    image_links[data[i]["timestamp"]] = data[i]["displayUrl"]

image_links = {k:image_links[k] for k in sorted(image_links, reverse = True)}
print(len(image_links))

# ---------------------------------------------------------------------

month = {
    "01":"January", "02": "February", "03":"March", "04":"April", "05":"May", "06":"June",
    "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"
        }

# ---------------------------------------------------------------------

import requests
import os


def save_images_from_links(image_links, save_dir = save_dir):
    id = 1
    for t, link in image_links.items():
        sub = f"{t.split('-')[0]}-{month[t.split('-')[1]]}"
        try:
            response = requests.get(link)
            if response.status_code == 200:
                date = t.split('T')[0]
                time = t.split('T')[1].split('.')[0].split(':')
                file_name = f"{date}_{time[0]}_{time[1]}_{time[2]}"
                os.makedirs(f'{save_dir}/{sub}', exist_ok=True)
                path = f'{save_dir}/{sub}/{file_name}.jpg'
                with open(path, 'wb') as f:
                    f.write(response.content)
                    print(f"Image {id} saved as {path}")

                    id += 1
            else:
                print(f"Failed to download image {id}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


save_images_from_links(image_links)