import frappe
from erpnext.crm.doctype.lead.lead import Lead

class NewLead(Lead):  # Ensure it correctly extends Document
    def before_insert(self):

        passport_number = self.passport_number
        creation_date = self.creation

        # Fetch the latest lead creation date for the same passport within 90 days
        check_existing_passport = frappe.db.get_value(
            "Lead", 
            {"passport_number": passport_number}, 
            ["creation"]
        )
        print(check_existing_passport)

        if check_existing_passport:
            last_creation_date = frappe.utils.get_datetime(check_existing_passport)
            current_creation_date = frappe.utils.get_datetime(creation_date)

            # Check if the last lead was created within 90 days
            if (current_creation_date - last_creation_date).days <= 120:
                frappe.throw("A lead with this passport was already created in the last 120 days.")
