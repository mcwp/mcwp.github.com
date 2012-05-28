#! /usr/bin/env python
import argparse
import os
from pyPdf import PdfFileWriter, PdfFileReader

def get_files_list(dirname, date_order, rdate_order):
    """Get the order of the files to merge."""
    file_list = os.listdir(dirname)
    file_mtimes = dict.fromkeys(file_list)
    for f in file_list:
        if f[0] == '.':
            print "Skipping file: ", f
            del file_mtimes[f]
            continue
        if date_order or rdate_order:
            file_mtimes[f] = os.stat(dirname + '/' + f).st_mtime
    if date_order or rdate_order:
        return sorted(file_mtimes.keys(), key=file_mtimes.get, reverse=rdate_order)
    else:
        return file_list

    
def merge_files_in_order(pdf_list, list_only, output_file):
    """Merge the files in order."""
    output_file = output_file + ".pdf"
    if not list_only:
        output = PdfFileWriter()
        outputStream = file(output_file, "wb")
    total_pages = 0    
    for pdf_in in pdf_list:
        try:
            pdf = PdfFileReader(file(pdf_in, "rb"))
            num_pages = pdf.getNumPages()
        except IOError:
            print "skipping ", pdf_in
            continue
        if list_only:
            print pdf_in, ':', num_pages
        else:
            for i in range(num_pages):
                output.addPage(pdf.getPage(i))
            output.write(outputStream)
        total_pages += num_pages
    would_be = "would be"
    if not list_only:
        outputStream.close()
        would_be = ""
    print total_pages, "pages", would_be, "written to", output_file

        

def main(path, date_order, rdate_order, list_only, output_file):
    if path[-1] != '/':
        path = path + '/'
    file_list = get_files_list(path, date_order, rdate_order)
    pdf_list = [path + '../pdf/' + file_list[x][:-3] + 'pdf' for x in range(len(file_list))]
    merge_files_in_order(pdf_list, list_only, output_file)
                    
            
if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Script with options and args.')
    mtimes = parser.add_mutually_exclusive_group()
    mtimes.add_argument('-m', '--mtime', dest='date_order',
                        action='store_true',
                        help='Collect in modification date order.')
    mtimes.add_argument('-r', '--reversem', dest='rdate_order',
                        action='store_true',
                        help='Collect in reverse modification date order.')
    parser.add_argument('path', help='The dir containing the pdf files to combine.')
    parser.add_argument('-l', '--list_only', dest='list_only',
                        action='store_true',
                        help='List the page count of the input files only.')
    parser.add_argument('-o', '--output_file', dest='output_file', 
                       default="combined", help='Name to use for the outputfile.pdf')

    args = parser.parse_args()

    main(args.path, args.date_order, args.rdate_order, args.list_only, args.output_file)


