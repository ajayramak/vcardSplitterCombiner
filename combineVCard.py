# Ajayrama Kumaraswamy, 07 Oct 2014
# Usage: "python combineVCard.py contacts" where 'contacts' is a directory in pwd containing the vcf files which are to
# be combined.
import os

def combineVCF(dirName):
    """
    combines all the contacts in individual files in dirName into a single file called dirName.vcf in pwd.
    """

    with open(os.path.split(dirName)[1] + '.vcf', 'w') as outFle:

        for fleName in os.listdir(dirName):

            if fleName[-4:] == '.vcf':

                with open(os.path.join(dirName, fleName), 'r') as inFle:

                    vCard = inFle.read()

                    outFle.write(vCard)


if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 2, 'this script takes only one commandline argument'

    dirName = sys.argv[1]

    combineVCF(os.path.abspath(dirName))