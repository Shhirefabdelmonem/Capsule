from django.urls import path
from . import views 


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('index',views.index,name='index'),
    path('emptycart',views.emptycart,name='emptycart'),
    path('fullcart',views.fullcart,name='fullcart'),
    path('wish',views.wish,name='wish'),


]