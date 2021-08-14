from PyPDF2 import PdfFileMerger
pdfs=['in1_file.pdf','in2_file.pdf']
merge=PdfFileMerger()

for pdf in pdfs:
    merge.append(pdf)

with open('merged_file.pdf','web') as file:
       merge.write(file)

print('pdf files merged into merged_file.pdf')