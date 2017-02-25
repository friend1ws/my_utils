#! /bin/bash

import pysam

def get_seq(reference, region):

    seq = ""    
    for item in pysam.faidx(reference, region):
        seq = seq + item.rstrip('\n')
    seq = seq.replace('>', '')
    seq = seq.replace(region, '')

    return seq


def reverse_complement(seq_str):

    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A',
                  'W': 'W', 'S': 'S', 'M': 'K', 'K': 'M', 'R': 'Y', 'Y': 'R',
                  'B': 'V', 'V': 'B', 'D': 'H', 'H': 'D', 'N': 'N'}

    cseq = "".join(complement.get(base, base) for base in reversed(seq_str))

    return(cseq)


