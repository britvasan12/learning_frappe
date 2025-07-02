# Copyright (c) 2025, Brit and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns, data = get_columns(),get_values(filters or {})
	return columns, data


def get_columns():
	columns = [
		{
			"fieldname":"course",
			"label":_("Course"),
			"fieldtype":"Link",
			"options":"Course"
		},
		{
			"fieldname":"start_date",
			"label":_("Start Date"),
			"fieldtype":"Date"
		},
		{
			"fieldname":"end_date",
			"label":_("End Date"),
			"fieldtype":"Date"
		},
		{
			"fieldname":"lecture_title",
			"label":_("Lecture Title"),
			"fieldtype":"Data"
		},
		{
			"fieldname":"lecture_date",
			"label":_("Lecture Date"),
			"fieldtype":"Date"
		},
		{
			"fieldname":"topic_name",
			"label":_("Topic Name"),
			"fieldtype":"Data"
		},
		{
			"fieldname":"duration_in_minutes",
			"label":_("Duration In Minutes"),
			"fieldtype":"Int"
		},
		{
			"fieldname":"rating",
			"label":_("Rating"),
			"fieldtype":"Rating"
		},
		{
			"fieldname":"feedback",
			"label":_("Feedback"),
			"fieldtype":"Small Text"
		}
	]

	return columns


def get_values(filters):
	condition = "1=1"

	if filters.get('course'):
		condition += f" AND C.name = '{filters.get('course')}'"

	if filters.get('start_date'):
		condition += f" AND C.start_date = '{filters.get('start_date')}'"

	if filters.get('end_date'):
		condition += f" AND C.end_date = '{filters.get('end_date')}'"

	if filters.get('lecture_title'):
		condition += f" AND L.lecture_title = '{filters.get('lecture_title')}'"

	if filters.get('lecture_date'):
		condition += f" AND L.lecture_date = '{filters.get('lecture_date')}'"

	if filters.get('topic_name'):
		condition += f" AND LT.topic_name = '{filters.get('topic_name')}'"
	
	if filters.get('duration_in_minutes'):
		condition += f" AND LT.duration_in_minutes = '{filters.get('duration_in_minutes')}'"
	
	if filters.get('rating'):
		condition += f" AND CF.rating = '{filters.get('rating')}'"
	
	if filters.get('feedback'):
		condition += f" AND CF.feedback = '{filters.get('feedback')}'"

	query = f"""
		SELECT
			C.name AS course,
			C.start_date,
			C.end_date,
			L.lecture_title,
			L.lecture_date,
			LT.topic_name,
			LT.duration_in_minutes,
			CF.rating,
			CF.feedback
		FROM
			`tabCourse` C
		LEFT JOIN
			`tabLecture` L
		ON
			L.course = C.name
		LEFT JOIN
			`tabLecture Topic` LT
		ON
			LT.parent = L.name
		LEFT JOIN
			`tabCourse Feedback` CF
		ON 	
			CF.course = C.name
		WHERE
			{condition}
	"""

	return frappe.db.sql(query, as_dict=True)