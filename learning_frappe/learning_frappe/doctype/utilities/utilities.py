# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Utilities(Document):
	pass

@frappe.whitelist()
def get_info(name):
	doc = frappe.get_doc('Utilities',name)

	# Record = doc.name
	# Name = doc.name1
	# Email = doc.email
	# Phone = doc.phone
	# Date = doc.date

	# return Record, Name, Email, Phone, Date

	return{
		'Record':doc.name,
		'name': doc.name1,
		'email':doc.email,
		'phone':doc.phone,
		'date':doc.date
	}

@frappe.whitelist()
def single_parameter(a):
	a = int(a)
	a = a*a
	return a

@frappe.whitelist()
def single_parameter(role_profile):
	if role_profile == 'Admin':
		return 'Single Parameter'
	else:
		return 'Error'

@frappe.whitelist()
def calculate_total(a,b):
	import time
	time.sleep(2)
	a = int(a)
	b = int(b)
	return a+b 