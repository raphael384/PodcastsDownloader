import requests
import feedparser
import json
import re

# load data
with open("data.json", 'r') as file:
    data = json.load(file)

# iterate through podcast list
for name, podcast in data.items():

    # connect to rss
    rss = feedparser.parse(podcast['url'])

    # count podcasts
    count = len(rss.entries)

    print(f"Online podcasts for {name}: {count}")

    # compute difference
    dif = count - podcast['count']

    # check the difference
    if dif > 0:
        print(f"There are {dif} podcasts not downloaded")

        # download new podcasts
        for entry in rss.entries[:dif]:
            
            # rename for Windows
            entry_title = re.sub(r'[<>:"/\\|?*]', '', entry.title)

            print(f"\n---> Download file: {entry_title}\n")
            doc = requests.get(entry.enclosures[0].href)
            with open(f'podcasts/{name}/{entry_title}.mp3', 'wb') as f:
                f.write(doc.content)

        # update the count in the JSON file
        data[name]['count'] = count
        with open("data.json", "w") as file:
            json.dump(data, file)

    else:
        print(f"Up to date for {name}")
