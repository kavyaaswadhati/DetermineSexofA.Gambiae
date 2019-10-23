#!/bin/bash
fastq-dump --fasta -I --split-files --stdout {ACCESSION} >Â  {ACCESSION}.fasta 2>  {ACCESSION}.fasta.err
bwa mem GCA_000005575.1_AgamP3_genomic.fnaÂ  {ACCESSION}.fasta >  {ACCESSION}.fasta.sam 2>Â  {ACCESSION}.fasta.sam.err
samtools view -bhÂ  {ACCESSION}.fasta.sam >Â  {ACCESSION}.fasta.sam.bam
samtools sortÂ  {ACCESSION}.fasta.sam.bam > {ACCESSION}.fasta.sam.bam.s.bam
samtools depth -aÂ  {ACCESSION}.fasta.sam.bam.s.bam >Â  {ACCESSION}.fasta.sam.bam.s.bam.depth
python3 sex_a_gambiae.py <Â  {ACCESSION}.fasta.sam.bam.s.bam.depth >Â  {ACCESSION}.fasta.sam.bam.s.bam.depth.chroms
