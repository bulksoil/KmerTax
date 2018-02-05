#!/usr/bin/python

import sys
from optparse import OptionParser
from collections import Counter
import pandas as pd
import gzip
import re

def opt_get():
	parser = OptionParser()
	parser.add_option("-r", help = "FASTA database file, no gaps",dest = "reference_file", type = "string")
	parser.add_option("-k", help = "Size of kmer", dest = "k_size", type = "int", default = 4)
	parser.add_option("-o", help = "Outfile to print to", dest = "out_file", type = "string")
	(options, args) = parser.parse_args()
	return(options)

def read_fasta(FH):
	header = FH.readline().rstrip("\n")
	seq = FH.readline().rstrip("\n")
	header = header[1:]
	if not header:
		return(["none", "none"])
	else:
		return([header, seq])

def break_into_kmers(info, k_size):
	header, sequence = info
	kmers = []
	for i in range(len(sequence) - k_size):
		kmer = sequence[i:i+k_size]
		if re.search('^[ATCGatcg]*$', kmer):
			kmers.append(kmer)
	return(Counter(kmers))


def main():
	processed_seqs = 0

	opts = opt_get()
	ref_file = opts.reference_file
	k_size = opts.k_size
	out_file = opts.out_file

	fasta_in = gzip.open(ref_file, 'rb')
	kmer_store = {}
	while True:
		fasta_info = read_fasta(fasta_in)
		kmers = break_into_kmers(fasta_info, k_size)
		kmer_store[fasta_info[0]] = kmers
		processed_seqs += 1

		if processed_seqs % 10 == 0:
			sys.stdout.write('%s\r' % processed_seqs)
    		sys.stdout.flush()

		if fasta_info[0] == "none":
			df = pd.DataFrame(kmer_store).transpose().fillna(0)
			df.index.names = ["OTU_ID"]
			df.to_csv(out_file, sep = '\t')
			break

main()
