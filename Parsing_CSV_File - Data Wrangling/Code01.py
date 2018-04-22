import os

DATADIR = ""
DATAFILE = "Music-list.csv"

#Defining parse file function
def parse_file(datafile):
    data = []
    with open (datafile, "rb") as f:
        for line in f:
            print line

    return data

#Function to test above code implementation
def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file (datafile)
    firstline = {'Title': 'Song-One', 'Music chart position': '1', 'Label':}

