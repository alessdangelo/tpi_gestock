from . import views
# Import the path & include function from the django.urls module
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Define a list of URL patterns for the web application
urlpatterns = [
    # Map the URLs to it's view function and give it a name
    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('article', views.article, name='article'),
    path('borrow', views.borrow, name='borrow'),
    path('borrows', views.borrows, name='borrows'),
    path('products', views.products, name='products'),
    path('articles', views.articles, name='articles'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('editProduct', views.editProduct, name='editProduct'),
    path('deleteProduct', views.deleteProduct, name='deleteProduct'),
    path('addArticle', views.addArticle, name='addArticle'),
    path('editArticle', views.editArticle, name='editArticle'),
    path('deleteArticle', views.deleteArticle, name='deleteArticle'),
    path('addBorrow', views.addBorrow, name='addBorrow'),
    path('editBorrow', views.editBorrow, name='editBorrow'),
    path('deleteBorrow', views.deleteBorrow, name='deleteBorrow'),
    path('jsondata', views.jsondata, name='jsondata'),
    # Include the authentication URLs provided by Django and prefix them with /accounts/
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)