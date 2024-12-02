import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from ebooklib import epub
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
def init_driver():
    options = Options()
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Use WebDriver Manager to automatically handle driver installation
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def create_ebook(url, book_title):
    driver = init_driver()

    try:
        driver.get(url)
        time.sleep(5)  # Let the page load completely (adjust if needed)

        # Retrieve page source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract content from the article (you may need to inspect the HTML structure)
        content = soup.find('article')  # Look for the <article> tag, which contains the article content
        if content is None:
            print("Could not find the article content on the page.")
            return

        # Initialize the eBook
        book = epub.EpubBook()
        book.set_title(book_title)
        book.set_language('en')

        # Create a chapter for the eBook
        chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml')
        chapter.content = str(content)  # Convert content to string to avoid parsing issues
        book.add_item(chapter)

        # Add metadata for table of contents (optional)
        book.add_item(epub.EpubNav())  # Navigation for the eBook

        # Define spine of the eBook
        book.spine = ['nav', chapter]

        # Write the eBook to a file
        epub.write_epub(f'{book_title}.epub', book, {})

        print(f"eBook '{book_title}.epub' created successfully!")

    except Exception as e:
        print(f"Error creating the eBook: {e}")
    finally:
        driver.quit()

# Example usage
create_ebook('https://medium.com/@tshashwat568/deep-dive-into-json-what-why-ecb36a99623f', 'My eBook2')
