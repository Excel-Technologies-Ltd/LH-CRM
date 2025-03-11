import frappe
from erpnext.crm.doctype.lead.lead import Lead
from erpnext.selling.doctype.customer.customer import parse_full_name

class NewLead(Lead):
    # Ensure it correctly extends Document
    def before_save(self):
        self.validate_passport_number()


    def validate_passport_number(self):
        passport_number = self.passport_number
        creation_date = self.creation
        check_existing_passport = None
        if passport_number:
            previous_doc = frappe.db.get_value("Lead", {"passport_number": passport_number},["modified","name"])
            if previous_doc and len(previous_doc) > 0 and (previous_doc[1] != self.name):
                check_existing_passport = previous_doc[0]

        if check_existing_passport and passport_number:
            last_creation_date = frappe.utils.get_datetime(check_existing_passport)
            current_creation_date = frappe.utils.get_datetime(creation_date)

            # Check if the last lead was created within 120 days
            if (current_creation_date - last_creation_date).days <= 120:
                frappe.throw("A lead with this passport was already created in the last 120 days.")
