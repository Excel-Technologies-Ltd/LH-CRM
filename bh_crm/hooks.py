app_name = "bh_crm"
app_title = "Bh Crm"
app_publisher = "Sohanur Rahman"
app_description = "BH CRM"
app_email = "sohan.dev@excelbd.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bh_crm/css/bh_crm.css"
# app_include_js = "/assets/bh_crm/js/bh_crm.js"

# include js, css files in header of web template
# web_include_css = "/assets/bh_crm/css/bh_crm.css"
# web_include_js = "/assets/bh_crm/js/bh_crm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bh_crm/public/scss/website"

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
# 	"methods": "bh_crm.utils.jinja_methods",
# 	"filters": "bh_crm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bh_crm.install.before_install"
# after_install = "bh_crm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bh_crm.uninstall.before_uninstall"
# after_uninstall = "bh_crm.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bh_crm.utils.before_app_install"
# after_app_install = "bh_crm.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bh_crm.utils.before_app_uninstall"
# after_app_uninstall = "bh_crm.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bh_crm.notifications.get_notification_config"

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

override_doctype_class = {
	"Lead": "bh_crm.override.lead.NewLead",
	"Opportunity": "bh_crm.override.opportunity.NewOpportunity"
}

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



scheduler_events = {
   "cron": {
        "* * * * *": [
            "frappe.email.doctype.email_account.email_account.pull"
        ]
    },
}


# Testing
# -------

# before_tests = "bh_crm.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bh_crm.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bh_crm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bh_crm.utils.before_request"]
# after_request = ["bh_crm.utils.after_request"]

# Job Events
# ----------
# before_job = ["bh_crm.utils.before_job"]
# after_job = ["bh_crm.utils.after_job"]

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
# 	"bh_crm.auth.validate"
# ]


fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Opportunity-passport_number",
                    "Opportunity-gender",
                    "Opportunity-mobile_no",
                    "Opportunity-email_id",
                    "Opportunity-dob",
                    "Opportunity-last_name",
                    "Opportunity-first_name",
                    "Lead-passport_number",
                    "Lead-dob",
                    "Lead-hospital",
                    "Lead-purpose",
                    "Lead-sub_agent"
                ],
            ]
        ],
    },
    {
        "dt": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                    "Lead-middle_name-hidden",
                    "Lead-main-field_order",
                    "Opportunity-main-field_order",
                    "Lead-last_name-label",
                    "Lead-first_name-label",
                    "Referral-naming_series-options",
                    "Tele Consultation-naming_series-options",
                    "Lead-request_type-hidden"
                ],
            ]
        ],
    },
    {
        "dt": "Lead Source",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sub Agent"
                ],
            ]
        ],
    }
]