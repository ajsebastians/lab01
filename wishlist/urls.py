from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_ajax
from wishlist.views import create_ajax
from wishlist.views import show_xml
from wishlist.views import show_xml_by_id  
from wishlist.views import show_json 
from wishlist.views import show_json_by_id 
from wishlist.views import register #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>', show_xml_by_id, name="show_xml_by_id"),
    path('json/', show_json, name='show_json'), 
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/',show_wishlist_ajax,name='show_wishlist_ajax'),
    path('ajax/submit/', create_ajax, name='create_ajax'),
]