import sys
import PyPDF2

documents = sys.argv[1:]


def pdf_combiner(pdf_files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write("Super.pdf")


pdf_combiner(documents)
