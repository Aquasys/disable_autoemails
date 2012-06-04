{
    "name": "Disable auto-emails",
    "version": "0.1",
    'category': 'Tools',
    "depends": ["sale"],
    "author": "Vincent Prouillet",
    "description": """
      Automatically disable the sending of emails when confirming sales orders and invoice
    """,
    'website': '',
    'init_xml': [],
    'update_xml': [
        'server_actions.xml'
        ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
