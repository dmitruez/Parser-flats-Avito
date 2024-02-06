import json
from entity import Flat


class Service:
	
	
	@staticmethod
	def save_to_json(flats: list[Flat], path=None):
		if path is None:
			path = 'flats.json'
		path_to_dir = 'json_data/' + path
		with open(path_to_dir, 'w+', encoding="utf-8") as f:
			
			data = {}
			for flat in flats:
				data_flat = {
					"price": flat.price,
					"area": flat.area,
					"description": flat.description
					}
					
				data[flat.href] = data_flat
			
			json.dump(data, f, ensure_ascii=False, indent=2)