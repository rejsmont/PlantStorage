import numpy as np

# minEditDistance()
# function to calculate the minimal edit distance,
# levenshteinDistance
# without numpy
def levenshteinDistance(s1, s2):

    # if the first string is "" the minimal distance will be the length of the second string
    if s1 == "" :
        return len(s2)

# if the second string is "" the minimal distance will be the length of the first string
    if s2 == "":
        return len(s1)

# if the length of s1 is < to s2,, inversing the two parameter, its to build the matrix correctly
    if len(s1) < len(s2):
        return levenshteinDistance(s2, s1)

    #At this point, we are sure that we can calculate the minimal edit distance correctly, string in the good order, and no one them are empty

    # initialising our first raw to make our comparisons
    previous_row = range(len(s2) + 1)

    # looping into the first string
    for i, c1 in enumerate(s1):
        # creating the current list we working on, the first value in the list correspond to the index of the letter we are checking on the string
        # for exemple, for the word "sitting", its gonna be 2 when we are checking the first i
        current_row = [i + 1]

        # checking into s2 to check our alignement
        for j, c2 in enumerate(s2):
            #  here, we using j+1 instead of j since previous_row and current_row are one character diff
            insertions = previous_row[j + 1] + 1
            # here, just using j and not j+1 to check the deletions
            deletions = current_row[j] + 1
            # checking if c1 and c2 are the same char or not, false = 0 true = 1
            substitutions = previous_row[j] + (c1 != c2)
            # adding the lowest value in our current list, the minimal value here corresponding to the minimal edit distance  needed at the current state of our string check
            current_row.append(min(insertions, deletions, substitutions))
            # updating our previous raw to the current raw, by doing that, we only need the two last raws to calculated our minimal edit distance
        previous_row = current_row
        # print(current_row)


    return previous_row[-1]


# minEditDistanceV2()
# function to calculate the minimal edit distance,
# levenshteinDistance
# Using numpy matrix

def minEditDistanceV2(s1, s2):
# initialisation  of a matrix full of 0, len()+1, since first character is " ", therefore 0
    matrix = np.zeros ((len(s1)+1, len(s2)+1)) 
	# setting first column to the word, the length is +1 since first character is empty
    matrix [0:len(s1)+1, 0] = [x for x in range (0, len(s1)+1)] 
	# setting first row of matrix to the word, the length is +1 since the first character is empty
    matrix [0,0: len(s2)+1] = [y for y in range (0, len(s2)+1)] 

# iterating over columns in a row, starting from index 1, since  0 was previously preset
    for x in range(1, len(s1)+1): # iterating rows, we start from 1 because 0 was preset before
        for y in range(1, len(s2)+1): 			# if characters are equal, we do nothing
			# checking if the char characters are equal, if yes, nothing happen
            if s1[x-1] == s2[y-1]: 
                matrix [x,y] = matrix[x-1,y-1]
				# if they are different, checking which opperation is the least costly: substitution, deletion or insertion
            else: 
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
	#printing the matrix
    print (matrix) 

	# returning  the last element of the matrix, corresponding to our minimal edit distance

    return (matrix[len(s1), len(s2)])
	
def main():
    s1 = input("Enter the first word : ")
    s2 = input("Enter the second word : ")
    print("without using numpy : ")
    print("the minimal edit distance is : " + str(levenshteinDistance(s1, s2)))

    print("using numpy matrix : ")
    print("the minimal edit distance is : " + str(levenshteinDistance(s1, s2)))

if __name__ == '__main__':
	main()