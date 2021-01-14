import random
import levenshteinDistance

def mutation(rate, seq):
    mutatedSeq = ""
    baseList = ["A","T","C","G"]
    mutationHistory = []
    for i in range(len(seq)):
        base = seq[i]
        chance = random.random()
        if chance < rate:
            diff = False
            while diff == False:
                newBase = baseList[random.randint(0, len(base))]
                if newBase != base:
                    mutatedSeq += newBase
                    mutationHistory.append([i, base, newBase])
                    diff = True

        else: #if no mutation occured, just adding the bases to our new sequence
            mutatedSeq += base
                
    return [mutatedSeq, mutationHistory, len(mutationHistory)]

def chooseRandomSequence(fastafile):
    sequences = []
    with open(fastafile) as fileobj:
        isNewSec = False
        secId = ""
        realNucLine = ""
        for line in fileobj:
            if ">" in line and isNewSec == False:
                secId = line[line.rfind(">")+1:line.find("\n")]
                realNucLine = ""
                isNewSec = True
            elif ">" in line and isNewSec == True:
                sequences.append(realNucLine)
                secId = line[line.rfind(">")+1:line.find("\n")]
                realNucLine = ""
            elif line.find(">") == -1:
                realNucLine += line.split("\n")[0]

        if secId and realNucLine:
            sequences.append(realNucLine)

    return sequences[random.randint(0,len(sequences))]

def main():
    random.seed()
    seq = chooseRandomSequence("./ressources/Araport11_genes.201606.cdna.fasta")
    newSeq, history, nbMutation  = mutation(1/1000, seq)
    print("lenght of unmuted sequence : ", len(seq))
    print("lenght of muted sequence : ", len(newSeq))
    if nbMutation == levenshteinDistance.levenshteinDistance(seq, newSeq):
        print("We found : " + str(nbMutation) + " mutations in the sequence")
        accept = input("Type ''Y'' to see the history of the mutation or anything else to finish")
        if accept.lower() == "y":
            for elem in history:
                print("Mutation at index : " + str(elem[0]) + " which consist of a substitution where " + elem[1] + " has been transformed into a " + elem[2])

if __name__ == '__main__':
    main()