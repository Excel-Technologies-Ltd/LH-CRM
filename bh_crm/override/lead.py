import frappe
from erpnext.crm.doctype.lead.lead import Lead
from erpnext.selling.doctype.customer.customer import parse_full_name

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

        self.contact_doc = None

        if frappe.db.get_single_value("CRM Settings", "auto_creation_of_contact"):
            if self.source == "Existing Customer" and self.customer:
                contact = frappe.db.get_value(
                    "Dynamic Link",
                    {"link_doctype": "Customer", "parenttype": "Contact", "link_name": self.customer},
                    "parent",
                )
                if contact:
                    self.contact_doc = frappe.get_doc("Contact", contact)
                    return
            self.contact_doc = self.create_contact()

        # leads created by email inbox only have the full name set
        if self.lead_name and not any([self.first_name, self.middle_name, self.last_name]):
            self.first_name, self.middle_name, self.last_name = parse_full_name(self.lead_name)
