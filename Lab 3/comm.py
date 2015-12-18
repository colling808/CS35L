#!/usr/bin/python

import random, sys, locale
from optparse import OptionParser

locale.setlocale(locale.LC_ALL, 'C')

#read input
class comm:
    def __init__(self, file1, file2):
        if file1 != "-":
            f1 = open(file1, 'r')
        else:
            f1 = sys.stdin
        self.lines1 = f1.readlines()
        f1.close()
        
        if file2 != "-":
            f2 = open(file2, 'r')
        else:
            f2 = sys.stdin
        self.lines2 = f2.readlines()
        f2.close()

    def column1(self):
        return self.lines1

    def column2(self):
        return self.lines2

    def checkIfSorted(self, filename, filelen):
        for i in range(filelen - 1):
            if filename[i] > filename[i+1]:
                return False
        return True
    
    
def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2

Compare sorted files FILE1 and FILE2 line by line.

With no options, produce three-column output. Column one contains
lines unique to FILE1, column two contains lines unique to FILE2,
and column three contains lines common to both files."""

#add options
    parser = OptionParser(version=version_msg,
                          usage=usage_msg)

    parser.add_option("-1", action="store_true", dest="opt1",
                      default=False, help="suppress column 1 (lines unique to FILE1)")
    parser.add_option("-2", action="store_true", dest="opt2",
                      default=False, help="suppress column 2 (lines unique to FILE2)")
    parser.add_option("-3", action="store_true", dest="opt3",
                      default=False, help="suppress column 3 (lines that appear in both files)")
    parser.add_option("-u", action="store_true", dest="optU",
                      default=False, help="do not check that the input is correctly sorted")

    options, args = parser.parse_args(sys.argv[1:])

#read in options and arguments
    if len(args) != 2:
        parser.error("wrong number of operands")
    input_file1 = args[0]
    input_file2 = args[1]
    opt1 = options.opt1
    opt2 = options.opt2
    opt3 = options.opt3
    optU = options.optU
    output = ""

    try:
        generator = comm(input_file1, input_file2)
        col1 = generator.column1()
        col2 = generator.column2()

#IOError (i.e. when file does not exist)
    except IOError as err:
        errno, strerror = err.args
        parser.error("I/O error({0}): {1}".format(errno, strerror))

    #add a newline to end of file if not there already
    if '\n' not in col1[len(col1)-1]:
        col1[len(col1)-1] += '\n'
    if '\n' not in col2[len(col2)-1]:
        col2[len(col2)-1] += '\n'

    #without option -u
    if not optU:

        #check if files are sorted
        if not generator.checkIfSorted(col1, len(col1)):
            output += "comm: file 1 is not in sorted order\n"
        if not generator.checkIfSorted(col2, len(col2)):
            output += "comm: file 2 is not in sorted order\n"
        if output != "":
            print(output)
            return

        i = 0
        j = 0

        while i < len(col1) and j < len(col2):
            if col1[i] < col2[j]:
                #check for option -1
                if not opt1:
                    output += col1[i]
                i += 1
            elif col1[i] > col2[j]:
                #check for option -2
                if not opt2:
                    if opt1:
                        output += col2[j]
                    else:
                        output += '\t'+ col2[j]
                j += 1
            else:
                #otherwise, element is in both files
                #check for option -3
                if not opt3:
                    if opt1 and opt2:
                        output += col1[i]
                    elif opt1 or opt2:
                        output += '\t' + col1[i]
                    else:
                        output += '\t\t' + col1[i]
                i += 1
                j += 1
        #print remaining list
        if i < len(col1) and not opt1:
            for k in range(i, len(col1)):
                output += col1[k]
                
        if j < len(col2) and not opt2:
            for k in range(j, len(col2)):
                if opt1:
                    output += col2[k]
                else:
                    output += '\t' + col2[k]

    #with option -u
    else:
        #traverse through col1 in order
        for i in range(len(col1)):
            found = False
            #see if elements from col1 exists in col2
            for j in range(len(col2)):
                #if they share an element, add to col3
                if col1[i] == col2[j]:
                    if not opt3:
                        if opt1 and opt2:
                            output += a[i]
                        elif opt1 or opt2:
                            output += '\t' + col1[i]
                        else:
                            output += '\t\t' + col1[i]
                        #deletes element so it will not be duplicated
                        col2.pop(j)
                        found = True
                        break
            #else add to first column
            if not found and not opt1:
                output += col1[i]

        #add remaining elements not in col1 to second column
        if not opt2:
            for j in range(len(col2)):
                if opt1:
                    output += col2[j]
                else:
                    output += '\t' + col2[j]

    #if all options -123 are on, return nothing                
    if opt1 and opt2 and opt3:
        return
    else:
        print(output)

    return
    
if __name__ == "__main__":
    main()
