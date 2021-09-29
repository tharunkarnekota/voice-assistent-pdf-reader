import PyPDF2
import pyttsx3

reader = pyttsx3.init()

""" RATE"""
rate = reader.getProperty('rate')   # getting details of current speaking rate
reader.setProperty('rate', 150)     # setting up new voice rate


def read(txt):
    reader.say(txt)
    reader.runAndWait()

read('i am your virtual friend. helps you read pdf')

#make sure file is decrpted
#else, go to pdf decrypt: unlock PDF - free online pdf password remover
#grab the file into it, later download it

read('please enter file name (without extension): ')
filename = input('enter file name (without extension): ')
filename = filename + '.pdf'
pdf_book = open(filename,'rb')

try:
    pdfReader = PyPDF2.PdfFileReader(pdf_book)
    pages = pdfReader.numPages
    print('total pages:',pages)

    read('please enter page number to start from')
    page_num = int(input('Enter page no: '))
    page_num = page_num - 1

    read('ok boss')
    print('reading..')

    for num in range(page_num, pages):
        page = pdfReader.getPage(num)                   #it converts to binary format index start fron zero
        text = page.extractText()
        text = text.replace('\n',' ')
        print(text)

        read(text)
except:
    print('pdf file is not decrypted')

input()                                            #we ned one alteast empty input to run a console

