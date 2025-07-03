LICENSES = {
    'by': {
        'name': 'Attribution',
        'abbreviation': 'CC BY',
        'description': 'This license lets others distribute, remix, adapt, and build upon your work, even commercially, as long as they credit you for the original creation.',
        'allows_commercial': True,
        'allows_derivatives': True,
        'requires_sharealike': False,
        'requires_attribution': True,
        'icon': 'by.svg',
        'legal_code': 'https://creativecommons.org/licenses/by/4.0/legalcode'
    },
    'by-sa': {
        'name': 'Attribution-ShareAlike',
        'abbreviation': 'CC BY-SA',
        'description': 'This license lets others remix, adapt, and build upon your work even for commercial purposes, as long as they credit you and license their new creations under the identical terms.',
        'allows_commercial': True,
        'allows_derivatives': True,
        'requires_sharealike': True,
        'requires_attribution': True,
        'icon': 'by-sa.svg',
        'legal_code': 'https://creativecommons.org/licenses/by-sa/4.0/legalcode'
    },
    # Add other licenses (by-nc, by-nd, by-nc-sa, by-nc-nd)
}

def get_license(allows_commercial, allows_derivatives, sharealike=False):
    if allows_commercial:
        if allows_derivatives:
            return LICENSES['by-sa'] if sharealike else LICENSES['by']
        else:
            return LICENSES['by-nd']
    else:
        if allows_derivatives:
            return LICENSES['by-nc-sa'] if sharealike else LICENSES['by-nc']
        else:
            return LICENSES['by-nc-nd']