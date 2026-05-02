import PyPDF2
import sys

def extract():
    try:
        pdfFileObj = open('college-detail\\Autonomous\\News Letter\\CSBS.pdf', 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        text = ''
        for pageObj in pdfReader.pages:
            text += pageObj.extract_text() + '\n'
        with open('tmp_csbs_pdf.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Success")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    extract()
