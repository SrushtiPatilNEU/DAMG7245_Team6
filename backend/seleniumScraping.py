from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

def selenium_scraping(url):
    # Initialize WebDriver (Ensure you have ChromeDriver installed and configured)
    try:
        driver = webdriver.Chrome()  # You can replace this with any WebDriver (e.g., geckodriver for Firefox)
    except Exception as e:
        return f"Error initializing WebDriver: {str(e)}", []

    driver.get(url)

    # Wait for the page to load completely
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

    markdown_content = "# Extracted Content from {url}\n\n"
    images = []  # To hold image URLs

    # Extract and save text content (headings and paragraphs)
    markdown_content += "## Text Content\n\n"
    elements = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //p")
    for element in elements:
        markdown_content += f"{element.text.strip()}\n\n"

    # Extract and save tables
    markdown_content += "## Tables\n\n"
    tables = driver.find_elements(By.TAG_NAME, "table")
    for table_index, table in enumerate(tables, start=1):
        markdown_content += f"### Table {table_index}\n\n"
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text.strip() for col in columns]
            markdown_content += "| " + " | ".join(row_data) + " |\n"
        markdown_content += "\n"

    # Extract and save links
    markdown_content += "## Links\n\n"
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        if href:
            markdown_content += f"- [Link]({href})\n"
    markdown_content += "\n"

    # Extract and save images
    markdown_content += "## Images\n\n"
    images = driver.find_elements(By.TAG_NAME, "img")
    image_urls = []
    for index, image in enumerate(images, start=1):
        img_url = image.get_attribute("src")
        if img_url:
            try:
                headers = {"User-Agent": "Mozilla/5.0"}
                img_data = requests.get(img_url, headers=headers).content
                img_name = f"image_{index}.jpg"
                
                # Return image URL
                image_urls.append(img_url)
            except Exception as e:
                markdown_content += f"Error downloading image: {e}\n"

    markdown_content += "\n"

    # Close the WebDriver
    driver.quit()

    return markdown_content, image_urls
