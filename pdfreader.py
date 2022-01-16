import PyPDF2 as py
import pyttsx3 as pt
book = open("cookbook.pdf","rb")
reader = py.PdfFileReader(book)
pages = reader.numPages
print(pages)
speak = pt.init()
voices = speak.getProperty('voices')
speak.setProperty('voice',voices[1].id)
try:
 for num in range(13,pages):
    page = reader.getPage(13)
    text = page.extractText()
    speak.say(text)
    print(text)
    speak.runAndWait()
except Exception as e:
    print(e)