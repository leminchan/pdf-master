import sys, argparse

from dep import merge

if __name__ == "__main__":
    commands = dict()
    try:
        parser = argparse.ArgumentParser(description="Master PDF allows you to merge, split, and extract text/images from PDFs.\nFollow the following commands to manipulate your PDFs!")
        parser.add_argument('-f', nargs='*', help='Merge specified files [F [F...]] in the order specified.')
        parser.add_argument('-d', nargs=1, help='Merge all files in specified directory D.')
        args = parser.parse_args()
        commands = vars(args)
    except:
        print("Error occurred.")
        sys.exit(2)

    # args.m is a list of strings containing the given arguments.
    if args.f:
        merge.mergeFiles(args.f)

    # args.f is list of one string specifying the directory.
    if args.d:
        files = merge.getFiles(args.d)
        merge.mergeFiles(files)