import re, json

name = 'nike'

# ##############################################################################
json_name = f'dataset_{name}.json'
urls = {}
with open(json_name, 'r', encoding='utf-8') as fh:
    jdata = json.load(fh)


for i in range(len(jdata)):
    month = int(jdata[i]["timestamp"].split('-')[1])
    day = int(jdata[i]["timestamp"].split('-')[2].split('T')[0])
    year = int(jdata[i]["timestamp"].split('-')[0])
    if (month in [8, 9, 10, 11, 12, 1, 2]) and year in [2023, 2024]:
    # if (month in [9, 10, 11 ,12, 1, 2]) and year in [2023, 2024]:
        if month == 2 and day >= 21:
            continue
        if month == 8 and day <= 22:
            continue
        # if month == 9 and day == 5:
        #     continue 
        # (third IF for kia gallery)
        urls[jdata[i]["timestamp"]] = jdata[i]["url"]

urls = {k:urls[k] for k in sorted(urls, reverse = True)}
dates = list(urls.keys())
links = list(urls.values())
print(f"len json ---> {len(dates)}")
print(f"urls:\n{urls}")
# ##############################################################################

# with open(f"{name}_comments_drag_dirty_replaced.txt", encoding='utf-8') as fh:
#     data = fh.read()

# pattern_date = "^date:"
# posts_list = re.split(pattern_date, data, flags=re.MULTILINE)
# # print(posts_list)

# for i in posts_list: 
#     if i.strip() == '' or i == None or i.strip() == '':
#         posts_list.remove(i)
# # print(posts_list[0])
# print(f"len of draged posts ---> {len(posts_list)}")
# # -------------------------------------------------------------------------------
# check = False
# for id, post in enumerate(posts_list):
#     num = 0
#     pattern = "\*~\*~\*~\*~\*~\*~\*~\*~\*~\*~\*~\*~"
#     comments_list_per_post = re.split(pattern, post)
#     # print(comments_list_per_post)
#     if (dates[0].strip() != comments_list_per_post[0].strip()) and (check == False):
#         print([dates[0],comments_list_per_post[0].strip()])
#         print("\n-------------------Dates do not match!-------------------")
#         print(f"dates[0] = {dates[0].strip()}")
#         print(f"comments_list_per_post[0] = {comments_list_per_post[0].strip()}")
#         # print(post)
#         break
#     elif (dates[0].strip() == comments_list_per_post[0].strip()) and (check == False):
#         print("\n-------------------dates validated!-------------------")
#     check = True
#     with open(f"{name}_comments_drag_clean.txt", 'a', encoding="utf-8") as fh:
#         fh.write(f"\n\n***************************************************")
#         fh.write(f"\ndate----> {dates[id]}")
#         fh.write(f"\nlink_of_post----> {links[id]}")
#         fh.write(f"\n---------------------------------------------------\n")
#         first_element = True
#         for comment in comments_list_per_post:
#             if comment.strip() == '':
#                 continue
#             if first_element == True:
#                 first_element = False
#                 continue
#             fh.write(f"comment{num}:{comment.strip()}\n")
#             num += 1
#             # print(f"{dates[id]} is written!")