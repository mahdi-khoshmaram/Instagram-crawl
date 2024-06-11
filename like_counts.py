
save_dir = ''
json_name = f'dataset_{save_dir}.json'

months = {
    "01":"January", "02": "February", "03":"March", "04":"April", "05":"May", "06":"June",
    "07":"July", "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"
        }

# ---------------------------------------------------------------------------------------------

import json 
from tqdm import tqdm

likes = {}

with open(json_name, 'r', encoding='utf-8') as fh:
    data = json.load(fh)

length = len(data)

for i in range(length):
    likes[data[i]["timestamp"]] = data[i]['likesCount']

# I sort dictionary
likes = {k:likes[k] for k in sorted(likes, reverse = True)}

# print(likes)
# ----------------------------------------------------------------------------------------------
import os, csv



def delete(likes, save_dir=save_dir):
    check_path = {}
    for t, like in likes.items():
        year = t.split('-')[0]
        month = months[t.split('-')[1]]
        sub_dir = f"{year}-{month}"

        path = f'{save_dir}/{sub_dir}/likes.csv'

        if path not in check_path.keys():
            check_path[path] = 1

        if os.path.exists(path):
            os.remove(path)
            print(" Existing file deleted.")

    return check_path
    

def save_likes(likes, save_dir=save_dir):
    check = delete(likes)
    for t, like in tqdm(likes.items()):
        # tmp = [t,like]

        year = t.split('-')[0]
        month = months[t.split('-')[1]]
        sub_dir = f"{year}-{month}"


        os.makedirs(f'{save_dir}/{sub_dir}', exist_ok=True)
        path = f'{save_dir}/{sub_dir}/likes.csv'

        with open(path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if check[path] == 1:
                writer.writerow(["Date", "like"])
                check[path] = 0
            writer.writerow([t,like])

        


save_likes(likes)