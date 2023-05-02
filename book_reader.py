import fitz
import pyttsx3
from transformers import pipeline, AutoModelForDocumentQuestionAnswering, AutoTokenizer

class BookReader:

    def __init__(self, pdf, context):
        self.pdf = pdf
        self.context=self.get_text_from_PDF(pdf)
        model_name = "DistilBertForQuestionAnswering"
        # model_name="distilbert-base-uncased"
        model = AutoModelForDocumentQuestionAnswering.from_pretrained(model_name )
        tokenizer = AutoTokenizer.from_pretrained(model_name )
        self.question_answerer = pipeline(
            'question-answering', model=model, tokenizer=tokenizer)
        # self.question_answerer = pipeline("question-answering")

    def get_text_from_PDF(self,pdf):
        doc = fitz.open(pdf)
        text = ""
        for page in doc: 
            text += page.get_text()
        return text
        # return "hi to be implemented"

    def set_context_for_extractive_answering(self,text):
        self.context=text

    def get_answer(self,ques):
        result = self.question_answerer(question=ques, context=self.context)
        return result
        
    def text_do_speech(self,text):
        # Initialize the Text-to-speech engine using the init() function:
        engine = pyttsx3.init()
        # Convert your text to speech using the say() function:
        engine.say(text)
        # Run the engine to output the speechES:
        engine.runAndWait()
      

    def get_text_from_speech(self):
        text="To be implemented"
        return text

    def print_text_full_screen(self,text):
        #TODO replace this function later
        print(text)


# Instantiate the class
my_book = BookReader("my_pdf.pdf", "none")
my_book.print_text_full_screen("Have a good day")
my_book.text_do_speech("Have a good day")
pdf_contentt=my_book.get_text_from_PDF("my_pdf.pdf")
my_book.set_context_for_extractive_answering(pdf_contentt)
print("loading answer.......")
answer = my_book.get_answer("The compatibility of the product is the responsibility of who?")
# my_book.print_text_full_screen("Have a good day")

my_book.text_do_speech(answer)
answer = my_book.get_answer("inspection and maintenance of machinery/equipment should only be performed after?")
my_book.text_do_speech(answer)