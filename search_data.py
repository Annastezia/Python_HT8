def search(user_list):
	q = input('Что нужно найти? Введите: \n')
	value = True
	for i in user_list:
		if q in i:
			print(i)
			value = False
	if value:
		print('К сожалению, пользователь не найден')
	return q + f';{not value}'