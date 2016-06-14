from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from decimal import Decimal

class Compare:
    def __init__(self, file1, file2):
        #Initialized using file names (String Format)
        self.file1 = file1
        self.file2 = file2

    def compare(self):
        f = open(self.file1, 'r')
        g = open(self.file2, 'r')

        #Clears any previous output (if applicable)
        #New output overwrites previous data
        fo = open('output.txt', 'w').close()


        f_lines = f.readlines()
        g_lines = g.readlines()


        for line in f_lines:
            line = line.rstrip('\r\n')
            out = open("output.txt", "a")
            out.write(str(line + ':'+ '\n'))
            for line2 in g_lines:

                line2 = line2.rstrip('\r\n')

                #Utilizes primary (most common) meaning of the word
                a = wn.synsets(line)[0]
                b = wn.synset(line2 + ".v.01")

                comparison = a.path_similarity(b)

                out = open("output.txt", "a")
                out.write("    " + line2 + " - " + str(comparison) + "\n")

            out.write('\n')

        print("***COMPARISON COMPLETED: Results recorded in output.txt***")
