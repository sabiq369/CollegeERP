{
    'name': 'College ERP',
    'depends': ['base_setup'],
    'sequence': 1,
    'application': True,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/demo_data.xml',
        'views/menu_actions.xml',
        'views/college_menus.xml',
        'views/students_tree_view.xml',
        'views/students_form_view.xml',
        'views/course_tree_view.xml',
        'views/course_form_view.xml',
        'views/admission_tree_view.xml',
        'views/admission_form_view.xml',
        'views/semester_tree_view.xml',
        'views/semester_form_view.xml',

    ]

}
