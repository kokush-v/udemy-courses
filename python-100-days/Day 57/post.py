class Post:
    def __init__(self, blog_id: str, title: str, subtitle: str, body: str) -> None:
        self.id = blog_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
