ft = raw_input('path_file: ')
ft_o = open(ft).readlines()
for i in ft_o:
	if '@yahoo.com' in i:
		print('ini yahoo: '+i)
		w_f = open('/sdcard/rs_replace.txt','a')
		w_f.write(i)
		w_f.close()
	else:
		print('ini bukan yahoo: '+i)
print('save as: rs_replace.txt ( in sdcard ) ')