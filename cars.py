def make_car(manfacturer, model, **car_info):
	car_info['manfacturer'] = manfacturer
	car_info['model'] = model
	return car_info

car = make_car('BMW', '330xi', color = 'Silver', packages = 'M Package')
print(car)