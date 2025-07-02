# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Booking(Document):
	pass


# @frappe.whitelist()
# def calculate_total(ticket_count, price):
# 	ticket_count = int(ticket_count)
# 	price = float(price)

# 	total_amount = ticket_count * price
# 	return total_amount
