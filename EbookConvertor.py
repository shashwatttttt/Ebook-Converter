import requests
from bs4 import BeautifulSoup
from ebooklib import epub


def create_ebook(url, book_title):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    book = epub.EpubBook()
    book.set_title(book_title)

    chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml')
    chapter.content = soup.prettify()
    book.add_item(chapter)

    book.spine = ['nav', chapter]
    epub.write_epub(f'{book_title}.epub', book, {})


create_ebook('https://medium.com/@tshashwat568/deep-dive-into-json-what-why-ecb36a99623f', 'My eBook')