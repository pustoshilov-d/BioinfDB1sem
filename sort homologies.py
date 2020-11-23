from Bio import AlignIO


original_file = open(r"data/Homologues_aligned.fasta", 'r')
new_file = open(r"data/Homologues_named.fasta", 'w')


records = AlignIO.read(original_file, 'fasta')

for record in records:
    print(record.description)
    spl1 = str(record.description).split(' ', maxsplit=1)
    end = spl1[0].split('/')[-1]
    # print(end)
    mid = spl1[1]\
        .replace(', whole genome shotgun sequence','')\
        .replace('contig ', '')\
        .replace('contig', 'con.')
    mid = mid.split(' genome assembly ', maxsplit=1)
    mid = mid[1] if len(mid)>1 else mid[0]

    # print(mid)
    record.id = str('Hom./'+mid+' wgs/'+end)\
        .replace('(','').replace(')','')\
        .replace("genome assembly", 'g.a.')

    record.name = ''
    record.description = ''
    print(record.id)

records.sort()

AlignIO.write(records,  new_file, 'fasta')







