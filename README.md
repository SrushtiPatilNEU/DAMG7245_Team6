
📌 Project Documentation: Open-Source vs. Enterprise Solutions for PDF Processing & Web Scraping
 Project Summary
This project aims to compare and document the efficiency, accuracy, and scalability of open-source vs. enterprise solutions for PDF processing and web scraping and store the data into AWS S3 bucket.

 Problem Statement
The objective of this assignment is to evaluate and compare open-source and enterprise solutions for PDF processing and web scraping by developing a structured documentation framework and Storing it in the AWS S3 Bucket.


 Project Goal
The goal of this project is to compare and document the efficiency of open-source vs. enterprise solutions for PDF processing and web scraping by generating structured datasets. The project will:
Extract and structure data from PDFs and websites using open-source (PyMuPDF, Selenium) and enterprise solutions (Azure AI Document Intelligence, ScrapingBee).
Create well-organized datasets from the extracted data for further analysis.
Provide a detailed comparative analysis covering performance, accuracy, cost, and scalability trade-offs.
Document the entire process in a structured GitHub repository with a proof-of-concept demo and AI Use Disclosure.

Technology Used
Frontend: Streamlit
Backend: FastAPI
FastAPI  deployment : Render
APIs & Tools:
📄 PDF Processing
PyMuPDF (open-source)
Azure AI Document Intelligence (enterprise)
🌐 Web Scraping
Selenium (open-source)
ScrapingBee (enterprise)
📜 Documentation & Visualization
Markdown (for structured documentation)
Docking ( for structure documentation)
GitHub Pages (for hosting documentation)
 Proof of Concept (PoC)
To validate the feasibility of using open-source and enterprise tools for PDF processing and web scraping, the following tasks will be performed:
✅ PDF Extraction Tests:
Use PyMuPDF to extract text and images from PDFs and store results in a structured format.
Use Azure AI Document Intelligence to process complex documents and compare accuracy.
✅ Web Scraping Tests:
Use Selenium to automate the extraction of structured data from websites.
Use ScrapingBee to test large-scale, API-based web scraping.
✅ Comparative Analysis:
Measure processing speed, accuracy, scalability, and ease of use.
Document findings in a side-by-side comparison with pros and cons.

✅ Final Demonstration:
Showcase results through a demo video, GitHub repository, and AI Use Disclosure.

Architecture Diagram



Features How to run the Application locally
Create a Python Virtual environment
Run -> pip install -r requirements.txt
Then run FastAPI (uvicorn backend.app:app)
Then run Streamlit (streamlit run dashboard.py)


Project Structure

'
├── Documentation
│   └── ToolComparison.docx
├── __pycache__
│   ├── auth.cpython-313.pyc
│   ├── azurePdfScraping.cpython-312.pyc
│   ├── azurePdfScraping.cpython-313.pyc
│   ├── doclingScraping.cpython-312.pyc
│   ├── doclingScraping.cpython-313.pyc
│   ├── openSourcePdf.cpython-312.pyc
│   ├── openSourcePdf.cpython-313.pyc
│   ├── scrapingBee.cpython-312.pyc
│   ├── scrapingBee.cpython-313.pyc
│   ├── selenium.cpython-312.pyc
│   ├── seleniumScraping.cpython-312.pyc
│   └── seleniumScraping.cpython-313.pyc
├── backend
│   ├── __pycache__
│   │   ├── app.cpython-313.pyc
│   │   ├── azurePdfScraping.cpython-313.pyc
│   │   ├── doclingScraping.cpython-313.pyc
│   │   ├── openSourcePdf.cpython-313.pyc
│   │   ├── scrapingBee.cpython-313.pyc
│   │   └── seleniumScraping.cpython-313.pyc
│   ├── app.py
│   ├── azurePdfScraping.py
│   ├── extracted_data.md
│   ├── file.pdf
│   ├── openSourcePdf.py
│   ├── scrapingBee.py
│   └── seleniumScraping.py
├── diagrams
│   ├── ai_application_data_pipeline.png
│   ├── architecture_diagram.ipynb
│   ├── azure.png
│   ├── docling.png
│   ├── markitdown.png
│   ├── pymupdf.png
│   ├── scrapingbee.png
│   ├── selenium.png
│   └── streamlit.png
├── directory_structure.txt
├── doclingScraping.py
├── frontend
│   └── dashboard.py
├── requirements.txt
├── venv
│   ├── bin
│   │   ├── Activate.ps1
│   │   ├── __pycache__
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── dotenv
│   │   ├── f2py
│   │   ├── fastapi
│   │   ├── jp.py
│   │   ├── jsonschema
│   │   ├── markdown-it
│   │   ├── normalizer
│   │   ├── numpy-config
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.13
│   │   ├── pygmentize
│   │   ├── pymupdf
│   │   ├── python -> python3.13
│   │   ├── python3 -> python3.13
│   │   ├── python3.13 -> /Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13
│   │   ├── streamlit
│   │   ├── streamlit.cmd
│   │   ├── uvicorn
│   │   └── wsdump
│   ├── etc
│   │   └── jupyter
│   ├── include
│   │   └── python3.13
│   ├── lib
│   │   └── python3.13
│   ├── pyvenv.cfg
│   └── share
│       └── jupyter
└── vercel.json
'
18 directories, 65 files



Key Features & Deliverables
✅ Key Features
✔ Open-Source vs. Enterprise Comparison – Evaluate trade-offs between cost, performance, and scalability.
 ✔ PDF Text & Data Extraction – Process structured/unstructured PDF content.
 ✔ Web Scraping Automation – Extract structured data from websites efficiently.
 ✔ Detailed Documentation – Step-by-step setup, API usage, and findings.
📦 Final Deliverables
GitHub Repository with structured documentation and code.
Comparative Report with key insights, pros & cons.
5-minute Demo Video showcasing the PoC and key findings.
AI Use Disclosure detailing AI tools used and their impact.

Future Enhancements

🚀 Future Enhancements
Airflow Integration: Make scraping and extraction processes run automatically.
Chatbots driven by LLM: Create a chatbot that can respond to queries based on documents that have been extracted.
Knowledge Base: Create a collection of subjects and information gleaned from papers.

Team Information

Pranjal Mahajan(002375449)
33.33%
Srushti Patil (002345025)  
33.33%
Ram Putcha (002304724
33.33%



