from pathlib import Path
import PyPDF2
import sys, argparse, os.path

def checkValidFiles(files: [str]) -> bool:
    '''
    Function to check if all Paths in a 
    given list are paths to actual files.
    '''
    # Turns all strings in the list into Paths
    paths = [Path(f) for f in files]
    for p in paths:
        if p.is_file() is not True: 
            print("Merge failed:\n" + str(p) + " is not a valid PDF.")
            return False
    return True

def getFiles(directory: [str]) -> [str]:
    '''
    Function to return a list of files in a specified directory.
    This function also checks if the given directory is also a valid one.
    '''
    files = []
    path_to_directory = Path(directory[0])
    if path_to_directory.is_dir() is not True:
        print("Merge failed:]n" + directory[0] + " is not a valid directory.")
        sys.exit(2)
    files = [directory[0]+f for f in os.listdir(path_to_directory) if f.endswith('.pdf')]
    return files

def mergeFiles(files: [str]) -> None:
    '''
    First checks if all files are valid.
    Then, creates the new PDF object, finally writing to 
    "output.pdf" after all files have been appended.
    '''
    if checkValidFiles(files):
        newPDF = PyPDF2.PdfFileMerger()
        for f in files:
            newPDF.append(f)
        with open("output.pdf", 'wb') as outputfile:
            newPDF.write(outputfile)
            newPDF.close()

if __name__ == "__main__":
    commands = dict()
    try:
        parser = argparse.ArgumentParser(description="Master PDF allows you to merge, split, and extract text/images from PDFs.\nFollow the following commands to manipulate your PDFs!")
        parser.add_argument('-f', nargs='*', help='Merge specified files [F [F...]] in the order specified.')
        parser.add_argument('-d', nargs=1, help='Merge all files in specified directory D.')
        args = parser.parse_args()
        commands = vars(args)
    except:
        sys.exit(2)

    # args.m is a list of strings containing the given arguments.
    if args.f:
        mergeFiles(args.f)

    # args.f is list of one string specifying the directory.
    if args.d:
        files = getFiles(args.d)
        mergeFiles(files)