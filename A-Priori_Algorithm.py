"""
Title: A-Priori Algorithm
Author: Brendan Lauck
"""

import itertools as itt
import operator

# get all unique items from baskets
# returns dictionary
def getItems(fp):
    line = fp.readline()
    items = {}
    while line:
        line_items = line.split(' ')
        # store items in dictionary
        items.update({line_items[i] : 0 for i in range(len(line_items)) if line_items[i] not in items})
        line = fp.readline()
    return items


# read each basket and count occurences of each item
# get counts of all items in baskets
# updates counts of all items in dataset
def getItemCounts(items, fp):
    fp.seek(0)
    line = fp.readline()
    while line:
        for item in line.split():
            items[item] += 1
        line = fp.readline()

# Pass 1
# get frequent numbers and make pairs
# returns list of 2-tuples
def getCandidatePairs(items):
    frequentItems = sorted([item for item, count in items.items() if count >= 100])
    return list(itt.combinations(frequentItems, 2))


# Pass 2
# get support of pairs then return frequent pairs
# returns dictionary
def getFrequentPairs(candidatePairs, fp):
    candidatePairs = set(candidatePairs) # using a set saved MASSIVE amounts of time
    pair_counts = {}
    fp.seek(0)
    line = fp.readline()

    while line:
        line_pairs = list(itt.combinations(sorted(line.split(' ')[:-1]), 2))
        for pair in line_pairs:
            if pair in candidatePairs:
                if pair not in pair_counts.keys():
                    pair_counts[pair] = 0
                pair_counts[pair] += 1
        line = fp.readline()
    return {key : value for key, value in pair_counts.items() if value >= 100}


# Pass 3
# get frequent pairs and make triples
# returns list of 3-tuples
def getCandidateTriples(frequentPairs):
    items_frequentPairs = set()
    for pair in frequentPairs:
        items_frequentPairs.add(pair[0])
        items_frequentPairs.add(pair[1])
    return list(itt.combinations(sorted(items_frequentPairs), 3))


# Pass 4
# get support of triples then return frequent triples
# returns dictionary
def getFrequentTriples(candidateTriples, fp):
    candidateTriples = set(candidateTriples) # using a set saved MASSIVE amounts of time
    triple_counts = {}
    fp.seek(0)
    line = fp.readline()

    while line:
        line_triples = list(itt.combinations(sorted(line.split(' ')[:-1]), 3))
        for pair in line_triples:
            if pair in candidateTriples:
                if pair not in triple_counts.keys():
                    triple_counts[pair] = 0
                triple_counts[pair] += 1
        line = fp.readline()
    return {key : value for key, value in triple_counts.items() if value >= 100}


# prints confidence scores of pairs
def printConfidenceScores_pairs(items, frequentPairs):
    frequentItems = {key: value for key, value in items.items() if value >= 100}
    confidenceScores_pairs = {}
    for pair, support in frequentPairs.items():
        confidenceScores_pairs[pair] = round(support / frequentItems[pair[0]], 5)
        confidenceScores_pairs[tuple([pair[1], pair[0]])] = round(support / frequentItems[pair[1]], 5)
    return sorted(confidenceScores_pairs.items(), key=operator.itemgetter(1))[:-6:-1]
   
 
# prints confidence scores of pairs
def printConfidenceScores_triples(frequentPairs, frequentTriples):
    confidenceScores_triples = {}
    for triple, support in frequentTriples.items():
        confidenceScores_triples[triple] = round(support / frequentPairs[tuple([triple[0], triple[1]])], 5)
        confidenceScores_triples[tuple([triple[0], triple[2], triple[1]])] = round(support / frequentPairs[tuple([triple[0], triple[2]])], 5)
        confidenceScores_triples[tuple([triple[1], triple[2], triple[0]])] = round(support / frequentPairs[tuple([triple[1], triple[2]])], 5)
    return sorted(confidenceScores_triples.items(), key=operator.itemgetter(1))[-15:-20:-1]


# performs A_Priori algorithm on big data
def A_Priori(filepath):
    fp = open(filepath)
    items = getItems(fp)
    getItemCounts(items, fp)
    candidatePairs = getCandidatePairs(items)
    frequentPairs = getFrequentPairs(candidatePairs, fp)
    candidateTriples = getCandidateTriples(frequentPairs)
    frequentTriples = getFrequentTriples(candidateTriples, fp)
    out1 = printConfidenceScores_pairs(items, frequentPairs)
    out2 = printConfidenceScores_triples(frequentPairs, frequentTriples)
    file = open("output.txt","w")
    file.write('\n\nOUTPUT A\n' + str(out1) + '\n\n')
    file.write('OUTPUT B\n' + str(out2) + '\n\n\n')
    file.close()
    fp.close()



if __name__ == '__main__':
    A_Priori('browsingdata.txt')
