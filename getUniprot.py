from Bio import AlignIO
from bioservices import UniProt
u = UniProt()

def split_mine(str):
    # print(str)
    l = str.split('\n')
    cols = l[0].split('\t')
    values = l[1].split('\t')

    dict = {cols[i]:values[i] for i in range(len(cols))}
    return dict


results = u.search("Blyttiomyces helicus", columns="id, organism, lineage(SUPERKINGDOM), lineage(all)", limit=1)
print(results)


# [print(key,record.__getattribute__(key)) for key in record.__dict__.keys()]