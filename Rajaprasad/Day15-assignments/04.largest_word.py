# Python3 program for the above approach

# Function to print the longest
# word in given sentence
def largestWord(string):

    # Sort the words in increasing
    # order of their lengths
    string = sorted(string, key=len)

    # Print last word
    print('largest word on the sentence is : ', string[-1])


# Driver Code
if __name__ == "__main__":

    # Given string
    string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"

    # Split the string into words
    l = list(string.split(" "))

    largestWord(l)
