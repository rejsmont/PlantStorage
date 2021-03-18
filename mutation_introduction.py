import random
import levenshteinDistance
from Bio import SeqIO
import numpy as np
from io import StringIO

def mutation(rate, seq):
    baseList = ["A","T","C","G"]
    records = list(SeqIO.parse(seq, "fasta"))
    for sequence in records:
        curSeq = StringIO(str(sequence.seq))
        mutatedSeq = sequence.seq.tomutable()
        mutationHistory = []
        randomList = np.random.rand(len(curSeq.getvalue()))
        index = 0
         
        for base in curSeq.readline():
            index = curSeq.tell() - 1
            curSeq.seek(index)
            if randomList[index] < rate:
                diff = False
                while diff == False:
                    newBase = baseList[random.randint(0, 3)]
                    if newBase != base:
                        mutatedSeq[index] = newBase
                        mutationHistory.append([index, base, newBase])
                        diff = True


        yield (curSeq, mutatedSeq, mutationHistory, len(mutationHistory))


def main():
    for seq, newSeq, history, nbMutation  in mutation(1/1000, "./ressources/Araport11_genes.201606.cdna.fasta"):
        print("lenght of unmuted sequence : ", len(seq.getvalue()))
        print("lenght of muted sequence : ", len(newSeq))
        if nbMutation == levenshteinDistance.levenshteinDistance(seq.getvalue(), newSeq):
            print("We found : " + str(nbMutation) + " mutations in the sequence")
            accept = input("Type ''Y'' to see the history of the mutation or anything else to finish")
            if accept.lower() == "y":
                for elem in history:
                    print("Mutation at index : " + str(elem[0]) + " which consist of a substitution where " + elem[1] + " has been transformed into a " + elem[2])
            next = input("Type ''N'' to see the next mutation or anything else to finish")
            if next.lower() != "n":
                print("finish")
                return    
    print("finish")



if __name__ == '__main__':
    main()