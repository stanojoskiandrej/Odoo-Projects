{
    "name": "To-Do List Manager",
    "version": "16.0.1.0.0",
    "summary": "Manage personal and team tasks",
    "author": "Andrej Stanojoski",
    "category": 'Accounting/Accounting',
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/todo_task_views.xml",
        "views/todo_category_views.xml",
        "views/todo_priority_views.xml",
        "views/todo_tag_views.xml",
        "views/menu_items.xml",
        "reports/todo_task_templates.xml",
        "reports/todo_task_reports.xml",
    ],
    "installable": True,
    "application": True,
}
