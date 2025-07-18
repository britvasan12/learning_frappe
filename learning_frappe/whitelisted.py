import frappe

@frappe.whitelist()
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    frappe.msgprint(f"Custom count logic for {doctype}")
    return frappe.db.count(doctype, filters)
