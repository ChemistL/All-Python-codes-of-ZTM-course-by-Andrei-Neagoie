# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:08:18 2020

@author: saura
"""
import PyPDF2 # the package that installs the PDF functions 

with open('./PDF/dummy.pdf', 'rb') as file:       
# 'rb' is read binary, for pdf we append 'b' to it.
# so it converts the file to binary and PyPDF2 works with binary files.
    reader = PyPDF2.PdfFileReader(file)
    print(file)
    print(reader)
    print(reader.numPages)
    print(reader.getPage(0))

    page = reader.getPage(0) # page object has to be assigned before rotating, otherwise python dosn't recognize reader. rotateClockwise
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('./PDF/rotated.pdf', 'wb') as new_file:  #'wb' stands for write the file in binary format 
        writer.write(new_file)

