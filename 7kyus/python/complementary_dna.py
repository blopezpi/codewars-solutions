def DNA_strand(dna):
    strand = ""
    for letter in dna:
        if letter == "A":
            strand += "T"
        elif letter == "T":
            strand += "A"
        elif letter == "C":
            strand += "G"
        elif letter == "G":
            strand += "C"
    return strand
