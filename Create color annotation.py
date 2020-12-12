import pandas as pd
import seaborn as sns
import numpy as np


csv_file = open(r"data/proteins_lineage.csv", 'r')


df = pd.read_csv(csv_file)
level = 1
for level in range(1,15):
    ann_file = open(r"annotations/color_level_"+str(level)+".txt", 'w')

    # print(df)
    print(level)
    values = df[str(level)].unique()
    # print(len(values))
    palette = sns.color_palette(None, len(values)).as_hex()
    # print(palette)

    dict_colors = {values[i]: palette[i] for i in range(len(values))}
    print(dict_colors)

    ann_file.write('TREE_COLORS\n')
    ann_file.write('SEPARATOR SPACE\n')
    ann_file.write('DATA\n')

    for index, row in df.iterrows():
        # print(pd.isnull(row["20"]))
        if not (pd.isnull(row[str(level)])):
            name = row['name']
            value = row[str(level)]

            name = name\
                .replace(" ","_")\
                .replace("[","")\
                .replace("]","")\
                .replace(",","")

            st = "'"+name+"' range "+dict_colors[value]+" "+value+"\n"
            ann_file.write(st)
            # print(st)


    ann_file.close()