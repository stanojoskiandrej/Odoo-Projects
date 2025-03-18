from odoo import models, fields

class ToDoSubTask(models.Model):
    _name = "todo.subtask"
    _description = "To-Do Subtask"

    name = fields.Char(string="Subtask Name", required=True)
    description = fields.Text(string="Description")
    task_id = fields.Many2one("todo.task", string="Main Task", required=True, ondelete="cascade")
    status = fields.Selection(
        [("draft", "Draft"), ("in_progress", "In Progress"), ("done", "Done")],
        default="draft",
        string="Status",
    )

    def mark_done(self):
        self.status = "done"
