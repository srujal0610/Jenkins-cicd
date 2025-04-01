{
    'name': "Documents",
    'version': '18.0.1.0.0',
    'author': "Surekha Technologies Private Limited",
    'category': 'Custom',
    'license':'LGPL-3',
    'description': """
        This module extends the Odoo Website functionality by introducing a document snippet.
        It allows users to display a list of documents dynamically on the frontend of the website. 
        The documents are fetched from the Odoo backend and presented in an easy-to-view format using 
        Bootstrap cards with thumbnails, filenames, and file types. 

        Additionally, the module includes customizable snippet options for managing how documents 
        are displayed on the website, including adding custom categories and filtering the content.

        Features:
        - Display documents dynamically with metadata (e.g., filename, thumbnail, file type).
        - Simple and customizable document snippet for frontend use.
        - Option to include filtering and categorization features.
    """,

    'summary':"""
        This module provides a dynamic document snippet for Odoo websites, enabling users to display 
        documents along with their metadata in a structured and customizable layout.
    """,

    'data': [
        'views/snippets/s_doc_snippet.xml',
        'views/snippets/snippet_options.xml',
    ],

    'assets': {
            'web.assets_frontend':[
                '/st_doc_snippet/static/src/js/documents.js',
                '/st_doc_snippet/static/src/scss/styles.css'
            ],
            'web.assets_backend':[
                # Any backend-specific assets go here
            ],
            'website.assets_wysiwyg':[
                # Assets specific to the WYSIWYG editor (if applicable)
            ],
        },

    'depends' : ['base','documents','web_editor','website','web'],

    'installable': True,
    'application': True,
}
