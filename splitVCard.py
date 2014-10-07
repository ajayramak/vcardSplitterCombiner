# Ajayrama Kumaraswamy, 07 Oct 2014
# Usage: "python splitVCard.py contacts.vcf" where "contacts.vcf" contains multiple contacts.
# A folder (in the case named contacts) will be created and the contacts will be stored inside the directory in files
# named 1.vcf, 2.vcf.., one contact being stored per file.

import os
from shutil import rmtree

class vcf(object):
    """
    Class to handle a vcard string
    """

    def __init__(self):
    
        self.vcfStr = []
        self.name = []
        self.valid = True
        self.uk = 1

    def write(self, fName):
        """
        writes the vcard into fName
        """

        if self.name == '':
            self.name = 'Unknown' + str(self.uk)
            self.uk += 1
        with open(os.path.join(fName), 'w') as out:
            for field in self.vcfStr:
                out.write(field)

    def addLine(self, stri):

        if self.valid:

            if stri[-2:] == '\r\n':
                stri = stri[:-2] + '\n'

            self.vcfStr.append(stri)


if __name__ == '__main__':

    import sys

    assert len(sys.argv) == 2, 'this script takes only one commandline argument'

    fleName = sys.argv[1]

    dirName = fleName[:-4]

    if os.path.isdir(dirName):
        rmtree(dirName)
    os.mkdir(dirName)

    fle = open(fleName, 'r')

    presLine = fle.readline()

    count = 1

    while presLine != '':

        if presLine[:11] == 'BEGIN:VCARD':

            presVCF = vcf()

        presVCF.addLine(presLine)

        if presLine[:9] == 'END:VCARD':

            presVCF.write(os.path.join(dirName, str(count) + '.vcf'))
            count += 1
            presVCF.valid = False

        if presLine[:2] == 'FN':

            if presLine[-2:] == '\r\n':
                presLine = presLine[:-2]
            presVCF.name = presLine[3:]

        presLine = fle.readline()
    

