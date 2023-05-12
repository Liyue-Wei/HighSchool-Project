import re
while(True):
    try:
        def capitalize_sentence(sentence):
            sentence = sentence.capitalize()
            sentence = re.sub(r'\bi\b', 'I', sentence)
            sentence = re.sub(r'(?<=[.!?])\s+([a-z])', lambda x: x.group(0).upper(), sentence)
            return sentence
        input_text = input()
        output_text = capitalize_sentence(input_text)
        print(output_text)
    except:
        break

'''
import re
while(True):
    try:
        b = str(input())
        t = b
        a = []
        for l in range(len(t)):
            if(t[l]=="." or t[l]=="!" or t[l]=="?"):
                a.append(t[l])
        b = re.split('\. |\! |\? |\!', b)
        if(len(b)!=1):
            b.pop()
            for n in range(len(b)):
                spl = str(b[n]).capitalize()
                print("{}{}".format(spl, a[n]), end=' ')
            print('\n')
        else:
            for n in range(len(b)):
                spl = str(b[n]).capitalize()
                print(spl, end=' ')
            print('\n')
    except:
        break
'''