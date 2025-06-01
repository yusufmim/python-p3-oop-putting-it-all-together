# lib/book.py

class Book:
    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            print("Title must be a non-empty string")

    title = property(get_title, set_title)
