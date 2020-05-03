# spancheck

A spelling and grammar checker for students and instructors of L2 Spanish.

## Instructions:

This project compiles three different tools that can process compositions in L2 Spanish and help students and instructors to get instant feedback about the text. To run each of them, follow this steps:

1. Parse the raw text from a .txt file with the conllu-analyser.py and es-analyser included, and print the result in the "outputmorpho.txt" file, which will be read afterwards. In the terminal:

```
$ cat [your text file here] |\python3 conlluanalyser.py es-analyser.tsv | vislcg3 -t -g es.cg3 > outputmorpho.txt
```
or, alternatively:

```
$ echo "[some text here]" |\python3 conlluanalyser.py es-analyser.tsv | vislcg3 -t -g es.cg3 > outputmorpho.txt
```


2. After that, you should run the spellcheck.py tool to check that all the words are spelled correctly. This will make the other tools more accurate. If you get some spelling errors, make sure you correct them in your raw .txt file, and run step 1. again with the corrected text. You can run the spellchecker.py tool in your terminal by typing:

```
$ python3 spellchecker.py
```

If you don't get any output, there are no errors in the text.


3. Then you can run either the grammar checker or the statistical tool by simply typing:

```
$ python3 grammarchecker.py
```

or:

```
$ python3 stats.py
```
