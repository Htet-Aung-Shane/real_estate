{
    'name' : 'Theme Customization',
    'description' : 'Movies Website Hosted By MT Tech',
    'depends' : ['base','contacts'],
    'category': 'Customization',
    'author': 'Htet Aung Shane',
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets':{
        'web.assets_frontend': [
            "/customization/static/src/scss/custom.scss",
        ]
    }
}