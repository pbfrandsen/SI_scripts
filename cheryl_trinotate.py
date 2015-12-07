# This script takes as input two files: a file containing trinotate output and
# a file containing a list of search terms. For each search term, this script
# searches the trinotate file and prints every line containing the search term
# to an outfile named "out.csv". Rename this file after each run if you wish
# to preserve it
import sys

def add_header(inFile, outFile):
    """adds header from inFile to outFile"""
    # Open files for reading and writing
    inFile = open(inFile, 'r')
    outFile = open(outFile, 'w')

    # Pull and write the header line
    header = inFile.readline()
    outFile.write(header)

    # Move back to the first line after the header in the inFile
    inFile.seek(1)
    inFile.close()
    outFile.close()

def search_lines(term, inFile, outFile):
    """Pull lines with search terms.

    This function takes a search term, then looks through the trinotate file
    for the terms and pulls out any line that contains the term and prints
    it to the outfile.
    """
    inFile = open(inFile, 'r')
    outFile = open(outFile, 'a')
    # outFile.write(term + '\n')

    # Loop through the lines of the file and search for the term
    for line in inFile.readlines():
        line = line.lower()
        if term in line:
            outFile.write(line)

    inFile.seek(1)
    inFile.close()
    outFile.close()

def gen_term_list(termFile):
    """Generate list of search terms"""
    # Open up the term file
    termFile = open(termFile, 'r')
    termList = []

    # Read each line and save it to a list
    for line in termFile.readlines():
        line = line.strip('\n\r')
        line = line.lower()
        termList.append(line)
    return termList

def loop_terms(termList, inFile, outFile):
    """Loop through term searches"""
    # Search and output lines for each term
    for term in termList:
        search_lines(term, inFile, outFile)


if __name__ == '__main__':
    # Parse the command line input
    inFile = sys.argv[1]
    termFile = sys.argv[2]
    outFile = "out.csv"
    # Run functions to generate outFile
    add_header(inFile, outFile)
    termList = gen_term_list(termFile)
    loop_terms(termList, inFile, outFile)


