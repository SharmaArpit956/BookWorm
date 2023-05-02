import fitz
import docx2txt
 
def get_text_from_PDF(file_path):
  
    file_path=str(file_path)

    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        text = ""
        for page in doc: 
            text += page.get_text()
        return text
    
    if file_path.endswith(".txt"):
        # Open file for reading
        file = open(file_path, 'r')
        # Read the content of the file
        text = file.read()
        # Close the file
        file.close()
        return text
    
    if (".doc") in file_path:
        # Extract text from the Word document
        text = docx2txt.process(file_path)
        return text
 
 
 


# print(get_text_from_PDF("K:/my_pdf2.pdf"))



 