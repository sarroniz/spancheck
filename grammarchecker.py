import sys
import re

PUNCT = [".", ",", "¿", "?", "¡", "!"]
alltags = ["ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X"]
presente = open("lists/conjugaciones/presente_ind.txt", "r")
imperfecto = open("lists/conjugaciones/imperfecto_ind.txt", "r")
preterito = open("lists/conjugaciones/preterito.txt", "r")
futuro = open("lists/conjugaciones/futuro.txt", "r")
condicional = open("lists/conjugaciones/condicional.txt", "r")
ser_estar = open("lists/conjugaciones/ser_estar.txt", "r")


# KNOWN ISSUES:
# Sometimes, when the parser outputs more than one possible tag for a single token,
# it can print the results for every tag.
# -
# This code could probably be improved with a stemmer and reducing the number of "if" statement.
# -

print("---------------------------------------------------------------")
with open('outputmorpho.txt', 'r') as f:
    for line in f:
        if line[0] == ";":
            continue
        elif line[0] == "\"":
            print(line[2:-3])
        elif line[0] == "\t":

            # Analyze NOUNs
            if re.findall('NOUN', line):
                print("<NOUN>")
                if re.findall('Gender=Masc', line) and re.findall('Number=Sing', line):
                    print("\tMasculino Singular")
                if re.findall('Gender=Fem', line) and re.findall('Number=Sing', line):
                    print("\tFemenino Singular")
                if re.findall('Gender=Masc', line) and re.findall('Number=Plur', line):
                    print("\tMasculino Plural")
                if re.findall('Gender=Fem', line) and re.findall('Number=Plur', line):
                    print("\tFemenino Plural")

                print("\tDon't forget to check the agreement between the determiner (DETERMINER) \n\tand the adjective (ADJECTIVE) that may go with this noun!")
                print("------------------------")

            # Analyze DETs
            if re.findall('DET', line):
                print("<DETERMINER>")
                if re.findall('Gender=Masc', line) and re.findall('Number=Sing', line):
                    print("\tMasculino Singular")
                if re.findall('Gender=Fem', line) and re.findall('Number=Sing', line):
                    print("\tFemenino Singular")
                if re.findall('Gender=Masc', line) and re.findall('Number=Plur', line):
                    print("\tMasculino Plural")
                if re.findall('Gender=Fem', line) and re.findall('Number=Plur', line):
                    print("\tFemenino Plural")

                print("\tDon't forget to check the agreement between the noun (NOUN) \n\tand the adjective (ADJECTIVE) that may go with this determiner!")
                print("------------------------")

            # Analyze VERBs
            if re.findall('VERB', line):
                print("<VERB>")
                # Present Indicative Tense
                if (re.findall('Tense=Pres', line)) and (re.findall('Mood=Ind', line)):
                    infinitive = re.findall('\"[a-z]+\"', line)
                    print(presente.read() + "\n")
                    print("La conjugación para el verbo", infinitive[0], "es:")
                    for i in infinitive:
                        if re.findall('\"ser\"', line):
                            print("\tsoy\n\teres\n\tes\n\tsomos\n\tsois\n\tson\n")
                            print(ser_estar.read() + "\n")
                            print("------------------------")
                        elif re.findall('\"estar\"', line):
                            print("\testoy\n\testás\n\testá\n\testamos\n\testáis\n\testán\n")
                            print(ser_estar.read() + "\n")
                            print("------------------------")
                        else:
                            if i[-3:-1] == "ar":
                                print("\t",i[1:-3] + "o\n" + "\t",i[1:-3] + "as\n" + "\t",i[1:-3] + "a\n" + "\t",i[1:-3] + "amos\n" + "\t",i[1:-3] + "áis\n" + "\t",i[1:-3] + "an\n")
                                print("------------------------")
                            elif i[-3:-1] == "er" or "ir":
                                print("------------------------")
                                print("\t",i[1:-3] + "o\n" + "\t",i[1:-3] + "es\n" + "\t",i[1:-3] + "e\n" + "\t",i[1:-3] + "emos\n" + "\t",i[1:-3] + "éis\n" + "\t",i[1:-3] + "en\n")


                # Imperfect Indicative Tense
                if (re.findall('Tense=Imp', line)) and (re.findall('Mood=Ind', line)):
                    infinitive = re.findall('\"[a-z]+\"', line)
                    print(imperfecto_ind.read() + "\n")
                    print("La conjugación para el verbo", infinitive[0], "es:")
                    for i in infinitive:
                        if re.findall('\"ser\"', line):
                            print("\tera\n\teras\n\tera\n\téramos\n\térais\n\teran\n")
                            print("\t",ser_estar.read() + "\n")
                            print("------------------------")
                        elif re.findall('\"estar\"', line):
                            print("\testaba\n\testabas\n\testaba\n\testábamos\n\testabais\n\testaban\n")
                            print("\t",ser_estar.read() + "\n")
                            print("------------------------")
                        else:
                            if i[-3:-1] == "ar":
                                print("\t",i[1:-3] + "aba\n" + "\t",i[1:-3] + "abas\n" + "\t",i[1:-3] + "aba\n" + "\t",i[1:-3] + "ábamos\n" + "\t",i[1:-3] + "ábais\n" + "\t",i[1:-3] + "aban\n")
                                print("------------------------")
                            elif i[-3:-1] == "er" or "ir":
                                print("\t",i[1:-3] + "ía\n" + "\t",i[1:-3] + "ías\n" + "\t",i[1:-3] + "ía\n" + "\t",i[1:-3] + "íamos\n" + "\t",i[1:-3] + "íais\n" + "\t",i[1:-3] + "ían\n")
                                print("------------------------")

                # Preterit Indicative Tense
                if (re.findall('Tense=Past', line)) and (re.findall('Mood=Ind', line)):
                    infinitive = re.findall('\"[a-z]+\"', line)
                    print(preterito.read() + "\n")
                    print("La conjugación para el verbo", infinitive[0], "es:")
                    for i in infinitive:
                        if re.findall('\"ser\"', line):
                            print("\tfui\n\tfuiste\n\tfue\n\tfuimos\n\tfuisteis\n\tfueron\n")
                            print("\t",ser_estar.read() + "\n")
                            print("------------------------")
                        elif re.findall('\"estar\"', line):
                            print("\testuve\n\testuviste\n\testuvo\n\testuvimos\n\testuvisteis\n\testuvieron\n")
                            print("\t",ser_estar.read() + "\n")
                            print("------------------------")
                        else:
                            if i[-3:-1] == "ar":
                                print("\t",i[1:-3] + "é\n" + "\t",i[1:-3] + "aste\n" + "\t",i[1:-3] + "ó\n" + "\t",i[1:-3] + "amos\n" + "\t",i[1:-3] + "asteis\n" + "\t",i[1:-3] + "aron\n")
                                print("------------------------")
                            elif i[-3:-1] == "er" or "ir":
                                print("\t",i[1:-3] + "í\n" + "\t",i[1:-3] + "iste\n" + "\t",i[1:-3] + "ió\n" + "\t",i[1:-3] + "imos\n" + "\t",i[1:-3] + "isteis\n" + "\t",i[1:-3] + "ieron\n")
                                print("------------------------")

                # Simple Conditional Tense
                if (re.findall('Mood=Cnd', line)):
                    infinitive = re.findall('\"[a-z]+\"', line)
                    print("\t",condicional.read() + "\n")
                    print("La conjugación para el verbo", infinitive[0], "es:")
                    for i in infinitive:
                        print("\t",i[1:-1] + "ía\n" + "\t",i[1:-1] + "ías\n" + "\t",i[1:-1] + "ía\n" + "\t",i[1:-1] + "íamos\n" + "\t",i[1:-1] + "íais\n" + "\t",i[1:-1] + "ían\n")
                        print("------------------------")

                # Simple Future Tense
                if (re.findall('Tense=Fut', line)) and (re.findall('Mood=Ind', line)):
                    infinitive = re.findall('\"[a-z]+\"', line)
                    print("\t",futuro.read() + "\n")
                    print("La conjugación para el verbo", infinitive[0], "es:")
                    for i in infinitive:
                        print("\t",i[1:-1] + "é\n" + "\t",i[1:-1] + "ás\n" + "\t",i[1:-1] + "á\n" + "\t",i[1:-1] + "emos\n" + "\t",i[1:-1] + "éis\n" + "\t",i[1:-1] + "án\n")
                        print("------------------------")


            # Analyze ADJs
            if re.findall('ADJ', line):
                print("<ADJECTIVE>")
                if re.findall('Gender=Masc', line) and re.findall('Number=Sing', line):
                    print("\tMasculino Singular")
                if re.findall('Gender=Fem', line) and re.findall('Number=Sing', line):
                    print("\tFemenino Singular")
                if re.findall('Gender=Masc', line) and re.findall('Number=Plur', line):
                    print("\tMasculino Plural")
                if re.findall('Gender=Fem', line) and re.findall('Number=Plur', line):
                    print("\tFemenino Plural")

                print("\tDon't forget to check the agreement between the determiner (DETERMINER) \n\tand the noun (NOUN) that may go with this adjective!")
                print("------------------------")

            # Analyze PROPNs
            if re.findall('PROPN', line):
                if re.findall('Gender=Masc', line):
                    print("<PROPER NOUN>")
                    print("\tMasculino")
                    print("------------------------")
                if re.findall('Gender=Fem', line):
                    print("<PROPER NOUN>")
                    print("\tFemenino")
                    print("------------------------")

            # If PUNCT, end of sentence
            if re.findall('PUNCT', line):
                print("---------------------------------------------------------------")

            # For everything else, do not show the tags
            else:
                continue
