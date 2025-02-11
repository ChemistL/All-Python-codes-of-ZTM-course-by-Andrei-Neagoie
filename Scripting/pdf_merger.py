# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:42:11 2020

@author: saura
"""
import PyPDF2
import sys

inputs = sys.argv[1:]   # this will stores all the arguments passes except the first one, and store them in a list

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger() # merge object is created
    for pdf in pdf_list:
        merger.append(pdf) #append all pdf on the list in this loop until the last one is done
    merger.write('./PDF/merged.pdf')

pdf_merger(inputs)
