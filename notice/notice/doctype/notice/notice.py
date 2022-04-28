# Copyright (c) 2022, SDC and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import *
from frappe.model.naming import make_autoname

class Notice(WebsiteGenerator):
	def before_save(self):
		self.date = today()
 
		# variables
		
		department = self.department
		requiredRole = "HOD" #Role

		#departments
		cse = "Computer Science & Engineering - SD" 
		
		self.hod = frappe.db.sql(f""" select full_name 
			from `tabUser` 
			where `email` IN (select user 
			from `tabUser Permission` 
			where `for_value`="{department}" AND `user` IN (select parent 
			from `tabHas Role` 
			where `role`="{requiredRole}" )) """)
		
		if self.department == cse:
			self.name = make_autoname('NOTICE-'+'CSE'+'/'+'.YYYY.'+'/'+'.#####')
		else:
			self.name = make_autoname('NOTICE-'+'CIVIL'+'/'+'.YYYY.'+'/'+'.#####')

	def before_submit(self):
		self.date = today()
