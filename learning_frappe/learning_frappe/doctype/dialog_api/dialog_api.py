# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class DialogAPI(Document):
	pass


# for the method 1 and 2 this py code is enough simple and clean

@frappe.whitelist()
def confirm_data(name):
	doc = frappe.get_doc("Dialog API", name)
	if doc.docstatus == 0:
		doc.submit()
		return "Document Submitted Successfully"
	return "Document already submitted"


# this method is complex but it works with a notification after refresh the form the state 
# has turn as submitted!

@frappe.whitelist()
def confirm_data(**kwargs):

	# Get the JSON string from args (this happens in server_action calls)
	args_json = kwargs.get('args')
	frappe.log_error("Backend Called", f"Raw args: {args_json}")

	if not args_json:
		frappe.throw("Arguments are missing")

	# Parse the JSON string to get actual dict

	try:
		args = json.loads(args_json)
	except Exception as e:
		frappe.throw(f"Invalid arguments: {e}")

	docname = args.get("name")
	frappe.log_error("Parsed Name", f"Docname: {docname}")

	if not docname:
		frappe.throw('Document Name is Required')

	# Get the document
	doc = frappe.get_doc('Dialog API', docname)

	if doc.docstatus == 0:
		doc.submit()
		return f'Document {docname} Submitted Successfully!'
	else:
		frappe.throw('Document is already Submitted')

@frappe.whitelist()
def success(name):
	if not name:
		frappe.throw('Document Not Available!')

	doc = frappe.get_doc('Dialog API', name)

	if doc.docstatus == 0:
		doc.submit()
		return f'Successfully Submitted'

@frappe.whitelist()
def failure(name):
	if not name:
		frappe.throw("Document Not Available")
	
	doc = frappe.get_doc('Dialog API', name)

	if doc.docstatus == 1:
		doc.cancel()
		return f'Successfully Cancelled'