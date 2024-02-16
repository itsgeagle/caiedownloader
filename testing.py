import fitz

outFile = fitz.open(r'/Users/aaryanmehta/Downloads/9709 Paper 5 2020-23 FM MJ.pdf')

words = outFile[78].get_text("words", delimiters=None)
for i in range(0, len(words)-1):
    print(words[i][4] + " " + words[i+1][4])
    print(words[i][4] == "BLANK" and words[i+1][4] == "PAGE")
