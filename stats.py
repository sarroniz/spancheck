import sys
import re

verbs_list = []
verbs_pres_list = []
verbs_imp_list = []
verbs_pret_list = []
verbs_fut_list = []
verbs_cond_list = []
nouns_list = []
adj_list = []
adv_list = []
others = []
word_list = []
glossary = ['casa', 'arbol']
glossary_list = []


with open('outputmorpho.txt', 'r') as f:
    for line in f:
        if line[0] == "\"":
            if not re.findall('[\.\,\¡\!\¿\?]', line):
                word_list.append(line[2:-3])

f.close()


with open('outputmorpho.txt', 'r') as f:
    for line in f:
        if line[0] == ";":
            continue
        if line[0] == "\t":
            # Append VERBS
            if re.findall('VERB', line) or ('AUX', line):
                if (re.findall('Tense=Pres', line)) and (re.findall('Mood=Ind', line)):
                    verbs_list.append(line)
                    verbs_pres_list.append("<Tense=Pres>")
                if (re.findall('Tense=Imp', line)) and (re.findall('Mood=Ind', line)):
                    verbs_list.append(line)
                    verbs_imp_list.append("<Tense=Imp>")
                if (re.findall('Tense=Past', line)) and (re.findall('Mood=Ind', line)):
                    verbs_list.append(line)
                    verbs_pret_list.append("<Tense=Past>")
                if (re.findall('Tense=Fut', line)) and (re.findall('Mood=Ind', line)):
                    verbs_list.append(line)
                    verbs_fut_list.append("<Tense=Fut>")
                if (re.findall('Mood=Cnd', line)):
                    verbs_list.append(line)
                    verbs_cond_list.append("<Mood=Cnd>")
                next(f)

            # Append NOUNS
            if re.findall('NOUN', line):
                nouns_list.append("<NOUN>")
                next(f)

            # Append ADJs
            if re.findall('ADJ', line):
                adj_list.append("<ADJ>")
                next(f)

            # Append ADVs
            if re.findall('ADV', line):
                adv_list.append("<ADV>")
                next(f)

            else:
                if not re.findall('PUNCT', line):
                    next(f)

    print("---------------------------------------------------------------")
    print("Total de palabras en el texto: ", len(word_list))
    print("De las cuales ", len(nouns_list), "/", len(word_list), "son sustantivos")
    print("De las cuales ", len(adj_list), "/", len(word_list), "son adjetivos")
    print("De las cuales ", len(adv_list), "/", len(word_list), "son adverbios")
    print("De las cuales ", len(verbs_list), "/", len(word_list), "son verbos")
    print("\tDe estos verbos: ")
    print("\t\t", len(verbs_pres_list), "/", len(verbs_list), " están en PRESENTE DE INDICATIVO")
    print("\t\t", len(verbs_imp_list), "/", len(verbs_list), " están en IMPERFECTO DE INDICATIVO")
    print("\t\t", len(verbs_pret_list), "/", len(verbs_list), " están en PRETÉRITO DE INDICATIVO")
    print("\t\t", len(verbs_fut_list), "/", len(verbs_list), " están en FUTURO SIMPLE")
    print("\t\t", len(verbs_cond_list), "/", len(verbs_list), " están en CONDICIONAL SIMPLE")

f.close()

# Load the vocabulary into the list "glossary"
with open('lists/VOCABULARY.txt', 'r') as f:
    for word in f:
        glossary.append(word)

f.close()

# Check if the words from the text are in the "glossary"
for word in word_list:
    if word in glossary:
        glossary_list.append(word)

print("\nEl texto incluye ", len(glossary_list), "/", len(word_list), " palabras del vocabulario especificado en VOCABULARY.txt:")
for i in glossary_list:
    print("\t -", i)
print("---------------------------------------------------------------")
