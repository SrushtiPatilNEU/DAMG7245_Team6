import requests
from bs4 import BeautifulSoup

def extract_and_store_to_markdown(url):
    try:
        # Send a GET request to fetch the HTML content of the page
        response = requests.get(url)
        
        if response.status_code != 200:
            return f"Error: Unable to fetch the page. Status Code: {response.status_code}", []

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content (headings, paragraphs)
        text_content = []
        for element in soup.find_all(['h1', 'h2', 'h3', 'p']):
            text_content.append(element.get_text(strip=True))

        # Extract image URLs
        images = []
        for img in soup.find_all('img'):
            img_url = img.get('src')
            if img_url:
                images.append(img_url)

        # Extract links (anchor tags)
        links = []
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href:
                links.append(f"[{link.get_text(strip=True)}]({href})")

        # Extract tables
        tables = []
        for table in soup.find_all('table'):
            rows = []
            for row in table.find_all('tr'):
                cells = row.find_all(['th', 'td'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                rows.append(row_data)
            if rows:  # Only append non-empty tables
                tables.append(rows)

        # If no data was extracted, return an error message
        if not any([text_content, images, links, tables]):
            return "Error: No data extracted.", []

        # Format the markdown content
        markdown_content = "# Extracted Content\n\n"
        
        # Text Content
        if text_content:
            markdown_content += "## Text Content\n\n"
            for text in text_content:
                markdown_content += f"{text}\n\n"
        
        # Images
        if images:
            markdown_content += "## Images\n\n"
            for img in images:
                markdown_content += f"![Image]({img})\n"
        
        # Links
        if links:
            markdown_content += "## Links\n\n"
            for link in links:
                markdown_content += f"{link}\n"
        
        # Tables
        if tables:
            markdown_content += "## Tables\n\n"
            for table in tables:
                markdown_content += "### Table\n\n"
                for row in table:
                    markdown_content += "| " + " | ".join(row) + " |\n"

        return markdown_content, images

    except Exception as e:
        return f"Error during scraping: {str(e)}", []

# Test function with a URL
if __name__ == "__main__":
    url = "https://www.example.com"  # Replace with your desired URL
    markdown_content, images = extract_and_store_to_markdown(url)

    if markdown_content.startswith("Error"):
        print(markdown_content)  # Print error message
    else:
        # Store to a markdown file
        with open('extracted_data.md', 'w') as file:
            file.write(markdown_content)
        
        # Print the extracted images URLs
        print("Extracted Images:", images)
        print("Markdown content written to extracted_data.md")
