from bioservices import UniProt
from Bio import SeqIO

sorted_file = r"Proteins_sorted.fasta"
named_file = r"Proteins_named.fasta"
# open(sorted_file, 'w') as sorted,

# with open(named_file, 'w') as named:
#     records = SeqIO.parse(named_file, 'fasta')
#     for record in records:
#         print(record.id)

records =  list(SeqIO.parse(named_file, "fasta"))
records.sort()
[print(rec) for rec in records]

# named.close()
#