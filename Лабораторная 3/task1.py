class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self,  pages: int):

        if not isinstance(pages, int):
            raise TypeError("pages должна быть типа int ")


        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниы {self.pages}"


class AudioBook(Book):
    def __init__(self,  duration: float):

        if not isinstance(duration, float):
            raise TypeError("duration должна быть типа  float")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

def main():
    pb = PaperBook(10)
    pb.__str__()
    pb.__repr__()

    ab = PaperBook()
    ab.__str__()
    ab.__repr__()

if __name__ == "__main__":
    main()