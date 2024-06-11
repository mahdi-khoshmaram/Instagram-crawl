import re
import json

name = "victoria"

# ##############################################################################
json_name = f'dataset_{name}.json'
urls = {}
with open(json_name, 'r', encoding='utf-8') as fh:
    jdata = json.load(fh)


for i in range(len(jdata)):
    month = int(jdata[i]["timestamp"].split('-')[1])
    day = int(jdata[i]["timestamp"].split('-')[2].split('T')[0])
    year = int(jdata[i]["timestamp"].split('-')[0])
    if (month in [8, 9, 10, 11 ,12, 1, 2]) and year in [2023, 2024]:
        if month == 2 and day >= 21:
            continue
        if month == 8 and day <= 21:
            continue
        # if month == 9 and day == 5:
        #     continue 
        # (third IF for kia gallery)
        urls[jdata[i]["timestamp"]] = jdata[i]["url"]

urls = {k:urls[k] for k in sorted(urls, reverse = True)}
# # injaaa
keys = list(urls.keys())
for key in keys[2:]:
    del urls[key]
# # injaaa
dates = list(urls.keys())
links = list(urls.values())
print(len(dates))
# ##############################################################################

with open(f'{name}_click_third.txt', 'r', encoding='utf-8') as fh:
    data = fh.read()

print(urls)

# split comments on date
list_of_posts = data.split('-----------------------------------------------date---------------')
# get rid of \n elements in list
for element in list_of_posts:
    if (element == "\n") or (element == ' ') or (element == ''):
        list_of_posts.remove(element)
print(len(list_of_posts))



for id, post in enumerate(list_of_posts):
    num = 1
    pattern1 = r"~{27}\n(.[^*~]+?)\n\*{27}"
    comments_1 = re.findall(pattern1, post, flags=re.DOTALL)
    pattern2 = r"~{27}\n(.+)\n\*{27}"
    comments_2 = re.findall(pattern2, post)
    with open(f"{name}_comments_click_clean.txt", 'a', encoding="utf-8") as fh:
        fh.write(f"\n\n***************************************************")
        fh.write(f"\ndate----> {dates[id]}")
        fh.write(f"\nlink_of_post----> {links[id]}")
        fh.write(f"\n---------------------------------------------------\n")
        for comment in comments_1:
            if comment.strip() == '':
                print(comment)
                continue
            fh.write(f"comment{num}:{comment.strip()}\n")
            num += 1
        for comment in comments_2:
            if comment not in comments_1:
                fh.write(f"comment{num}:{comment.strip()}\n")
                num += 1
    print(f"{dates[id]} is written!")