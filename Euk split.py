from Bio import SeqIO, AlignIO



# file = open(r"data/Proteins_named_Vir.fasta", 'r')
file_Vir  = open(r"data/temp.fasta", 'w')

file = open(r"data/Proteins_named_Euk_Vir.fasta", 'r')

records =  AlignIO.read(file, "fasta")

for record in records:
    # print(record.__dict__.keys())
    record.id = str(record.description).replace("(",'').replace(")",'')
    record.description = ''
    print(record.id)
    print(record.description)

AlignIO.write(records, file_new, "fasta")
