from bioservices import UniProt
from Bio import AlignIO
import pandas as pd

u = UniProt()

def split_mine(str):
    # print(str)
    l = str.split('\n')
    cols = l[0].split('\t')
    values = l[1].split('\t')

    dict = {cols[i]:values[i] for i in range(len(cols))}
    return dict


original_file = open(r"data/Proteins_named_Euk_Vir_Bac.fasta", 'r')
csv_file = open(r"data/proteins_lineage.csv", 'w')

cols = ["name", "id","1", "2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
df = pd.DataFrame(columns=cols)
print(df)
#
records = AlignIO.read(original_file, 'fasta')
#
for record in records:
    # print(record.id)
    # print(record.description)
    spl = str(record.description).split("/")
    name = record.description
    id = spl[-2]


    try:
        results = split_mine(u.search(id, columns="id, organism, lineage(SUPERKINGDOM), lineage(all)", limit=1))
        if results["Organism"] == '':
            lineage = ['No_identified']
            print('No_identified')
        else:
            lineage = str(results["Taxonomic lineage (all)"]).split(", ")
            print(lineage)


    except Exception as e:
        print('ошибка1', e)
        try:
            spl = str(record.description).split("[")
            search = spl[1][:-1]
            results = split_mine(u.search(search, columns="id, organism, lineage(SUPERKINGDOM), lineage(all)", limit=1))
            if results["Organism"] == '':
                lineage = ['No_identified']
                print('No_identified')
            else:
                lineage = str(results["Taxonomic lineage (all)"]).split(", ")
                id = results["Entry"]
                print(lineage)

        except Exception as e:
            print('ошибка2', e)
            lineage = ['Error2']

    if lineage[0]=='cellular organisms':
        lineage = lineage[1:]

    lineage = [name, id] + lineage
    new_data = dict(zip(cols, lineage))
    # new_data += {"name": name, "id": id}
    print(new_data)
    df = df.append(new_data, ignore_index=True)
    # print(df.loc[0,:])

#     print(record.id)
#
# records.sort()
#
# AlignIO.write(records,  new_file, 'fasta')
df.to_csv(csv_file)
csv_file.close()
print(df)







