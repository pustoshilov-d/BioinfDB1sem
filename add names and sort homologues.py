from Bio import AlignIO


original_file = open(r"data/Homologues_origin_aligned.fasta", 'r')
new_file = open(r"data/Homologues_named.fasta", 'w')


records = AlignIO.read(original_file, 'fasta')

for record in records:
    print(record.description)
    # print(record.seq)
    spl = str(record.description).split(' ', maxsplit=1)
    record.id = ('Hom./'+spl[1]+'/'+spl[0]).replace(' ', '_')

    record.name = ''
    record.description = ''
    print(record.id)

records.sort()

AlignIO.write(records,  new_file, 'fasta')







