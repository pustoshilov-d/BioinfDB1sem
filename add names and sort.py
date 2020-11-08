from bioservices import UniProt
from Bio import AlignIO
u = UniProt()

def split_mine(str):
    # print(str)
    l = str.split('\n')
    cols = l[0].split('\t')
    values = l[1].split('\t')

    dict = {cols[i]:values[i] for i in range(len(cols))}
    return dict


original_file = open(r"data/Proteins_origin.fasta", 'r')
# original_file = open(r"data/Proteins_short.fasta", 'r')
new_file = open(r"data/Proteins_named_sorted.fasta", 'w')


records = AlignIO.read(original_file, 'fasta')

for record in records:
    print(record.id)
    organism = ''
    try:
        find = record.id.split('/')[0]
        results = split_mine(u.search(find, columns="id, organism"))
        if results["Organism"] == '':
            organism = 'No_identified'
        else:
            organism = results["Organism"]

    except Exception as e:
        print('ошибка', e)
        organism = 'Error'

    record.id = organism.replace(' ', '_')+ "/"+record.id
    record.name = ''
    record.description = ''
    print(record.id)

records.sort()

AlignIO.write(records,  new_file, 'fasta')







