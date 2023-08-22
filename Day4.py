def removeDups(self, S):
    # code here
    output = ""
    for letter in s: # Goes through each and every letter in s
        if letter not in output:
            output+=letter
    return output
