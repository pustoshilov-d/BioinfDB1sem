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


results = u.search("MCP_IIV6", columns="id, organism")
print(results['Organism'])


# [print(key,record.__getattribute__(key)) for key in record.__dict__.keys()]