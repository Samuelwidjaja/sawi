from django.urls import include, path
from authentication.views import logout
from main.views import create_product_flutter, show_main, create_item, show_json, show_json_by_id, show_xml,show_xml_by_id, add_amount, reduce_amount, hapus, get_item_json
from main.views import add_item_ajax # type: ignore
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_amount/<int:id>', add_amount, name='add_amount'),
    path('reduce_amount/<int:id>', reduce_amount, name='reduce_amount'), # type: ignore
    path('hapus/<int:id>', hapus, name='hapus'),  # type: ignore
    path('get_item_json/', get_item_json, name='get_item_json'),
    path('add_item_ajax/', add_item_ajax, name='add_item_ajax'),
    path('auth/', include('authentication.urls')),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('logout/', logout, name='logout'),

]