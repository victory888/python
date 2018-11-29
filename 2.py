import os
root_path = os.getcwd()
#print(root_path)
offset = len(root_path.split("\\"))
#print(offset)
for root,dirs,files in os.walk(root_path):
	#print(root)
	current_dir = root
	path_list = current_dir.split("\\")
	indent_level = len(path_list) - offset
	# print(path_list,len(path_list))
	print("\t"*indent_level,"\\"+path_list[-1])
	for f in files:
		file_name = os.path.splitext(f)[0]
		print("\t"*(indent_level+1),file_name)