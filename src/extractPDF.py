from PIL import Image
import io
import fitz


def getText(pdf_path):
    pages = []
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        page_text = page.get_text()
        pages.append(page_text)
        text += page_text
    return {
        "text": text,
        "pageText": pages,
    }

def getImages(pdf_path, output_dir):
    pdf_document = fitz.open(pdf_path)
    pages = []
    images = []

    for num, page in enumerate(pdf_document, start=1):
        image_list = page.get_images(full=True)

        def saveImage(img, index):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            image_filename = f"{output_dir}/page{num}_image{index}.png"
            image.save(image_filename, "PNG")
            return image_filename
        
        saved_images = [saveImage(img, index) for index, img in enumerate(image_list, start=1)]
        pages.append(saved_images)
        images += saved_images

    pdf_document.close()
    return {
        "images": images,
        "pageImages": pages,
    }

