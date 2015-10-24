# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = next(f)
        header = [x.strip() for x in header.split(',')]
        #refactored thanks to the help of stack exchange, two lines became one!
        #header = header.strip()
        #header = header.split(',')
        linecount = 1

        for line in f:
            if linecount < 11:
                line = line.replace("\xe2\x80\x94","-")
                line = [x.strip() for x in line.split(',')]

                data.append(dict(zip(header, line)))
                linecount += 1

    print data

    return data

def main():
    datafile = os.path.join(DATADIR, DATAFILE)

    d = parse_file(datafile)

def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


test()


if __name__ == "__main__":
    main()

'''
I went ahead and screen grabbed how the instructor completed this step because it was different than
how I did. The strip and split string functions were combined thanks to a tip on SO. The Python
documentation says that strip and split are deprecateed -- need to look into the Python 3 string
method equivalents and how they work.
'''
