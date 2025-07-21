app_name = "learning_frappe"
app_title = "Learning Frappe"
app_publisher = "Brit"
app_description = "Learning Frappe"
app_email = "britvasan@tridotstech.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "learning_frappe",
# 		"logo": "/assets/learning_frappe/logo.png",
# 		"title": "Learning Frappe",
# 		"route": "/learning_frappe",
# 		"has_permission": "learning_frappe.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/learning_frappe/css/learning_frappe.css"
# app_include_js = "/assets/learning_frappe/js/learning_frappe.js"

# include js, css files in header of web template
# web_include_css = "/assets/learning_frappe/css/learning_frappe.css"
# web_include_js = "/assets/learning_frappe/js/learning_frappe.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "learning_frappe/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "learning_frappe/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "learning_frappe.utils.jinja_methods",
# 	"filters": "learning_frappe.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "learning_frappe.install.before_install"
# after_install = "learning_frappe.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "learning_frappe.uninstall.before_uninstall"
# after_uninstall = "learning_frappe.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "learning_frappe.utils.before_app_install"
# after_app_install = "learning_frappe.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "learning_frappe.utils.before_app_uninstall"
# after_app_uninstall = "learning_frappe.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "learning_frappe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"learning_frappe.tasks.all"
# 	],
# 	"daily": [
# 		"learning_frappe.tasks.daily"
# 	],
# 	"hourly": [
# 		"learning_frappe.tasks.hourly"
# 	],
# 	"weekly": [
# 		"learning_frappe.tasks.weekly"
# 	],
# 	"monthly": [
# 		"learning_frappe.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "learning_frappe.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "learning_frappe.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "learning_frappe.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["learning_frappe.utils.before_request"]
# after_request = ["learning_frappe.utils.after_request"]

# Job Events
# ----------
# before_job = ["learning_frappe.utils.before_job"]
# after_job = ["learning_frappe.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"learning_frappe.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# doctype_js = {
#     "Ticket Booking": "public/js/ticket_booking_list.js"
# }

# doc_events = {
#     "Task": {
#         "after_insert": "learning_frappe.learning_frappe.realtime.notify_task",
#         "on_update": "learning_frappe.learning_frappe.realtime.notify_task",
#     },
#     "Task Comment": {
#         "after_insert": "learning_frappe.learning_frappe.realtime.notify_comment",
#     },
# }


# app_include_js = "/assets/learning_frappe/js/alert.js"


# scheduler_events = {
#     "daily": [
#         "learning_frappe.learning_frappe.api.scheduler_test.daily_task"
#     ],
#     "hourly": [
#         "learning_frappe.learning_frappe.api.scheduler_test.hourly_task"
#     ]
# }

# scheduler_events = {
#     "cron": {
#         "*/1 * * * *": [
#             "learning_frappe.api.scheduler_test.daily_task"
#         ]
#     }
# }

# scheduler_events = {
#     "cron": {
#         "*/1 * * * *": [
#             "learning_frappe.api.scheduler_test.push_sales_data"
#         ]
#     }
# }

# scheduler_events = {
#     "cron": {
#         "*/1 * * * *": [
#             "learning_frappe.api.scheduler_test.daily_task"
#         ]
#     }
# }


# scheduler_events = {
    
#     "all":[
#         "learning_frappe.api.scheduler_test.send_test_record"
#     ]
# }

# scheduler_events = {
#     "cron": {
#         "*/1 * * * *": [
#             "learning_frappe.learning_frappe.api.push_leave_update"
#         ]
#     }
# }



doctype_list_js = {
    "Database API": "public/js/movie.js",
    'Utility Function': 'public/js/utility.js'
}

permission_query_conditions = {
    "Personal Notes": "learning_frappe.permissions.personal_note_query"
}

has_permission = {
    "Events": "learning_frappe.permissions.event_has_permission"
}

override_doctype_class = {
    "Event": "learning_frappe.overrides.event.CustomEvent"
}

doc_events = {
    "Events": {
        "before_insert": "learning_frappe.crud_events.check_private_event_permissions"
    }
}

override_whitelisted_methods = {
    "frappe.client.get_count": "learning_frappe.whitelisted.custom_get_count"
}

ignore_links_on_delete = ["Sub Record"]

# additional_timeline_content = {
#     "Events": ["learning_frappe.timeline.event_timeline.event_timeline"]
# }

before_migrate = "learning_frappe.migrate.before_migrate"
after_migrate = "learning_frappe.migrate.after_migrate"

jinja = {
    "methods": [
        "learning_frappe.jinja.methods",
        "learning_frappe.utils.get_fullname"
    ],
    "filters": [
        "learning_frappe.jinja.filters",
        "learning_frappe.utils.format_currency"
    ]
}
