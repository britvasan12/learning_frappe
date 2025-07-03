# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DocEvents(Document):

	# --> Worked
	def before_save(self):
		self.email = "brit@gmail.com"
		frappe.msgprint("Before save event triggered")                          
	
	# --> Not Working
	def after_save(self):
		frappe.msgprint("After Save event Triggered")                           

	# --> Not Working
	def on_save(self):
		frappe.msgprint('On save event triggered --> After Save')              

	# --> Worked
	def before_insert(self):
		self.bio = "Developer"
		frappe.msgprint("Before Insert event Triggered")                        

	# --> Worked
	def after_insert(self):
		self.phone = "6385517658"
		frappe.msgprint("After Insert event Triggered")                         

	# --> Worked
	def before_validate(self):
		if not self.email or '@' not in self.email:
			frappe.throw("Before Validate event Triggered--> Invalid Email")    

	# --> Worked
	def before_submit(self):
		if not self.phone or len(self.phone)<10:
			frappe.throw("Before Validate event Triggered--> Invalid Phone Number")
		else:
			frappe.msgprint(f'{self.name} Saved')                               

	# --> Not Working
	def after_submit(self):
		frappe.msgprint(f'After submit event Triggered')                        

	# --> Worked
	def on_submit(self):
		self.last_name = ' '
		self.full_name = f'{self.first_name} {self.last_name}'                 

		frappe.msgprint(f'After submit event triggered with name of on submit') 

	# --> Worked
	def before_cancel(self):
		frappe.throw("Before Cancel event Triggered")                       

	# --> Not Working
	def after_cancel(self):
		frappe.throw("After submit event triggered")                            

	# --> Worked
	def on_cancel(self):
		frappe.throw("Do you want to cancel? --> on cancel AS after_cancel")    

	# --> Not Working
	def before_delete(self):
		frappe.msgprint("Do you want to Delete?")                               

	# --> Worked
	def after_delete(self):
		frappe.throw("Do you want to Delete?")                                  

	# --> Not Working
	def on_delete(self):
		frappe.msgprint("Do you want to Delete?")                                