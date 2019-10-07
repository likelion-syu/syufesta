from django.conf import settings

def global_settings(req):
    return {
        'ASSETS_VERSION' : '1.1.6'
     }
    