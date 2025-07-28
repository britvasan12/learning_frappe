# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document	
# from pypika.functions import Count
# from pypika.functions import Avg
# from pypika.functions import Sum
# from pypika.functions import Min
# from pypika.functions import Max
# from pypika.functions import Abs
# from pypika.functions import IfNull
# from pypika.functions import Concat
# from pypika.functions import Extract
# from frappe.query_builder import DocType

class StudentRecord(Document):
	pass
	# query = frappe.db.sql("""
	# 	SELECT 
	# 		`name` as `Student_ID`,
	# 		`student_name`,
	# 		`status`,
	# 		`contact`
	# 	FROM 
	# 		`tabStudent Record`
	# 	WHERE
	# 		`name`='1'
	# """)
	# frappe.log_error('Query', query)
	# --------------------------------------------------
	# query = frappe.qb.get_query("Student Record")
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -------------------------------------------------
	# query = frappe.qb.get_query('Student Record', fields=['student_name', 'class_and_sec'], filters={'name':'1'})
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -------------------------------------------------
	# query = frappe.qb.get_query('Student Record', 
	# fields=['student_fee.fees', 'student_fee.first_graduate', 'student_fee.paid'], 
	# filters={'name':'2'})
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -------------------------------------------------
	# query = frappe.qb.get_query('Student Record', 
	# fields=['name as ID', 'student_name as Name', {'student_fee':['fees', 'paid']}],
	# filters={'name':'4'})
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -------------------------------------------------
	# query = frappe.qb.get_query('Student Record', 
	# fields=['name', 'student_name', {'student_fee':['fees', 'paid']}],
	# limit=2)
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# ------------------------------------------------

	# student = frappe.qb.DocType("Student Record")
	# fee = frappe.qb.DocType("Student Fee")


	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name==fee.parent)
	# 	.select(
	# 		student.name, 
	# 		student.student_name, 
	# 		student.status, 
	# 		student.class_and_sec, 
	# 		fee.fees, 
	# 		fee.paid
	# 	)
	# 	.where(student.name=='1')
	# )
	# --------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		Count(fee.fees).as_("Student Fee")
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# ------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		Sum(fee.fees).as_("Student Fee")
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		Avg(fee.fees).as_("Student Fee")
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		Min(fee.fees).as_("Student Fee")
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# --------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		Min(fee.fees).as_("Student Fee")
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -------------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		Max(fee.fees).as_("Student Fee")
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# -----------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		Abs(fee.fees).as_("Student Fee")
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)
	# ----------------------------------------------------
	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		student.class_and_sec,
	# 		IfNull(student.email, 'test@example.com').as_('EMail')
	# 	)
	# 	.where(student.name=='1')
	# )
	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)

	# query = (
	# 	frappe.qb.from_(student)
	# 	.select(
	# 		Concat(student.student_name,"(", student.email, "-", student.class_and_sec, ")"). as_("Concatination")
	# 	)
	# 	.where(student.name == '1')
	# )

	# data = query.run(as_dict=True)
	# frappe.log_error('Query', data)

	# query = (
	# 	frappe.qb.from_(student)
	# 	.join(fee).on(student.name == fee.parent)
	# 	.select(
	# 		student.student_name,
	# 		Extract("Day", student.dob).as_("Day")
	# 	)
	# 	.where(student.name=='1')
	# )

	# data = query.run(as_dict=True)
	# frappe.log_error('Query',data)
