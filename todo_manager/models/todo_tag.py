from odoo import models, fields

class ToDoTag(models.Model):
    _name = "todo.tag"
    _description = "To-Do Task Tag"

    name = fields.Char(string="Tag Name", required=True)
    task_ids = fields.Many2many("todo.task", string="Tasks")
