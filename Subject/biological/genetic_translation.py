'''
DNA A T C G --> RNA U A G C
'''
def translation(dna):
    global untranslated_dna, translated_mrna
    untranslated_dna = []
    translating = []
    translated_mrna = []
    
    untranslated_dna = dna
    count = len(untranslated_dna)

    for num in range(0, count, 1):
        translating.append(untranslated_dna[num])

    for num in range(0, count, 1):
        if translating[num] == "A":
            translated_mrna.append("U")

        elif translating[num] == "T":
            translated_mrna.append("A")

        elif translating[num] == "C":
            translated_mrna.append("G")

        elif translating[num] == "G":
            translated_mrna.append("C")

        else:
            translated_mrna = False

    print(translated_mrna)
    
dna = input()
translation(dna)