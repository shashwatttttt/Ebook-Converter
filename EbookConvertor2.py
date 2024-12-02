from selenium import webdriver
from bs4 import BeautifulSoup
from ebooklib import epub

def create_ebook(url, book_title):
    driver = webdriver.Chrome()  # You can use other drivers as well
    driver.get(url)

    # Wait for the page to load completely (or use WebDriverWait for specific elements)
    driver.implicitly_wait(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    book = epub.EpubBook()
    book.set_title(book_title)

    # Extract the main content (this is where you may need to adjust the selector)
    content = soup.find('article')  # Assuming the content is in <article> tag

    chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml')
    chapter.content = str(content)  # Make sure to convert the content to a string
    book.add_item(chapter)

    book.spine = ['nav', chapter]
    epub.write_epub(f'{book_title}.epub', book, {})

create_ebook('https://medium.com/@tshashwat568/deep-dive-into-json-what-why-ecb36a99623f', 'My eBook')
