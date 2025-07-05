# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Viewer(Document):
	pass

# @frappe.whitelist()
# def viewer_data(full_name=None, email=None, contact=None, date=None):
# 	doc = frappe.get_doc({
# 		"doctype": "Viewer",
# 		"full_name": full_name,
# 		"email": email,
# 		"contact": contact,
# 		"date": date
# 	})
# 	doc.insert()
# 	frappe.db.commit()	
	
# 	# return [full_name, email, contact, date]
# 	return doc.name