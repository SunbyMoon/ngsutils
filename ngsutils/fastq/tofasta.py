#!/usr/bin/env python
## category Conversion
## desc Converts to FASTA format (seq or qual)
'''
Convert FASTQ to FASTA.  Optionally outputs just the quality values.

Same format as SOLiD csfasta / qual files.
'''

import os
import sys

from ngsutils.fastq import FASTQ


def export_fasta(fastq, qual=False, out=sys.stdout, quiet=False):
    for read in fastq.fetch(quiet=quiet):
        if not qual:
            out.write('>%s\n%s\n' % (read.name, read.seq))
        else:
            out.write('>%s\n%s\n' % (read.name, ' '.join([str(ord(x) - 33) for x in read.qual])))


def usage():
    print """Usage: fastqutils tofasta {-qual} filename.fastq{.gz}
Options:
  -qual    Export the quality values (space separated numbers)
"""
    sys.exit(1)

if __name__ == '__main__':
    qual = False
    fname = None

    for arg in sys.argv[1:]:
        if arg == '-qual':
            qual = True
        elif os.path.exists(arg):
            fname = arg

    if not fname:
        usage()

    fq = FASTQ(fname)
    export_fasta(fq, qual)
    fq.close()
