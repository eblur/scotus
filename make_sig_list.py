#! /usr/bin/env python

"""
    make_sig_list.py -- Make a list of signatures from tab separated value text file
    
    2015.12.13: lia@space.mit.edu
"""

import random

INFILE  = 'responses_printed.tsv'
OUTFILE = 'signature_list.tex'

class Signature(object):
    def __init__(self, line):
        llist = line.split('\t')
        self.name  = llist[1].rstrip(" ")
        self.title = llist[2].rstrip(" ")
        self.affil = llist[3].rstrip("\n")
    
    @property
    def format_sig_string(self):
        if (self.title == "") and (self.affil == ""):
            return "{\\bf %s} \\\\" % (self.name)
        elif self.affil == "":
            return "{\\bf %s}, %s \\\\" % (self.name, self.title)
        elif self.title == "":
            return "{\\bf %s}, {\\sl %s} \\\\" % (self.name, self.affil)
        else:
            return "{\\bf %s}, %s, {\\sl %s} \\\\" % (self.name, self.title, self.affil)


def is_duplicate( sig, siglist ):
    result = False
    for scheck in siglist:
        if (sig.name == scheck.name) and (sig.affil == scheck.affil):
            result = True
    return result

if __name__ ==  '__main__':
    f_in  = open(INFILE, 'r')
    f_out = open(OUTFILE, 'w')
    
    # Create a list of signature objects
    siglist = []
    for line in f_in:
        sig = Signature(line)
        if not is_duplicate(sig, siglist):
            siglist.append(sig)
        else:
            pass
    
    # Shuffle the list and print it to a file
    counter = 1
    random.shuffle(siglist)
    for s in siglist:
        f_out.write("%d.~%s\n" % (counter, s.format_sig_string))
        counter += 1
    
    # close the files
    f_in.close()
    f_out.close()
