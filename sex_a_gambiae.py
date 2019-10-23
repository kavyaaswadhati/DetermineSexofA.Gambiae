# Determine the coverage of reads from a sample anopheles gambiae to the x, y, and autosome 
# scaffolds of the GCA_000005575.1_AgamP3_genomic.fna annotated reference genomce.
#
# EXECUTABLE: python3 sex_a_gambiae.py < indiv1.fasta.sam.bam.s.bam.depth
# OUTPUT: List of Chromosome ID and depth of coverage across 
#
# sex_a_gambiae.py
# Kavya Aswadhati
# 10/22/19

import sys



# GET DEPTH FILE FROM STDIN
depthfile = sys.stdin

# INITIALIZE REQUIRED OBJECTS
y_reads = 0
y_pos_num = 0
x_reads = 0
x_pos_num = 0
two_reads = 0
two_pos_num = 0
three_reads = 0
three_pos_num = 0

# CHROMOSOME  SCAFFOLD IDS
ys = [] # will be populate via an iteration through the reference genome
chrom2 = ['CM000357.1','CM000356.1','NT_078266.2','NT_078265.2'] # left and right scaffolds for chromosome 2
chrom3 = ['CM000358.1', 'CM000359.1','NT_078268.4','NT_078267.5'] # left and right scaffolds for chromosome 3


# POPULATE ys [] WITH Y SCAFFOLDS
# gather y chromosome scaffold names from reference genome
for line in open ('GCA_000005575.1_AgamP3_genomic.fna'):
	a = line.strip()
	if a[0] == '>':
		b = a.split(' ')
		if (b[6] == 'Y'):
				ys.append(b[0][1:]) # scaffold belongs to a Y chromosome reference


# GET READ COVERAGE

# From the depth file, get the coverage of reads and length of the chromosome scaffold for each 
# chromosome ( X, Y, Autosome)
num_ys = len(ys)
for line in depthfile:
	# each line in the depth file is:
	# chrom_scaffold    position    depth_at_position
	pos_info = line.strip().split('\t')
	# if the scaffold is a y chromosome scaffold
	read_at_pos = int(pos_info[2])
	# position correlates to a y chromosome
	if pos_info[0] in ys:
		y_reads += read_at_pos
		y_pos_num += 1
	# position correlates to a x chromosome
	if pos_info[0] == 'CM000360.1':
		x_reads += read_at_pos
		x_pos_num += 1
	# position correlates to a 2 chromosome
	if pos_info[0] in chrom2:
		two_reads += read_at_pos
		two_pos_num += 1
	# position correlates to a 3 chromosome
	if pos_info[0] in chrom3:
		three_reads += read_at_pos
		three_pos_num += 1

# CALCULATE AND OUTPUT RESULTS
print('chromosome   depth')
print('Y:   ', y_reads/y_pos_num)
print('X:   ', x_reads/x_pos_num)
print('2:   ', two_reads/two_pos_num)
print('3:   ', three_reads/three_pos_num)








