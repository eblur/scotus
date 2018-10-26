# scotus

This repo contains Python scripts for taking in tab-separated-value ascii files (e.g., output from a spreadsheet) and producing an html (or latex) ready list of signatures for displaying on the web.

## How to use these files

You can export the results of a Google form survey to a Google spreadsheet. In the spreadsheet, click on *File* -> *Download  As* -> *Tab-separated value (tsv)* to get an ascii file of tab separated values.

Modify the attributes of the `Signature` object in **make_sig_list.py** or **make_sig_list_html.py** to correspond to the columns in your .tsv file.

Modify the `Signature.format_sig_string` method if necessary to print the signatures as you desire. (Default is to print Name, Title, and Affiliation)

Run `python make_sig_list_html.py` in the terminal.

Note that the signatures will be printed in random order each time you run the script. To turn that off, comment out the `random.shuffle(siglist)` line.
