from Bio.Seq import Seq
from Bio import SeqIO

original_file = open(r"data/Homologues_origin.fasta", 'r')
new_file = open(r"data/Homologues_translated.fasta", 'w')


records = SeqIO.parse(original_file, 'fasta')
for record in records:
    # print(record.__dict__.keys())
    # print(record.translate())
    desc = record.description
    record = record.translate()

    record.description = ''
    record.id = desc
    print(record.id)
    print(record.description)
    SeqIO.write(record,  new_file, 'fasta')

# coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
# print(coding_dna.translate())
# help(coding_dna.translate)