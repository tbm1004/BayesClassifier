from bayesText import *

# change these to match your directory structure
baseDirectory = "20news-bydate/" #top level folder name
trainingDir = baseDirectory + "20news-bydate-train/" #training folder name
testDir = baseDirectory + "20news-bydate-test/" #test folder name

# initializer takes two arguments: training folder name, stoplist filename
bT = BayesText(trainingDir, baseDirectory + "stopwords0.txt")

# this is purely informational if you are curious to see what the probability of a word
# appearing in a particular newsgroup (folder)
print("probability of word 'god' appearing in rec.motorcycles:", bT.prob["rec.motorcycles"]["god"])
print("probability of word 'god' appearing in soc.religion.christian:",bT.prob["soc.religion.christian"]["god"])
print("probability of word 'stay' appearing in rec.sport.hockey:", bT.prob["rec.sport.hockey"]["stay"])
print("probability of word 'stay' appearing in hotels:",bT.prob["hotels"]["stay"])

print("Running Test ...")
bT.test(testDir)

# to classify a text document, make sure you have the document in the folder that the program looks for
# in this case classify1.txt is a file in my base diretory
string = "classify"
i = 1
while i <= 25:
    print("\nClassify post@classify" + str(i) + ":", bT.classify(baseDirectory + string + str(i) + ".txt"))
    i += 1
    #Classifies as expected. The hotel related posts are categorized corrently.

