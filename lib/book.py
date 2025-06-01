# lib/book.py

class Book:
    def __init__(self, title):
        self.title = title
        self.page_count = 0
        self.genre = None

    def get_title(self):
        return self._title

    def set_title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise TypeError("Title must be a string")

    title = property(get_title, set_title)

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            raise TypeError("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def get_genre(self):
        return self._genre

    def set_genre(self, value):
        if isinstance(value, str):
            self._genre = value
        else:
            raise TypeError("genre must be a string")

    genre = property(get_genre, set_genre)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
