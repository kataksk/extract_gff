import sys

gff_in = sys.argv[1]
gene_id = sys.argv[2]

id_list = list()
with open(gene_id, 'r') as il:
    for line in il:
        id_list.append(line.rstrip('\n'))

id_list_sorted = sorted(id_list)

with open(gff_in, 'r') as gi:
    lines = gi.readlines()
    lines_strip = [line.strip() for line in lines]
    for line in lines_strip:
        if line[line.find('ID=') + 3 : line.find(';')] in id_list:
            print(line)

# with open(gff_in, 'r') as gi:
#     lines = gi.readlines()
#     lines_strip = [line.strip() for line in lines]
#     for gene_id_each in id_list_sorted:
#         for line in lines_strip:
#             id_start = line.find('ID=')
#             id_end = line.find(';')
#             l_gene_id_each = [line for line in lines_strip if line[id_start + 3 : id_end] == gene_id_each]

# for line in l_gene_id_each:
#     print(line)




