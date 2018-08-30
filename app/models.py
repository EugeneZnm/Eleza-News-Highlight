class Sources:
    """
    Sources class to define source objects

    """
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:
    """
    Class article to define article objects

    """
    # list item to hold articles
    all_articles = []

    def __init__(self, source_id, source_name, author, title, description, url, urlToImage, publishedAt ):
        self.source_id = source_id
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


