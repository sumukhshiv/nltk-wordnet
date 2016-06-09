from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic

class Compare:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def compare(self):
        f = open(self.file1, 'r')
        g = open(self.file2, 'r')
        fo = open('output.txt', 'w').close()

        #Uses Information Content from both brown and semcor temporarily
        brown_ic = wordnet_ic.ic('ic-brown.dat')
        semcor_ic = wordnet_ic.ic('ic-semcor.dat')


        # fnew = f.read().splitlines()
        # gnew = g.read().splitlines()

        f_lines = f.readlines()
        g_lines = g.readlines()
        # f_lines_final = []
        # g_lines_final = []
        #
        # for line in f_lines:
        #     f_lines_final.append(line.rstrip('\n'))
        #
        # for line in g_lines:
        #     g_lines_final.append(line.rstrip('\n'))

        for line in f_lines:
            for line2 in g_lines:
                line = line.rstrip('\n')
                line2 = line2.rstrip('\n')
                a = wn.synsets(line)[0]
                b = wn.synsets(line2)[0]

                #Comparison uses Jiang-Conrath Similarity
                comparison_brown = str(a.jcn_similarity(b, brown_ic)) #Using ic-brown.dat
                comparison_semcor = str(a.jcn_similarity(b, semcor_ic)) #Using ic-semcor.dat

                out = open("output.txt", "a")
                out.write(str(a.lemmas()[0].name()) + "," + str(b.lemmas()[0].name()) + ": (brown - " + comparison_brown + ", semcor - " + comparison_semcor +")\n")

        print("***Comparison completed. Results recorded in output.txt.***")








# fo = open("foo.txt", "wb")
# comparison = str(self.word1.path_similarity(self.word2))
# fo.write(str(self.word1) + "," + str(self.word2) + ": " + comparison)


# f = open('test.txt', 'r')
# for line in f:
#     print(line)
#
# fo = open("foo.txt", "wb")
# x = "hello"
# y = "Sumukh"
# fo.write( x + "," +"\n" + y);


# with open("test.txt", "r") as ins:
#     array = []
#     for line in ins:
#         array.append(line)
#
#     print(array)
