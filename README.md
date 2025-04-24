This project is an attempt to make a program that scans a Word document (docx), looking for words and
phrases in a given language. The original docx file is rewritten with the words and phrases identified
with a different text color. 

A Python library named **fasttext** is used to detect the 'other language' words. It uses a file named
**lid.176.bin** as a knowledge-base for words in different languages. 

A Python library named **docx** is used to read the source document. This library provides data structures
that are used to scan the document context, mark the words and phrases in a different color, and
re-write the document to a new docx file.

I added the libraries to a virtual environment named **langdetect**.

The program name is **my_fasttext_colorcode.py**. The example input file is named **sample_tagging_text_all_black.docx**.
The sample file includes words in German (code de) and Greek (code el). This name is currently hard-coded in
the source file.

With the **langdetect** virtual environment loaded, it is invoked for German with a phrase length of 6 as follows:

python my_fasttext_colorcode.py de 6

It will read and scan the input file and write the output file named **sample_tagging_text_markup.docx**
