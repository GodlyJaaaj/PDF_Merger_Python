from PyPDF2 import PdfFileMerger
import os
from os import walk


merger = PdfFileMerger()
path = os.getcwd() + r"\pdf_files"
files = []
print("Enter final pdf file name (only name) : ")
final_Name = str(input()) + ".pdf"

if __name__ == '__main__':
    print(path)
    for dirpath, dirnames, filenames in walk(path):
        for file in filenames:
            if ".pdf" in file:
                files.append(file)
            else:
                pass
    print(files)
    for pdf_file in files:
        merger.append("pdf_files/"+pdf_file)
    merger.write(final_Name)
    merger.close()
    print()
    print("Done!")
    print()
    print(f"File named '{final_Name}' has been saved at '{os.getcwd()}'")
