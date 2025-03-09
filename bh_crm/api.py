import frappe
from frappe.model.mapper import get_mapped_doc
@frappe.whitelist()
def make_referral(source_name, target_doc=None):
	def set_missing_values(source, target):
		if source.opportunity_from == "Lead":
			target.referral_from = source.party_name
	doclist = get_mapped_doc(
		"Opportunity",
		source_name,
		{
			"Opportunity": {
				"doctype": "Referral",
				"field_map": {
					"first_name": "first_name",
					"last_name": "last_name",
					"dob": "dob",
					"email": "email",
					"mobile": "mobile",
					"gender": "gender",
                    "passport": "passport",
                     
				}
			}
		},
		target_doc,
		set_missing_values,
	)

	return doclist


@frappe.whitelist()
def make_lh_appointment(source_name, target_doc=None):
	def set_missing_values(source, target):
		if source.opportunity_from == "Lead":
			target.referral_from = source.party_name
	doclist = get_mapped_doc(
		"Opportunity",
		source_name,
		{
			"Opportunity": {
				"doctype": "LH Appointment",
				"field_map": {
					"first_name": "first_name",
					"last_name": "last_name",
					"dob": "dob",
					"email": "email",
					"mobile": "mobile",
					"gender": "gender",
                     "passport": "passport",
                     
				}
			}
		},
		target_doc,
		set_missing_values,
	)

	return doclist


@frappe.whitelist()
def make_tele_consultation(source_name, target_doc=None):
	def set_missing_values(source, target):
		if source.opportunity_from == "Lead":
			target.referral_from = source.party_name
	doclist = get_mapped_doc(
		"Opportunity",
		source_name,
		{
			"Opportunity": {
				"doctype": "Tele Consultation",
				"field_map": {
					"first_name": "first_name",
					"last_name": "last_name",
					"dob": "dob",
					"email": "email",
					"mobile": "mobile",
					"gender": "gender",
                    "passport": "passport",
                     
				}
			}
		},
		target_doc,
		set_missing_values,
	)

	return doclist