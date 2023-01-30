import json
import requests

# driver_path = '/usr/bin/chromedriver'


class YouTubeComments:
    def __init__(self, video_id):
        self.video_id = video_id
        self.comments = []
#@json.load
    def get_comments(self):
        url = f"https://www.youtube.com/watch?v={self.video_id}"
        response = requests.get(url)
        print(response)

        # extract the JSON data from the page source
        start = response.text.find("<script") # ("<script>")
        end = response.text.find("</script>") + 9 # ("</script>", start)
        json_text = response.text[start:end] # [start:end]
        print()

        json_data = json.loads(json_text)
        # retrieve the comments from the JSON data
        for item in json_data["contents"]["twoColumnWatchNextResults"]["secondaryResults"]["secondaryResults"][
            "results"
        ]:
            if "comments" in item:
                for comment in item["comments"]["comments"]:
                    author = comment["authorDisplayName"]
                    text = comment["textDisplay"]
                    self.comments.append((author, text))

    def iter(self):
        self.get_comments()
        for comment in self.comments:
            yield comment


video_id ="tcHiprXQMmk"
ytc1 = YouTubeComments(video_id)

comments = [c for c in ytc1.get_comments()]
print(comments)
