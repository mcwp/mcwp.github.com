from django.conf.urls.defaults import *

urlpatterns = patterns('guestbook.views',
    (r'^$', 'list_states'),
    (r'^sign$', 'create_greeting'),
    (r'^states$', 'list_states'),
    (r'^flowers$', 'list_flowers'),
    (r'^welcome$', 'welcome_view'),
    # (r'^bitty$', 'bitty_view'),                       
    # (r'^bitty/(\d{4})/(\d{2})/(\d+)/$', 'bitty_date'),                       
)
