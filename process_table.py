file = open("table1-descrip-new")
file_writer = open("table1.csv",'w')
meet_new_item = False
meet_right_name = False
count = 0
for line in file:
	# table_name = None
	line = line.strip()


	# print(line)
	if "Table of" in line:
		line = line.strip()
		tokens = line.split()
		table_name = tokens[2]
		print('*******'+table_name+'*************')
		file_writer.write(table_name+',N(%)'+'\n')
		continue

	elif "---------+--------+--------+" in line:
		meet_new_item = True
		continue

	elif meet_new_item:
		meet_new_item = False
		tokens = line.strip().split("|")
		# assert len(tokens) == 4
		if "Total" in line:
			print("*********")

		elif tokens[0].strip() != '0' and count == 0:
			meet_right_name = True
			first_num_c = tokens[1].strip()
			first_num_e = tokens[2].strip()
			print(tokens[0].strip() +'    '+first_num_c + '      ' + first_num_e + '\n')
			cate_name = tokens[0].strip()
			if cate_name == '1':
				cate_name = table_name
			# first_num_c = None
			# first_num_e = None
			count = 0
			continue

	elif meet_right_name:
		count = count + 1
		if count == 3:
			tokens = line.strip().split("|")
			second_num_c = str(round(float(tokens[1].strip()),1))
			second_num_e = str(round(float(tokens[2].strip()),1))

			print('     '+second_num_c + '   ' + second_num_e + '\n')
			file_writer.write(cate_name+',N(%)' +'\t'+first_num_c + "(" + second_num_c + "%)" + '\t' + first_num_e + "(" + second_num_e + "%)" + '\n')
			second_num_c = None
			second_num_e = None
			first_num_c = None
			first_num_e = None
			count = 0
			meet_right_name=False

