from Bio.Blast import NCBIWWW
from Bio import AlignIO

new_file = open(r"data/Proteins_named_All.fasta", 'r')

records = AlignIO.read(new_file, format="fasta")
record = records[9]
print(record)
print(record.seq)
find = str(record.seq).replace('-', '')
print(find)
# print('MHEYLIDEVQHSSSESHTPGHVRLNHPVKELLWVVQRDSAITPTPYTGPGALAGGLGNDWFNWSGQYDAGLGLVFDPIASAELQLNGHRRTLEHPAQYFRTVHPREKHTSKPSGFVYNYSFALYPEDKQPSGSCNFSRIDNVTLRLIFPTAYNSESAAHATPFNGQIRVYAPNPNVVLVTSGMMGKLYAN')

result = NCBIWWW.qblast("blastp", "wgs", find)
print(result)