'''
Downloads all papers that you don't have locally.
'''

import os, urllib2

directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d) and not d.startswith('.')]

while len(directories) > 0:
	try:
		curr_dir = directories[0]
		# Pull any papers not found in this directory
		paper_list = open(curr_dir + '/papers.txt').readlines()
		papers = [p.rstrip().split(':::')[0] for p in paper_list]
		links = [p.rstrip().split(':::')[1] for p in paper_list]

		for i in range(len(links)):
			file_path = curr_dir + '/papers/' + papers[i].lower().replace(' ', '_')[0:50] + '.pdf'
			print(file_path)
			if os.path.isfile(file_path):
				os.remove(file_path)

		# Recurse into sub directories
		new_dirs = [curr_dir + '/' + d for d in os.listdir(curr_dir)]
		new_dirs = [d for d in new_dirs if os.path.isdir(d) and 'papers' not in d]
		directories.extend(new_dirs)

		# Remove this directory
		del directories[0]
	except Exception as e:
		print(exception)