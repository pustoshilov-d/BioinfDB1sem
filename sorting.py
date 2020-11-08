from Bio import SeqIO, AlignIO

sorted_file = r"data/Proteins_sorted.fasta"
named_file = r"data/Proteins_named.fasta"

records =  AlignIO.read(named_file, "fasta")
records.sort()
print(records)
AlignIO.write(records, sorted_file, "fasta")

