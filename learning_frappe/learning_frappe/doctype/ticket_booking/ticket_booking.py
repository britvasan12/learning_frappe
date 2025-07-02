# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document

def generate_ticket_id():
		return 'TKT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class TicketBooking(Document):
	def before_save(self):
		if self.customer_name:
			self.email = f"{self.customer_name.lower()}@gmail.com"

		if self.movie_name:
			self.ticket = self.movie_name

	
	def validate(self):
		if self.ticket_count:
			self.ticket_price = int(self.ticket_count) * 200

		if self.payment_method is not None:
			self.paid = 1

		if self.movie_name and not self.ticket_id:
			self.ticket_id = self.generate_ticket_id()

	