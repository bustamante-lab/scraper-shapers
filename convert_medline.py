import sys

open_file = open(sys.argv[1], 'r')
file = open_file.readlines()
open_file.close()

#print(str(len(file)))

outfile = open("review_papers.txt", 'w')
outfile.write("PMID"+'\t'+"Date"+'\t'+"Title"+'\t'+"Abstract"+'\t'+"Author(s)"+'\t'+"Journal"+'\t'+"Journal Full")

line_counter = 0
article_counter = 0

for line in file:
	line = line.strip()
	
	if line.startswith("PMID"):
		line_items = line.split('- ')
		ID = line_items[1]
		outfile.write('\n'+str(ID)+'\t')
		article_counter = article_counter + 1
			
	elif line.startswith("DP"):
		line_items = line.split(' - ')
		date = line_items[1]
		outfile.write(date +'\t')
	
	elif line.startswith("TI"):
		current = line_counter
		line_items = line.split(' -')
		t1 = line_items[1]
		outfile.write(t1)
		while file[current+1].startswith(' ') == True:
			outfile.write(' '+file[current+1].strip())
			current = current + 1
		outfile.write('\t')
	
	elif line.startswith("AB  -"):
		current = line_counter
		line_items = line.split('-')
		a1 = line_items[1]
		outfile.write(a1)
		while file[current+1].startswith(' ') == True:
			outfile.write(' '+file[current+1].strip())
			current = current + 1
		outfile.write('\t')
	
	elif line.startswith("AU  -"):
		line_items = line.split('-')
		author = line_items[1]
		#print(author)
		outfile.write(author)
	
	elif line.startswith("TA  -"):
		line_items = line.split('-')
		source = line_items[1]
		outfile.write('\t')
		outfile.write(source)

	elif line.startswith("JT  -"):
		line_items = line.split('-')
		source_full = line_items[1]
		outfile.write('\t')
		outfile.write(source_full)
	 
	line_counter = line_counter + 1

outfile.close()

print("Number of articles printed to outfile 'review_papers.txt': " + str(article_counter))