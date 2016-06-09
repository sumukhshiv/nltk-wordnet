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

        #Supports Information Content from both brown corpus and semcor corpus
        brown_ic = wordnet_ic.ic('ic-brown.dat')
        semcor_ic = wordnet_ic.ic('ic-semcor.dat')

        f_lines = f.readlines()
        g_lines = g.readlines()


        for line in f_lines:
            for line2 in g_lines:

                #Currently supports only one word lines
                line = line.rstrip('\n')
                line2 = line2.rstrip('\n')

                #Utilizes primary (most common) meaning of the word
                a = wn.synsets(line)[0]
                b = wn.synsets(line2)[0]


                """
                ***IMPORTANT***
                Comparison uses IC from ic-brown.dat, but also supports
                ic-semcor.dat. To switch to semcor, comment out the first
                brown comparison and uncomment the second.

                """
                #Comparison uses Jiang-Conrath Similarity (JCN Similarity)

                #BROWN_IC
                comparison = str(round(a.jcn_similarity(b, brown_ic), 4)) #Using ic-brown.dat

                #SEMCOR_IC (UNCOMMENT TO USE ic-semcor.dat)
                #comparison = str(round(a.jcn_similarity(b, semcor_ic), 4)) #Using ic-semcor.dat

                out = open("output.txt", "a")
                out.write(str(a.lemmas()[0].name()) + "," + str(b.lemmas()[0].name()) + ": " + comparison + "\n")

        print("***COMPARISON COMPLETED: Results recorded in output.txt***")






# fnew = f.read().splitlines()
# gnew = g.read().splitlines()


# f_lines_final = []
# g_lines_final = []
#
# for line in f_lines:
#     f_lines_final.append(line.rstrip('\n'))
#
# for line in g_lines:
#     g_lines_final.append(line.rstrip('\n'))

# fo = open("foo.txt", "wb")
# comparison = str(self.word1.path_similarity(self.word2))
# fo.write(str(self.word1) + "," + str(self.word2) + ": " + comparison)


# f = open('test.txt', 'r')
# for line in f:
#     print(line)
#
# fo = open("foo.txt", "wb")
# x = "hello"
# y = "World"
# fo.write( x + "," +"\n" + y);


# with open("input.txt", "r") as ins:
#     array = []
#     for line in ins:
#         array.append(line)
#
#     print(array)
