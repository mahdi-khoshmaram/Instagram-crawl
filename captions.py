save_dir = ''
json_name = f'dataset_{save_dir}.json'



months = {
    "01":"January", "02": "February", "03":"March", "04":"April", "05":"May", "06":"June",
    "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"
        }

# ---------------------------------------------------------------------------------------------

import json 
from tqdm import tqdm

captions = {}

with open(json_name, 'r', encoding='utf-8') as fh:
    data = json.load(fh)

length = len(data)

for i in range(length):
    captions[data[i]["timestamp"]] = data[i]['caption']

# I sort dictionary
captions = {k:captions[k] for k in sorted(captions, reverse = True)}
# print(captions)

# ----------------------------------------------------------------------------------------------
import os, csv


def delete(captions, save_dir=save_dir):
    check_path = {}
    for t, caption in captions.items():
        year = t.split('-')[0]
        month = months[t.split('-')[1]]
        sub_dir = f"{year}-{month}"

        path = f'{save_dir}/{sub_dir}/captions.csv'

        if path not in check_path.keys():
            check_path[path] = 1

        if os.path.exists(path):
            os.remove(path)
            print(" Existing file deleted.")

    return check_path
    

def save_captions(captions, save_dir=save_dir):
    check = delete(captions)
    for t, caption in tqdm(captions.items()):
        # tmp = [t,caption]

        year = t.split('-')[0]
        month = months[t.split('-')[1]]
        sub_dir = f"{year}-{month}"


        os.makedirs(f'{save_dir}/{sub_dir}', exist_ok=True)
        path = f'{save_dir}/{sub_dir}/captions.csv'

        with open(path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if check[path] == 1:
                writer.writerow(["Date", "Caption"])
                check[path] = 0
            writer.writerow([t,caption])

        


save_captions(captions)