#! /usr/bin/env python

import seq

def get_seq_main(args):

    gseq = seq.get_seq(args.reference, args.region)
    print gseq


def reverse_complement_main(args):

    cseq = seq.reverse_complement(args.seq_str)
    print cseq


