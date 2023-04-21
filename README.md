# PodcastsDownloader

This is a Python script that downloads your podcasts.

### Getting Started

1. Download the required dependencies by running the following command:

```bash
$ pip install -r requirements.txt
```

2. Edit the `data.json` file with the following structure:
```json
{
    "Name": {
        "url": "rss url",
        "count": 0
    }
}
```
The `"count"` key stores the number of podcasts you have already downloaded.

3. Create a download directory with the same name as your `data.json` file:

Create a directory named `podcasts/name`.

4. Run the script with the following command:
```bash
$ python main.py
```
