# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Register(Document):
	pass

	"""Validate"""
	# def validate(self):
	# 	if self.first_name:
	# 		fname = self.first_name.capitalize()
	# 		self.first_name = fname	

	# 	if self.first_name and self.last_name:
	# 		self.full_name = f"{self.first_name} {self.last_name}"

	# 	if not self.email:
	# 		frappe.throw("Email field is Empty!")
		
	# 	if '@' not in self.email:
	# 		frappe.throw("Invalid Email Address")	
		
	# 	if not self.phone.isdigit():
	# 		frappe.throw("Invalid Numbers")

	# 	if len(self.phone) != 10:
	# 		frappe.throw("Must be 10 Numbers")

	# 	if self.gender == "":
	# 		frappe.throw("Please select the gender!")

	# 	if not self.small_text_wprj:
	# 		self.small_text_wprj = "This is default message!"


	"""Before validate"""
	# def before_validate(self):
	# 	if not self.signed_in:
	# 		self.signed_in = 1

	# 	if self.first_name and self.last_name:
	# 		self.full_name = f"{self.first_name} {self.last_name}"




	"""Before naming"""
	# def before_naming(self):
	# 	if self.title:
	# 		title = self.title.strip(" ").title()
	# 		frappe.msgprint(f"The title is:{self.title}")



	"""After Insert"""
	# def after_insert(self):
	# 	frappe.msgprint(f"After Insert Code {self.first_name}")
		

	"""Before Insert"""
	# def before_insert(self):
	# 	if self.first_name and self.gender:
	# 		if self.gender == 'Male':
	# 			prefix = "Mr. "
	# 		elif self.gender == 'Female':
	# 			prefix = "Mrs. "
	# 		else:	
	# 			prefix = ""

	# 		if not self.first_name.startswith(prefix):
	# 			self.first_name = f"{prefix}{self.first_name}"



	# def get_full_name(self):
	# 	self.full_name = f"{self.first_name}{self.last_name}"
	# 	self.save()


	"""Before save"""
	# def before_save(self):
	# 	if self.first_name:
	# 		if self.gender == 'Male':
	# 			pref = 'Mr.'
	# 			self.first_name = f"{pref}{self.first_name}"
	# 		elif self.gender == 'Female':
	# 			pref = 'Mrs.'
	# 			self.first_name = f"{pref}{self.first_name}"
	# 		else:
	# 			return self.first_name
		
	# 	'''
	# 	if self.first_name:
	# 		if self.gender == 'Male':
	# 			pref = 'Mr.'
	# 			self.first_name = f"{pref}{self.first_name}"
	# 		else:
	# 			pref = 'Mrs.'
	# 			self.first_name = f"{pref}{self.first_name}" 
	# 	'''