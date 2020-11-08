def split_mine(str):
    # print(str)
    l = str.split('\n')
    cols = l[0].split('\t')
    values = l[1].split('\t')

    dict = {cols[i]:values[i] for i in range(len(cols))}
    return dict

from bioservices import UniProt

u = UniProt()
results = u.search("MCP_IIV6", columns="id, organism")
# print(results)
# results = u.search("organism:10090+and+reviewed:yes", columns="id,entry name", limit=2)
# print(results['Organism'])

from Bio import SeqIO

original_file = r"Proteins_1.fasta"
corrected_file = r"Proteins_named.fasta"

with open(original_file) as original, open(corrected_file, 'w') as corrected:
    records = SeqIO.parse(original_file, 'fasta')
    for record in records:
        # print(type(record))
        # print(record.keys)
        # print (record.id.split('/')[0])
        organism = ''
        try:
            results = split_mine(u.search(record.id.split('/')[0], columns="id, organism"))
            # print(results)
            if results["Organism"] == '':
                organism = 'No_identified'
            else:
                organism = results["Organism"]

        except:
            print('ошибка нахуй')
            organism = 'Error'

        record.id = organism.replace(' ', '_')+ "///"

        # if record.id == 'foo':
        #     record.id = 'bar'
        print(record.id)  # prints 'bar' as expected
        SeqIO.write(record, corrected, 'fasta')







