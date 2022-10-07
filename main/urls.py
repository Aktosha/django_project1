from django.contrib import admin
from django.urls import path, include
from accounts.views import (login_view,
                            logout_view)

urlpatterns = [
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),

]
