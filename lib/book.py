# lib/book.py

class Book:
    def __init__(self, title):
        self.title = title  # uses the property setter
        self._page_count = 0
        self._genre = None

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            print("Title must be a string")

    title = property(get_title, set_title)

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def get_genre(self):
        return self._genre

    def set_genre(self, genre):
        if isinstance(genre, str):
            self._genre = genre
        else:
            print("genre must be a string")

    genre = property(get_genre, set_genre)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
