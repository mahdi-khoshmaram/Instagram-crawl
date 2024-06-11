import json 
def links(save_dir):
    json_name = f'dataset_{save_dir}.json'
    urls = {}
    with open(json_name, 'r', encoding='utf-8') as fh:
        data = json.load(fh)


    for i in range(len(data)):
        month = int(data[i]["timestamp"].split('-')[1])
        day = int(data[i]["timestamp"].split('-')[2].split('T')[0])
        if month in [1, 2, 8, 9, 10, 11 ,12]:
            if month == 2 and day > 20:
                continue
            if month == 8 and day <= 22:
                continue
            urls[data[i]["timestamp"]] = data[i]["url"]

    urls = {k:urls[k] for k in sorted(urls, reverse = True)}
    print(f"{len(urls.keys())} post links have found!")
    return urls