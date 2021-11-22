import hackernews


news_client = hackernews.hn.NewsClient()
stories = news_client.get_best_story(fetchMax=10)

for story in stories:
    print(story.title)

