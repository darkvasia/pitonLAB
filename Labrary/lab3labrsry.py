from typing import List, Dict, Union

class PageIDRegistry:
    _instance = None
    _page_ids = set()

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_unique_id(cls) -> int:
        new_id = len(cls._page_ids) + 1
        cls._page_ids.add(new_id)
        return new_id

class Book:
    def __init__(self, pages: List[str], format: str = "A4"):
        self.pages = pages
        self.format = format

    def add_page(self, content: str):
        self.pages.append(content)

class ScienceBook(Book):
    def __init__(self, pages: List[str], literature: List[str], glossary: Dict[str, str]):
        super().__init__(pages)
        self.literature = literature
        self.glossary = glossary

class Novel(Book):
    def __init__(self, pages: List[str], characters: Dict[str, str]):
        super().__init__(pages)
        self.characters = characters

class Manual(Book):
    def __init__(self, pages: List[str], image: str):
        super().__init__(pages)
        self.image = image

class BookBuilder:
    def __init__(self, book_type: Union[ScienceBook, Novel, Manual], **kwargs):
        self.book = book_type([], **kwargs)

    def add_page(self, content: str):
        page_id = PageIDRegistry().get_unique_id()
        self.book.add_page(f"Page {page_id}: {content}")
        return self

    def build(self):
        return self.book

# Тестування
builder = BookBuilder(Novel, characters={})
novel = builder.add_page("Intro").add_page("Chapter 1").build()

print(novel.pages)
