from odoo import models, fields

class ToDoPriority(models.Model):
    _name = "todo.priority"
    _description = "To-Do Task Priority"

    name = fields.Char(string="Priority Level", required=True)
    level = fields.Integer(string="Priority Value")
