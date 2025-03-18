from odoo import models, fields


class ToDoTask(models.Model):
    _name = "todo.task"
    _description = "To-Do Task"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Task Name", required=True, tracking=True)
    description = fields.Text(string="Description")
    user_id = fields.Many2one("res.users", string="Assigned To", default=lambda self: self.env.user)
    category_id = fields.Many2one("todo.category", string="Category")
    priority_id = fields.Many2one("todo.priority", string="Priority")
    tag_ids = fields.Many2many("todo.tag", string="Tags")
    status = fields.Selection(
        [("draft", "Draft"), ("in_progress", "In Progress"), ("done", "Done")],
        default="draft",
        string="Status",
        tracking=True,
    )

    subtask_ids = fields.One2many("todo.subtask", "task_id", string="Subtasks")

    def mark_done(self):
        self.write({'status': 'done'})
        self.subtask_ids.write({'status': 'done'})
