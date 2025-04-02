{
    'name': "School Management",
    'version': '18.0.1.0.0',
    'author': "Kushal Shah",
    'category': 'Custom',
    'description': """
        Custom module for school management
    """,

    'data': [
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'views/school_student_view.xml',
        'views/school_student_sports_view.xml',
        'views/school_class_view.xml',
        'views/school_subjects_view.xml',
        'views/school_teacher_view.xml',
        'views/school_student_reports_view.xml',
        'views/snippets/s_basic_snippet.xml',
        'wizard/school_student_dob_wizard_view.xml',
        'report/student_report.xml',
        'report/ir_actions_report.xml',
        'data/ir_action_data.xml'

    ],

    'depends' : ['base','mail','web'],

    'installable':True,
    'application':True,
}