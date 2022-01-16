# NLP-and-co-occurrence-matrix
build the co-occurrence matrix as required in Manning's workshop

 The purpose of this code is to build co-occurrence matrix for a given corpus
reference : Prof C. Manning https://www.youtube.com/watch?v=rmVRLeJRkl4&list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ

A toy corpus is defined and next a co-occurrence matrix is built which has in each row the index of a unique word in the corpus, set as center word, and in each column the number
of occurrences of neighboring words to the center word.

M is the numpy co-occurrence matrix to be built

win is the window of words left and right relative to the center word

as of 1-15-2022 I tested win =1 and win =2




s_corpus is the sorted corpus that contains unique words

W is the dictionary with: keys = unique words in the sorted corpus of uique words, and values = index of those words
 {'<END>': 0, '<START>': 1, etc
The W dictionary is used to address each word in the corpus and associate an index which is used to build M

M_INDX is a 2D matrix where
 each row is the word index
 the values are the column indecs where M needs to be added + 1

 the core process includes 2 nested loops: over sentences, and over word in a sentence for the given corpus;
 inside the 2 nested loops, there is a while loop on window because we need the column indeces to be increased by 1

 for each center word, which is the inner for loop, there are left (ISTART) and right (IEND) words

 count is the array to be incremented as a new column index needs to be stored in the matrix of column indeces
 each row corresponding to a different word will have a different number of column indeces, hence count has to be a 1d array

 the column index is obtained as lookup in the W dictionary with key = the word being in process
 because the column indeces are stored progressively along the word row, the count variable needs to be increased by 1
 the code stores only the indeces because it must be cleaned up before applying to the co-occurrence


 after executing the code described above,  M_INDX contains too many IEND/ISTART entries and needs to be processed:
the B matrix ensures that for each row the column indeces are different from row indeces

Next, the filler is removed, and redundant column indeces are only kept if not 0 or 1
This is meant to retain multiple occurrences of important words, while retaining only one start/end token occurrence for each center word

In the final for loop:
 i is the row index that also indexes the word in s_corpus
 the rows are converted to list because it is easier to handle the redundant values in list
Because at this stage the lists are containing the right occurrences of the uniqe word, the list values are used to increment the M positions for the column index
