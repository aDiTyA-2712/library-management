from django.urls import path,include
from .views import LibraryListCreateView,LibraryDetailView,borrow,book_return
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('library/',LibraryListCreateView.as_view(),name='create-list-lib'),
    path('library/<int:pk>',LibraryDetailView.as_view(),name='detail-lib'),
    path('book/<int:pk>',borrow,name='borrow'),
    path('return/<int:pk>',book_return,name='return'),
    path('auth/', include('rest_framework.urls')),  # Login/logout using Django’s session framework
    path('auth/token/', obtain_auth_token, name='api_token_auth'),  # Token-based authentication
    path('auth/social/', include('social_django.urls', namespace='social')),  # SSO authentication
]