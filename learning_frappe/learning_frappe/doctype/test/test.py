# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Test(Document):
	pass
	# def before_save(self):
		# self.barcode = self.full_name
		# self.save()
		# frappe.db.set_value("Test",self.name,{
		# 	"barcode":self.barcode
		# })
		# frappe.db.commit()
	# 	frappe.delete_doc('Test', 'Test-018')
	# 	frappe.msgprint('Deleted')

# 	def set_name(self):
# 		frappe.msgprint(f'The Name is: {self.full_name}')

# @frappe.whitelist()
# def method_test(name):
# 	doc = frappe.get_doc('Test', 'Test-008')
# 	doc.run_method('set_name')
