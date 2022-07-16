from PyPDF2 import PdfFileMerger
import os
from os import walk

merger = PdfFileMerger()
path = os.getcwd() + r"\pdf_files"
files = []
final_Name = ""
while not any(final_Name):
    print("Enter final pdf file name (only name) : ")
    final_Name = str(input()) + ".pdf"
    if final_Name in os.listdir(path.rstrip(r"\pdf_files")):
        print(f"File '{final_Name}' already exists")
        print()
        final_Name = ""
    else:
        break

if __name__ == '__main__':
    print(path)
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            files.append(file)
        else:
            pass
    print(f"{len(files)} pdf files detected")
    print(files)
    if not files:
        print("No pdf files found in the directory")
    else:
        for pdf_file in files:
            merger.append("pdf_files/" + pdf_file)
        merger.write(final_Name)
        merger.close()
        print()
        print("Done!")
        print()
        print(f"File named '{final_Name}' has been saved at '{os.getcwd()}'")
    print()
