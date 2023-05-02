import re
import requests
from bs4 import BeautifulSoup


def get_text(url):
    # To extract all text from a website in Python, you can use the BeautifulSoup library. Here are the steps to do so:
    # Install BeautifulSoup by running !pip install beautifulsoup4 in your terminal or Jupyter Notebook.
    # Import the necessary libraries:
    # Use the requests library to get the HTML content of the website:
    response = requests.get(url)
    html_content = response.text
    # Use BeautifulSoup to parse the HTML content and remove unwanted elements such as scripts and styles:
    soup = BeautifulSoup(html_content, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    # Use the get_text() method to extract only the text from the parsed HTML content:
    text = soup.get_text()
    # Finally, you can further process the extracted text as needed, such as splitting it into lines:
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    # That's it! You should now have all the text content from the website in the text variable.
    text = re.sub('\s{2,}', ' ', text).strip()
    return text

if __name__ == "__main__":
    print(get_text("https://en.wikipedia.org/wiki/Guru_Tegh_Bahadur"))