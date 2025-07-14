# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DatabaseAPI(Document):
	pass
	 
@frappe.whitelist()
def random():
	'''frappe.db.get_list'''
	# frappe.get_list also works!!

	# movies = frappe.db.get_list('Database API')

	# movies = frappe.db.get_list('Database API', pluck='name')

	# movies = frappe.db.get_list('Database API',
	# filters={
	# 	'genre': 'Commercial'	
	# },
	# fields = ['name', 'movie_name', 'release_date'],
	# order_by = 'name asc',
	# start = 0,
	# page_length = 2,
	# as_list = True
	# )
	# return movies

	# movies = frappe.db.get_list('Database API', 
		# filters = {
		# 	'release_date': ['<', '2025-07-31']
		# },
		# fields = ['name', 'movie_name', 'release_date'],
		# order_by = 'release_date asc'

		# filters = [
		# 	['release_date', 'between', ['2025-07-01', '2025-07-19']]
		# ],
		# fields = ['name', 'movie_name', 'release_date'],
		# order_by = 'release_date asc'

		# filters = {
		# 	'movie_name': ['like','%A%']
		# },
		# fields = ['name', 'movie_name', 'release_date'],
		# order_by = 'release_date asc'

		# fields = ['count(genre) as Genre', 'genre'],
		# group_by = 'genre'
	# )
	# return movies

	'''frappe.db.get_all same as frappe.db.get_list'''
	# frappe.get_all also works!!

	# movie = frappe.db.get_all('Database API', pluck='name')
	# return movie

	'''frappe.db.get_value'''
	# frappe.get_value and frappe.db.get_values also works!!
	# frappe.db.get_values this will return an array!

	# Get_value = frappe.db.get_value('Database API', 'DB-API-004', 'movie_name')
	# return Get_value

	# return just the value

	# Get_value = frappe.db.get_value('Database API', 'DB-API-004', ['movie_name', 'genre'])
	# return Get_value

	# as_dict = True -> returns with fieldname

	# Get_value = frappe.db.get_value('Database API', 'DB-API-004', ['movie_name', 'genre'], as_dict = True)
	# return Get_value

	'''with filters return the first matching value!'''

	# Get_value = frappe.db.get_value('Database API', {'genre': 'Commercial'}, ['movie_name','genre'])
	# return Get_value

	'''frappe.db.set_value'''
	# frappe.set_value also works!

	# value = frappe.db.set_value('Database API', 'DB-API-003', {
	# 	'movie_name': 'Leo 2',
	# 	'genre': 'Action'
	# })
	# return value

	'''frappe.db.exists'''

	# exist = frappe.db.exists('Database API', 'DB-API-001')
	# if exist:
	# 	return 'True'
	# else:
	# 	return 'False'

	'''frappe.db.count'''

	# count = frappe.db.count('Database API', {'genre': 'Commercial'})
	# return count

	'''frappe.db.delete'''
	# we can delete whole records! as well conditions deletions also we can do!


	# doc = frappe.db.delete('Database API',{
	# 	'release_date': ['<', '2025-07-16']
	# })

	# if doc:
	# 	return "Deleted!"

	'''frappe.db.truncate'''
	# delete the whole document like delete all, no conditions for that only delete all or nothing concept!

	# doc = frappe.db.truncate('Database API')
	# if doc:
	# 	return 'Trucated!'
	
	'''frappe.db.describe'''
	# whole description about the doctype kind of meta data of the doctype!

	# doc = frappe.db.describe('Database API')
	# return doc

	'''frappe.db.sql'''
	# to write and execute raw SQL query!

	# movies = frappe.db.sql("""
	# 	SELECT 
	# 		movie_name, genre, release_date 
	# 	FROM 
	# 		`tabDatabase API` 
	# 	WHERE release_date='2025-07-14';
	# """
	# )
	# return movies

	'''we can execute multiple database query'''
	# here we have mariabd only so mariadb will only works!

	# data = frappe.db.multisql({
	# 	'mariadb':"SELECT * FROM `tabDatabase API`",
	# 	'postgres':"SELECT * FROM `tabDocument API`"
	# })
	# print(data)

	'''frappe.db.change_column_type'''
	# change the column type in db level not in UI!

	# change = frappe.db.change_column_type('Database API', 'movie_name', 'VARCHAR(255)')
	# return change

	'''add unique in DB level'''

	# doc = frappe.db.add_unique('Database API', 'movie_name')
	# return doc

	









