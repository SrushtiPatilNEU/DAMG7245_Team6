import logging
import time
import tempfile
from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from docling.datamodel.base_models import InputFormat
from docling.document_converter import PdfFormatOption
from markitdown import MarkItDown

# Setup logging
logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)

IMAGE_RESOLUTION_SCALE = 2.0

def docling_pdf_to_markdown(input_pdf_path: Path, output_dir: Path):
    """ Converts a PDF document to markdown and extracts images using Docling. """
    # PdfPipelineOptions configuration
    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True

    doc_converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
    )

    start_time = time.time()

    # Convert PDF
    conv_res = doc_converter.convert(input_pdf_path)

    if conv_res is None:
        _log.error(f"Failed to convert PDF: {input_pdf_path}")
        return

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    doc_filename = conv_res.input.file.stem

    # Save page images
    save_page_images(conv_res, output_dir, doc_filename)

    # Save images of figures and tables
    save_images_of_elements(conv_res, output_dir, doc_filename)

    # Save markdown files (embedded and referenced images)
    save_markdown_with_images(conv_res, output_dir, doc_filename)

    end_time = time.time() - start_time
    _log.info(f"Document converted and figures exported in {end_time:.2f} seconds.")

def save_page_images(conv_res, output_dir: Path, doc_filename: str):
    """ Save the images of each page. """
    for page_no, page in conv_res.document.pages.items():
        page_image_filename = output_dir / f"{doc_filename}-{page_no}.png"
        with page_image_filename.open("wb") as fp:
            page.image.pil_image.save(fp, format="PNG")

def save_images_of_elements(conv_res, output_dir: Path, doc_filename: str):
    """ Save images of tables and pictures. """
    table_counter = 0
    picture_counter = 0
    for element, _level in conv_res.document.iterate_items():
        if isinstance(element, TableItem):
            table_counter += 1
            element_image_filename = output_dir / f"{doc_filename}-table-{table_counter}.png"
            with element_image_filename.open("wb") as fp:
                element.get_image(conv_res.document).save(fp, "PNG")

        if isinstance(element, PictureItem):
            picture_counter += 1
            element_image_filename = output_dir / f"{doc_filename}-picture-{picture_counter}.png"
            with element_image_filename.open("wb") as fp:
                element.get_image(conv_res.document).save(fp, "PNG")

def save_markdown_with_images(conv_res, output_dir: Path, doc_filename: str):
    """ Save the markdown with embedded or referenced images. """
    # Markdown with embedded images
    md_filename = output_dir / f"{doc_filename}-with-images.md"
    conv_res.document.save_as_markdown(md_filename, image_mode=ImageRefMode.EMBEDDED)

    # Markdown with externally referenced images
    md_filename = output_dir / f"{doc_filename}-with-image-refs.md"
    conv_res.document.save_as_markdown(md_filename, image_mode=ImageRefMode.REFERENCED)

    # HTML with externally referenced images
    html_filename = output_dir / f"{doc_filename}-with-image-refs.html"
    conv_res.document.save_as_html(html_filename, image_mode=ImageRefMode.REFERENCED)

def save_extracted_data_as_markdown(content: str, filename="output_markitdown.md"):
    """ Helper function to save extracted text content into a markdown file. """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def markitdown_pdf_to_text(input_pdf_path: Path):
    """ Extracts text from a PDF using MarkItDown. """
    md = MarkItDown()
    try:
        result = md.convert(input_pdf_path)
        if result is None:
            _log.error(f"Failed to extract text from PDF: {input_pdf_path}")
            return None
        _log.info("Text content extracted using MarkItDown.")
        return result.text_content
    except Exception as e:
        _log.error(f"Error during conversion: {e}")
        return None

def docling_extract(pdf_file):
    """ Function to handle the extraction from uploaded PDF file. """
    # Use tempfile to safely handle temp files
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        temp_pdf_path = Path(tmp_file.name)
        tmp_file.write(pdf_file.read())

    # Call Docling for PDF to markdown (and images)
    output_dir = Path("scratch")
    docling_pdf_to_markdown(temp_pdf_path, output_dir)

    # Extract text using MarkItDown
    extracted_text = markitdown_pdf_to_text(temp_pdf_path)

    if extracted_text is None:
        _log.error("No text extracted from PDF.")
        return None

    return extracted_text

def save_md_data(extracted_data):
    """ Function to save extracted markdown data. """
    save_extracted_data_as_markdown(extracted_data, "output_markitdown.md")

    with open("output_markitdown.md", "r", encoding="utf-8") as f:
        markdown_content = f.read()

    return markdown_content
