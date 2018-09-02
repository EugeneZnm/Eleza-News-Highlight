class Sources:
    """
    Sources class to define source objects

    """
    def __init__(self, id, name, description, url, category, language, country):
        """
        passing parameters into object Sources

        """
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

    def __init__(self, id, author, title, description, url, urlToImage, publishedAt):
        """
        Passing parameters into the source articles

        """
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

