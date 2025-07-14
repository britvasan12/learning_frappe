# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FormEvents(Document):
	pass


@frappe.whitelist()
def calculate_total(count, price):
	count = int(count)
	price = float(price)

	total = count * price
	return total