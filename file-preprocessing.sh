pip install pdfminer

#make sure you're in the right directory (folder with your pdfs per patient)

#general layout for parsing of PDFs into plain text
pdf2txt.py -o name_of_output_file input_file.pdf

#removing ASCII characters
tr -cd '\11\12\15\40-\176' < file-with-binary-chars > clean-file
