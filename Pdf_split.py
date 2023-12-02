import PyPDF2
import os
import shutil

def split(x):    
    for i in os.listdir(x):
        fullpdfpath = os.path.join(x,i)
        pdf = PyPDF2.PdfReader(fullpdfpath)
        pdfpage = len(pdf.pages)
        for i in range(pdfpage):
            page = pdf.pages[i]
            content = page.extract_text()
            print(content)
            # if 'ABI Document Support Services' in content:
            #     shutil.move(fullpdfpath, 'B:\Python\Git\Split_Pdf_Pages_Inv_vise\ABI')
            #     break
            


def main():
    nm = os.path.dirname(os.path.abspath(__file__))
    pdfpath = os.path.join(nm, 'Pdf')
    split(pdfpath)



if __name__ == '__main__':
    main()

