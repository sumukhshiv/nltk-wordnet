# nltk-wordnet

This software uses the Natural Language Toolkit (NLTK). To download this, visit: http://www.nltk.org/data.html. From nltk.download(), you only need to download the book containing “Everything used in the NLTK Book.”

This software runs the Jiang-Conrath Similarity algorithm which “returns a score denoting how similar two word senses are, based on the Information Content (IC) of the Least Common Subsumer (most specific ancestor node) and that of the two input Synsets.” You can find out more about this and other similarity tests at: http://www.nltk.org/howto/wordnet.html.

WARNING: This file is dependent on other packages supported only for WordNet 3.0. They will not work with any other version of Wordnet.

This software takes two input files, compares the two line-by-line, and outputs the degree of similarity of the lines onto a new file. 

To use this, run the Python interactive mode. Create a new Compare Object, which is initialized using two file names in string format. These files must appear in the same directory. Run the .compare() method. The desired data will be outputted in a new file titled output.txt, found in the same directory. 

EXAMPLE:
Compare(‘input1.txt’, ‘input2.txt’).compare()