

class Utils:
	
	@staticmethod
	def input_path():
		while True:
			path = input('Введите название json файла с окончанием .json: ')
			check = path.count(' ')
			verifed = True
			if len(path) == 0:
				return None
			if not path.endswith('.json'):
				print('Файл должен заканчиваться на .json')
				verifed = False
				
			if not check == 0:
				print('файл не должен содержать пробелы')
				verifed = False
				
			r = True
			for elem in [':', '*', '?', '»', '<', '>', '|']:
				if elem in path:
					r = False
					
			if not r:
				print('Вы использовали в названии недопустимые символы')
				verifed = False
			
			if verifed:
				return path