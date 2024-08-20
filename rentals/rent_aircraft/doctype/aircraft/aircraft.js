// Copyright (c) 2024, MK and contributors
// For license information, please see license.txt

frappe.ui.form.on("Aircraft", {
	refresh(frm) {

	},

    get_summary(frm) {
        frm.get_field("summary").$wrapper.append("<h2>Here is your summary</h2>");
    }

});
