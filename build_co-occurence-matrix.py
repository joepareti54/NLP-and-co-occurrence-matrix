import numpy as np
# build co-occurrence matrix for a given corpus
START_TOKEN = '<START>'
END_TOKEN = '<END>'
#win is the window of words left and right relative to the center word
#as of 1-15-2022 I tested win =1 and win =2
#
win = 1
#
def flatten(C):
	c = []
	c = [y for x in C for y in x]
	return c
def distinct_words(corpus):
	corpus_words1 = flatten(corpus) 
	corpus_words = sorted(set(corpus_words1))
	num_corpus_words = len(corpus_words)
	return corpus_words, num_corpus_words
#
corpus = ["{} All that glitters isn't gold {}".format(START_TOKEN, END_TOKEN).split(" "), "{} All's well that ends well {}".format(START_TOKEN, END_TOKEN).split(" ")]
#
CORPUS, num_corpus_words = distinct_words(corpus)
s_corpus = sorted(CORPUS)
#s_corpus is the sorted corpus that contains unique words
print('raw corpus ', corpus)
print('sorted corpus ', s_corpus)
l = len(s_corpus)
#
W = dict(zip(s_corpus, range(l)))
#W is the dictionary with: keys = unique words in the sorted corpus of uique words, and values = index of those words
# {'<END>': 0, '<START>': 1, etc
# 
#print('dictionary')
#print (W)
#M is the co-occurrence matrix to be built
M = np.zeros((l,l), dtype=int)
count = np.zeros((l), dtype= int)
print('build matrix M')
print('use this corpus')
print(corpus)
print('and these entries')
print(s_corpus)
print('----------------------')
#
M_INDX = np.full((l, l), 7215)
#M_INDX is a 2D matrix where
# each row is the word index
# the values are the column indecs where M needs to be added + 1 
# 
print(M_INDX)
L = len(corpus)
# the next lines are the 2 nested loops: over sentences, and over word in a sentence for the given corpus
# inside the 2 nested loops, there is a while loop on window because we need the column indeces to be increased by 1 
# for each center word, which is the inner for loop, there are left (ISTART) and right (IEND) words
# count is the array to be incremented as a new column index needs to be stored in the matrix of column indeces
# each row corresponding to a different word will have a different number of column indeces, hence count has to be a 1d array 
# the column index is obtained as lookup in the W dictionary with key = the word being in process
# because the column indeces are stored progressively along the word row, the count variable needs to be increased by 1
# the code stores only the indeces because it must be cleaned up before applying to the co-occurrence
#
#
for sentence in corpus:
	L = len(sentence)
	for i, word in enumerate(sentence):
		row_idx = W[word]
		WIN = win
		while WIN > 0:
			ISTART = max(i-WIN, 0)
#			print(row_idx,count[row_idx],ISTART)
			M_INDX[row_idx][count[row_idx]] = W[sentence[ISTART]]	
			IEND   = min(i+WIN, L-1)
			count[row_idx] = count[row_idx] + 1 
			M_INDX[row_idx][count[row_idx]] = W[sentence[IEND]]
			count[row_idx] = count[row_idx] + 1 
			WIN = WIN - 1
#
#
# at this stage M_INDX contains too many END/start entries and needs to be processed
#the B matrix ensures that for each row the column indeces are different from row indeces
B = np.full((l,l), 7215)
for i in range(l):
	for j in range(l):
		if M_INDX[i][j] != i: 
			B[i][j] = M_INDX[i][j]
#print(B)
#
# the following ensures that the filler is removed and redundant column indeces are only kept if not 0 or 1
# i is the row index that also indexes the word in s_corpus
# the rows are converted to list because it is easier to handle the redundant values in list
#
for i in range(l):
	a_lst = list(B[i][:])
	LI = []
	for x in a_lst:
		if x != 0 and x != 1 and x < 100:
			LI.append(x)
		else:
			if x not in LI and x <100:
				LI.append(x)
	for x in LI:
		M[i][x] = M[i][x] + 1
print('M')
print(M)
