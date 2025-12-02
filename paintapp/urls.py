from django.urls import path,include
from . import views
from django.conf import settings 
from  django.conf.urls.static import static

app_name='paintapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blogdetails/',views.blogdetails,name='blogdetails'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('elements/',views.elements,name='elements'),
    path('main/',views.main,name='main'),
    path('productdetails/',views.productdetails,name='productdetails'),
    path('shop/',views.shop,name='shop'),
    path('upload/',views.uploadimage,name='upload'),
    path('profile/',views.profile,name='profile'),
    path('cart/',views.cart,name='cart'),
    path('wishlist/',views.wishlist,name='wishlist'),

    path('uploadsave/',views.uploadsave,name='uploadsave'),
    path('imageview/ <int:im_id>',views.imageview,name='imageview'),
    path('viewprofile/ <int:user_id>',views.viewprofile,name='viewprofile'),
    path('mycart/<int:item_id> ',views.mycart,name='mycart'),
    path('mywishlist/<int:itm_id>',views.mywishlist,name='mywishlist'),
    path('buynow/<int:buy_id>',views.buynow,name='buynow'),
    path('updatequantity/<int:qu_id>/<str:operator>',views.updatequantity,name='updatequantity'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
