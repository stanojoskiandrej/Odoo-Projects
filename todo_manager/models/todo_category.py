from odoo import models, fields

class ToDoCategory(models.Model):
    _name = "todo.category"
    _description = "To-Do Category"

    name = fields.Char(string="Category Name", required=True)
    task_ids = fields.One2many("todo.task", "category_id", string="Tasks")
