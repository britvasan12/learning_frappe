# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DocumentAPI(Document):
	pass
		
# 	# def before_save(self):
# 	# 	pass
# 		# get_doc and get_doc insert

# 		'''
# 		if self.status == 'Open':
# 			if frappe.db.exists('Test', 'Test-015'):
# 				test_doc = frappe.get_doc('Test', 'Test-015')
# 				test_doc.delete()
# 				frappe.msgprint(f'{test_doc.name} Deleted from Test Doc Successfully!')

# 		elif self.status in ['Closed']:
# 			frappe.throw('Test Doc Cannot be deleted because of status is not opened')

# 		else:
# 			doc2 = frappe.get_doc({
# 				'doctype': 'Test',
# 				'full_name': 'Raja',
# 				'age': '59'
# 			})
# 			doc2.insert()
# 			frappe.msgprint(f'{doc2.name} New Record Created on Test Doc')
# 		'''



# 		# get_last_doc to get last record or document from the doctype!
		
# 		'''
# 		test = frappe.get_last_doc('Test')
# 		frappe.msgprint(f'{test.name} this is the last record on Test Doc!')
# 		'''

# 		# get_last_doc with filters!

# 		'''
# 		test = frappe.get_last_doc('Test', filters={'full_name': 'Raja'})
# 		frappe.msgprint(f'Last record with the name of Raja is :{test.name}')
# 		'''

# 		# As per documentation it states that it get the document from cache before hitting to the DB!
# 		# but it same as get_doc

# 		'''
# 		test = frappe.get_cached_doc('Test','Test-025')
# 		frappe.msgprint(f'Document from Cache: {test.full_name}')
# 		'''


# 		# new_doc-> to create a new document in the doctype by inserting

# 		'''
# 		newDoc = frappe.new_doc('Test')
# 		newDoc.full_name = 'Thalapathy'
# 		newDoc.age = '51'

# 		newDoc.insert()
# 		frappe.msgprint(f'{newDoc.name} is a New Document! and its created on Test')
# 		'''

# 		# delete_doc-> It will delete the particular record! but Its return None while msgprint
# 		# Because 72th delete the record its gone, after that we tried to print so None!

# 		'''
# 		d = frappe.delete_doc('Test', 'Test-005')
# 		frappe.msgprint(f'{d} is deleted Successfully!')
# 		'''

# 		# rename_doc 

# 		'''
# 		rename = frappe.rename_doc('Test','Test-011','Test-012')
# 		frappe.msgprint(f'{rename} is Renamed Successfully!')
# 		'''

# 		# rename_doc with merge as False same like above

# 		'''
# 		rename = frappe.rename_doc('Test','Test-012','Test-011', merge=False)
# 		frappe.msgprint(f'{rename} is Renamed Successfully!')
# 		'''

# 		# rename_doc with merge true it delete the oldname record(Test-026) and remains newname record only

# 		'''
# 		rename = frappe.rename_doc('Test','Test-026','Test-014', merge=True)
# 		frappe.msgprint(f'{rename} is Renamed Successfully!')
# 		'''

# 		# get_meta-> it will give all the metadata(schema details) of the doctype!

# 		'''
# 		meta = frappe.get_meta('Test')
# 		print(meta)
# 		print(meta.fields)
# 		print(meta.is_submittable)
# 		print(meta.istable)
# 		print(meta.permissions)
# 		'''

# 		# doc.save() -> update the existing record or create a new record by using new_doc
# 		# doc.insert() -> create a new record and insert to save the record!
# 		# both are doing the same but works different ways!

# 		# self.update_test_doc() 
# 		'''
# 		def update_test_doc(self):
# 			doc = frappe.get_doc('Test','Test-014')
# 			doc.full_name = 'Britto'
# 			doc.age = '23'
# 			doc.save(
# 				ignore_permissions = True,
# 				ignore_version = True
# 			)

# 			frappe.msgprint(f'{doc.name} is Updated Successfully!')
# 		'''


# 		# Inside and Outside function
# 		"""
# 		If write the function inside of the class self is needed, it act as instance method of the class, but 
# 		if you write a function outside of the class it will act as a standalone function self doesnot needed
# 		"""

# 		# doc.delete() -> same as delete_doc

# 		'''
# 		doc = frappe.get_doc('Test','Test-007')
# 		doc.delete()
# 		frappe.msgprint(f'{doc.name} Deleted Successfully!')
# 		'''

# 		# get_doc_before_save() -> Find the changes old to new value

# 		'''
# 		old_doc = self.get_doc_before_save()
# 		if old_doc:
# 			if old_doc.status != self.status:
# 				frappe.msgprint(f'Status Changed from {old_doc.status} to {self.status}')

# 			if old_doc.full_name != self.full_name:
# 				frappe.msgprint(f'Fullname Changed from {old_doc.full_name} to {self.full_name}')

# 		else:
# 			frappe.msgprint('Wtf!')			
# 		'''

# 		# has_value_changed() -> return or false if the given field values are changed!?

# 		'''
# 		changes = self.has_value_changed('first_name')
# 		if changes:
# 			frappe.msgprint(f'First Name values are changed: {changes}')
# 		'''

# 		# doc.reload() -> Used to reload the DB 

# 		'''
# 		doc = frappe.get_doc('Test', 'Test-027')

# 		frappe.db.set_value('Test', 'Test-027', 'full_name', 'Thalapathy')

# 		frappe.msgprint(f'Before Reload: {doc.full_name}')

# 		doc.reload() #--> This will reload the database and get the latest value from DB

# 		frappe.msgprint(f'After Reload: {doc.full_name}')
# 		'''

# 		# doc.check_permission -> Not worked for me?

# 		'''
# 		doc = frappe.get_doc('Test', 'Test-027')
# 		# frappe.msgprint(frappe.session.user)

# 		if doc.check_permission(permtype='write'):
# 			frappe.throw('This User does not have a permission to write!')

# 		elif not doc.check_permission(permtype='write'):
# 			doc.full_name = 'Thalapathy Vijay'
# 			doc.save()

# 			frappe.msgprint('This User have a permission to write!')
# 		''' 

# 		# get_title() -> to get the title of the document! For example we have fullname field if we 
# 		# set that field to title_field in doctype settings we get this as title! (or)
# 		# Nothind is set we will name(Test-027) of the document as title

# 		'''
# 		doc = frappe.get_doc('Test', 'Test-027')
# 		title = doc.get_title()

# 		frappe.msgprint(f'Title:{title}')
# 		'''

# 		# db_set() 

# 		'''
# 		doc = frappe.get_doc('Test','Test-025')
# 		# doc.db_set('age','32', commit=True)
# 		# doc.db_set('age','67')
# 		# doc.db_set('age','29', commit=False)
# 		# doc.db_set('age','29', update_modified=False)  
# 		frappe.msgprint('Set')
# 		'''

# 		# doc.append() -> to add new row in child table using append

# 		'''
# 		doc = frappe.get_doc('Test', 'Test-024')
# 		doc.append('test_child',{
# 			'location': 'Chennai',
# 			'phone': '6766576565'
# 		})

# 		doc.save()
# 		frappe.msgprint('Appended!')
# 		'''

# 		# get_url() -> to get the path of the doc 
# 		# O/P---> URL: /app/test/Test-024

# 		'''
# 		doc = frappe.get_doc('Test', 'Test-024')
# 		url = doc.get_url()
# 		frappe.msgprint(f'URL: {url}')
# 		'''

# 		# add_comment() -> Comment, Edit Worked! Shared Didn't

# 		'''
# 		doc = frappe.get_doc('Test', 'Test-024')
# 		# doc.add_comment('Comment', 'First Comment in Test-024')
# 		# doc.add_comment('Edit', 'Edited?')
# 		user = frappe.session.user
# 		doc.add_comment("Shared", "{0} shared this document with everyone".format(user))
# 		frappe.msgprint('Comment added!')
# 		'''

# 		# add_seen() -> used to mark the user had seen the document
# 		'''
# 		doc = frappe.get_doc('Test', 'Test-008')
# 		doc.add_seen()
# 		doc.save()
# 		frappe.msgprint('Seened!')
# 		'''

# 		# add_viewed() -> used to record the user viewed the document!

# 		'''
# 		doc = frappe.get_doc('Test', 'Test-008')
# 		doc.add_viewed()
# 		doc.save()
# 		frappe.msgprint('Viewed!')
# 		'''

# 		# add_tag(), remove_tag(), get_tags()-> Not worked?

# 		'''
# 		# doc = frappe.get_doc('Test', 'Test-008')
# 		# doc.add_tag('Britvasan R')
# 		# frappe.msgprint('Tag is added!')

# 		# doc = frappe.get_doc('Test', 'Test-008')
# 		# doc.remove_tag('Britvasan R')
# 		# frappe.msgprint('Tag is removed!')

# 		# doc = frappe.get_doc('Test', 'Test-008')
# 		# all_tag = doc.get_tags('Test', 'Test-008')
# 		# print(all_tag)
# 		'''

	


# ''' # update_test_doc()
# @frappe.whitelist()
# def update_test_doc():
# 	doc = frappe.get_doc('Test', 'Test-009')
# 	doc.full_name = 'Thalapathy Vijay'
# 	doc.age = '51'

# 	doc.save()

# 	doc.notify_update()

# 	return f"Notification: {doc.name} Has been Updated!"
# '''

# # @frappe.whitelist()
# # def shared_log():
# # 	doc = frappe.get_doc('Test', 'Test-024')
# # 	user = frappe.session.user
# # 	doc.add_comment('Shared', f'{user} Shared this Message!')
# # 	doc.save()
# # 	frappe.db.commit()
# # 	frappe.msgprint('Shared!')