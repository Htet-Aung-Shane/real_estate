{
    'name' : 'Theme Customization',
    'description' : 'Customizing Real Estate Theme For Developed By MT Tech',
    'depends' : ['base','contacts'],
    'category': 'Customization',
    'author': 'Htet Aung Shane',
    'installable': True,
    'auto_install': False,
    'application': True,
    # "data":[
    #     'views/estate_footer.xml',
    # ],
    'assets':{
        'web.assets_frontend': [
            "/customization/static/src/scss/custom.scss",
        ]
    }
}