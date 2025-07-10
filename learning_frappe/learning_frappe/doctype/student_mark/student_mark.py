# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudentMark(Document):
	pass

@frappe.whitelist()
def student_data(name):
	if not name:
		frappe.throw("Document Not Available")

	doc = frappe.get_doc('Student Mark', name)

	frappe.log_error("Data",frappe.as_json(doc))

	return {
		"name": doc.name,
		"student_name": doc.student_name,
		"subject": doc.subject,
		"marks": doc.marks,
		"status": doc.status
	}