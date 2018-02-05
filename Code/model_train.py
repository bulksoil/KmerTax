#!/usr/bin/python

from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from optparse import OptionParser

def opt_get():
	parser = OptionParser()
	parser.add_option("-t", help = "Taxonomy file. Needs to be tab separated",dest = "tax_file", type = "string")
	parser.add_option("-i", help = "Input file of kmer counts", dest = "k_file", type = "string")
	parser.add_option("-o", help = "Outfile to print to", dest = "out_file", type = "string")
	parser.add_option("-p", help = "Parallel jobs to run. Defaults to 1", dest = "jobs", default = 1, type = "int")
	(options, args) = parser.parse_args()
	return(options)

def make_sets(tax, kmer_counts):
	tax_train, tax_test, kmer_train, kmer_test = train_test_split(tax, kmer_counts, test_size = 0.5, stratify = tax['Phylum'])
	return([tax_train, kmer_train, tax_test, kmer_test])

def train_model(train_tax, train_kmer):
	

def test_model(test_tax, test_kmer, model):

def main:

	# Load in the options
	opts = opt_get()

	# Read in the kmer file as a dataframe
	print "Reading in kmer file"
	kmer_counts = pd.read_csv(opts.k_file, sep = "\t")

	# Read in the taxonomy file as a dataframe
	print "Reading in taxonomy file"
	tax = pd.read_csv(opts.tax_file, sep = "\t")

	# Make the kmer file and taxonomy file match orders
	tax = tax.set_index('OTU_ID')
	tax = tax.reindex(index = kmer_counts['OTU_ID'])
	tax = tax.reset_index()

	# Make training and test sets
	train_tax, train_kmer, test_tax, test_kmer = make_sets(tax, kmer_counts)

	# Train the RF model
	model = train_model(train_tax, train_kmer)







