# coding: utf-8
import json

# from species_names.taxonomy import fasta_delimiter

fasta_delimiter = ">"

def main():

    with open(json_in) as color_js:
        colors = json.load(color_js)

    with open(f_in, "r") as fasta:
        with open(out_f, "w") as out:

            out.write("TREE_COLORS\n")
            out.write("SEPARATOR SPACE\n")
            out.write("DATA\n")

            line = fasta.readline()

            while line:
                if line.startswith(fasta_delimiter):
                    name = line[1:-1]

                    for key, md in colors.items():
                        if name.startswith(key):
                            out.write("{id} range {color} {label}\n".format(
                                id=name,
                                color=md["color"],
                                label=md["label"]
                            ))

                line = fasta.readline()


if __name__ == "__main__":
    json_in = "species_names/plants_colors.json"
    f_in = "trees/plants_subtree_names.txt"
    out_f = "trees/43colors_plants.txt"
    main()
