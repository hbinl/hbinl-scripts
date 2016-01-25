__author__ = 'HaoBin'
# To calculate the total number of patterns
# involding light/heavy syllables in prosody
# and prints out all the combinations
# using backtracking

def poetic_pattern(n,syllables,c):
    # backtracking recursive module
    if sum(syllables) == n:
        # if the sum of beats meet the length, output
        c += 1
        print(str(syllables))
        return c
    elif sum(syllables) < n:
        # try other combinations
        beats = [1,2]
        for i in range(len(beats)):
            syllables.append(beats[i])
            if sum(syllables) <= n:
                c = poetic_pattern(n, syllables[:],c)
            syllables = syllables[0:len(syllables)-1]
    return c

def prosody(new_beat,new_string=""):
    if (new_beat < 0):
        print("Error")
    elif (new_beat == 0):
        print(new_string)
    elif (new_beat == 1):
        prosody(new_beat-1, new_string + "-short")
    elif (new_beat >= 2):
        prosody(new_beat-1, new_string + "-short")
        prosody(new_beat-2, new_string + "-long")

def poetic(n):
    # recursion bootstrap
    print("Total number of combinations: " + str(poetic_pattern(n,[],0)))

if __name__ == "__main__":
    try:
        poetic(int(input("Please input a number: ")))
        prosody(int(input("Please input a number: ")))
    except ValueError:
        print("Invalid number input.")
