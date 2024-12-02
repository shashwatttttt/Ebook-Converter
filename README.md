# Ebook-Converter
This repository provides three versions of a Python script that can create an eBook from a webpage (such as a Medium article). The process involves extracting the content from a webpage, converting it into a readable format, and saving it as an EPUB file. The key difference between the scripts is their complexity and the methods used for web scraping, error handling, and eBook creation.

 ## Scripts Overview
 
1. Basic Web Scraping (Level 1) {EbookConvertor.py}
   
This is the simplest version of the script, where the content is extracted using requests and BeautifulSoup. It works well for static web pages where the content 
is directly available in the HTML.

Key Points:

Libraries Used: requests, BeautifulSoup, ebooklib

Process:
- Fetches the HTML content of the page using requests.
- Parses the page with BeautifulSoup to extract the content.
- Converts the extracted content into an EPUB eBook format.
- Limitations: This approach may not work with pages that load content dynamically via JavaScript.

2. Improved Web Scraping with Dynamic Content Handling (Level 2) {EbookConvertor2.py}
   
This version uses Selenium to handle dynamic content (JavaScript-rendered pages), making it more robust for modern websites like Medium. It waits for the page to load fully before scraping.

Key Points:

- Libraries Used: requests, BeautifulSoup, selenium, webdriver-manager, ebooklib
  
Process:

- Uses selenium for handling JavaScript content.
- Waits for content to load completely and retrieves the page source.
- Extracts and processes content, then creates the eBook in EPUB format.
- Advantages: Works on modern websites that rely on JavaScript to render content.

3. Enhanced Web Scraping with Error Handling and Clean Content (Level 3) {EbookConvertor3.py}
   
The third version enhances the second script by adding better error handling and ensuring cleaner content extraction. This version also includes optimizations for page load time and content extraction.

Key Points:
- Libraries Used: requests, selenium, BeautifulSoup, ebooklib, webdriver-manager
Process:

- Same as Level 2 but with added error handling and cleaner content parsing.
- Uses WebDriverWait for better control over the dynamic loading of elements.
- Ensures that only clean, readable content is added to the eBook.
- Advantages: This is the most reliable version, designed for a wider range of websites with both static and dynamic content.

### Requirements
To run these scripts, you will need the following Python packages:

- requests
- BeautifulSoup (from bs4)
- selenium
- webdriver-manager
- ebooklib
- time

You can install these dependencies using the following command:

code: pip install requests beautifulsoup4 selenium webdriver-manager ebooklib

#### Selenium Dependencies:

ChromeDriver: The script automatically manages ChromeDriver with webdriver-manager, but ensure that Google Chrome is installed on your machine.


## Conclusion
Level 1:

- Suitable for Static pages with simple HTML content.
- Limitation: Doesn’t handle JavaScript content.

Level 2:

- Suitable for Dynamic pages with JavaScript-rendered content (e.g., Medium articles).
- Improvement: Selenium is used to render dynamic content before scraping.
  
Level 3:

- Suitable for Advanced use cases with full error handling and more control over dynamic content.
- Improvement: Incorporates WebDriverWait for better element loading and cleaner content extraction.
- Use these scripts based on the complexity of the website you are targeting. Level 1 is good for simpler, static pages, while Level 3 provides the most reliable and 
  robust approach for handling modern web pages with dynamic content.
