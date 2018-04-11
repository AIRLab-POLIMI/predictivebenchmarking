import csv
import pickle

with open('stats.csv', 'r') as csvfile:
    content = list(csv.reader(csvfile, delimiter=','))

# pickle.dump(content, open('data/clinical_data.p', 'wb'))
# print content
final_dict = {}
final_dict['columns'] = content[0]

for index in range(1, len(content)):
    element = content[index]
    if len(element) == 0:
        continue
    final_dict[element[0]] = {}
    for subindex in range(0, len(element)):
        subelement = element[subindex]
        if final_dict['columns'][subindex] == 'dataset' :
        	final_dict[element[0]][final_dict['columns'][subindex]] = subelement
        else :
        	final_dict[element[0]][final_dict['columns'][subindex]] = float(subelement)

print final_dict
print final_dict['columns']
pickle.dump(final_dict, open('pickle.p', 'wb'))