# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EventMethod(Document):
	pass
	"""Validate"""
	# def validate(self):
	# 	if self.name1:
	# 		name = self.name1.title()
	# 		self.name1 = name

	# 	if not self.email:
	# 		frappe.throw("Email field is Empty!")
		
	# 	if "@" not in self.email:
	# 		frappe.throw("Enter the valid email address")

	# 	if not self.phone.isdigit():
	# 		frappe.throw("Digits only!")

	# 	if len(self.phone) < 14 or len(self.phone) > 14 :
	# 		frappe.throw("Invalid Mobile Number!")

	# 	if self.status == "":
	# 		frappe.throw("Status field is Empty!")

	# 	# if self.status == "":
	# 	# 	self.status = "Draft"

	"""Before save"""

	# def before_save(self):
	# 	if self.name1:
	# 		pref= "Mr. "
	# 		if not self.name1.startswith(pref):
	# 			self.name1 = f"{pref}{self.name1}"

	"""On change"""

	# def on_change(self):
	# 	if self.docstatus == 0:
	# 		self.status = "Draft"
	# 	elif self.docstatus == 1:
	# 		self.status = "Submitted"
	
	# 	elif self.docstatus == 2:
	# 		self.status = "Cancelled"


	"""On cancel"""

	# def on_cancel(self):
	# 	frappe.msgprint(f"{self.name} has been cancelled successfully.")

	"""Before cancel"""

	# def before_cancel(self):
	# 	frappe.msgprint(f"{self.name} has been cancelled successfully.")

