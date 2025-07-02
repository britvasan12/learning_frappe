// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt

frappe.query_reports["Course Report"] = {
	"filters": [
		{
			"fieldname":"course",
			"label":__("Course"),
			"fieldtype":"Link",
			"options":"Course"
		},
		{
			"fieldname":"start_date",
			"label":__("Start Date"),
			"fieldtype":"Date"
		},
		{
			"fieldname":"end_date",
			"label":__("End Date"),
			"fieldtype":"Date"
		}
	]
};
