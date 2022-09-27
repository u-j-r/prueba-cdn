{
    'name': 'Test theme',
    'description': 'A cool description for your theme.',
    'version': '1.0',
    'author': 'Your name',
    'category': 'Theme/Creative',

    'depends': ['website'],
    'data': [
         'views/assets.xml',
    ],
    'assets': {
         'web.assets_frontend': [          
         'Theme_Test/static/src/scss/style.scss'
        ]
    }
}