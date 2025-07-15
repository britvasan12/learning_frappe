# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import (now, today, getdate, add_to_date, 
date_diff, days_diff, month_diff, pretty_date, format_duration, 
comma_and, comma_or, money_in_words, random_string, unique, 
get_abbr, validate_url, validate_email_address, validate_phone_number)
from datetime import datetime
import json
from frappe.utils import validate_json_string
from frappe.utils.pdf import get_pdf


class UtilityFunction(Document):
	pass


@frappe.whitelist()
def my_method():
	pass
	'''now()'''
	# frappe.msgprint(f'Current time:{now()}')
	# frappe.msgprint(f'Current Date: {frappe.format(now())}')
	'''today'''
	# frappe.msgprint(f'Today: {today()}')
	# today_date = datetime.now().strftime('%d-%m-%Y')
	# return today_date

	'''add_to_date'''
	# after_10_days = add_to_date(datetime.now(), days=10, as_string=True)
	# return after_10_days


	# month = add_to_date(datetime.now(), months=2)
	# return month


	# D = add_to_date(datetime.now(), days=10, as_string=True, as_datetime=True)
	# return D


	# year = add_to_date(None, years=6)
	# return year

	
	'''date_diff'''
	# date1 = today()
	# date2 = add_to_date(date1, days=20)
	# return date_diff(date2, date1)

	'''days_diff'''
	# day1 = today()
	# day2 = add_to_date(day1, days=15)
	# return days_diff(day2, day1)

	'''month_diff'''

	# day1 = '2025-07-15'
	# day2 = add_to_date(day1, days=60)
	# return month_diff(day2, day1)

	'''pretty_date'''
	# return pretty_date(add_to_date(now(), minutes=-10))
	# return pretty_date(add_to_date(now(), hours=-10))
	# return pretty_date(add_to_date(now(), months=-10))
	# return pretty_date(add_to_date(now(), years=-10))

	'''format_duration'''

	# return format_duration(50)
	# return format_duration(1000)
	# return format_duration(2000)
	# return format_duration(500000, hide_days=True)

	'''comma_and'''

	# num = comma_and([1,2,3])
	# return num

	# props = comma_and(['Apple', 'Ball', 'Cat'], add_quotes=False)
	# return props

	# letters = comma_and('abcd')
	# return letters

	# A = comma_and(['A'])
	# return A

	# letters = comma_or('abcd')
	# return letters

	# missing_fields = ['Email', 'Phone', 'Address']
	# frappe.throw(f"Please fill in the following fields: {comma_and(missing_fields, add_quotes=False)}.")

	# invalid_roles = ['Guest', 'Anonymous']
	# frappe.msgprint(f"The following roles are not allowed: {comma_and(invalid_roles)}")

	# selected = ['Option A', 'Option B', 'Option C']
	# frappe.msgprint(f"You selected {comma_and(selected, add_quotes=False)}.")


	'''money_in-words'''

	# money1 = money_in_words(10000000.50, 'USD')
	# return money1

	'''validate_json_string'''

	# data = {
	# 	"name": "brit",
	# 	"age": "22"
	# }

	# data1 = json.dumps(data)

	# try:
	# 	validate_json_string(data1)
	# 	parsed = json.loads(data1)
	# 	# print(parsed)
	# 	return parsed['name']
	# except frappe.ValidationError:
	# 	frappe.throw("Invalid JSON!")

	'''random_string'''	

	# string = random_string(5)
	# return string

	'''unique'''
	
	# is_unique = unique([1,2,2,3])
	# is_unique = unique('ababcdc')
	# is_unique = unique(['apple', 'grapes', 'apple', 'banana'])
	# return is_unique

	'''get_abbr'''

	# abb = get_abbr('Gavin') 
	# return abb
	# abb1 = get_abbr('Coca Cola Company') 
	# return abb1
	# abb2 = get_abbr('Britvasan R', max_len=2) 
	# return abb2

	'''validate_url'''

	# url = validate_url('google')
	# print(url)

	# url1 = validate_url('https://google.com')
	# print(url1)
	# url2 = validate_url('https://google.com', throw=True)
	# print(url2)

	'''validate_email_address'''

	# email = validate_email_address('britvasan@tridotstech.com')
	# return email

	# email1 = validate_email_address('this is email address', throw=True)
	# return email1

	'''validate_phone_number'''
	# phone = validate_phone_number('753858375')
	# phone = validate_phone_number('number123', throw=True)
	# return phone


'''get_pdf'''
@frappe.whitelist(allow_guest=True)
def simple_pdf():
    html = """
    <html>
        <head>
            <style>
                h1 { color: #4CAF50; font-family: Arial, sans-serif; }
                p { font-size: 14px; font-family: Arial; }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple PDF generated from Frappe.</p>
        </body>
    </html>
    """

    frappe.local.response.filename = "hello_world.pdf"
    frappe.local.response.filecontent = get_pdf(html)
    frappe.local.response.type = "pdf"
