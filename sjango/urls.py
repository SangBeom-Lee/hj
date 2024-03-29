## 2022-05-31 서브페이지를 위한 경로 추가 (Index)
from django.contrib import admin
from django.urls import path, include
from layout import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.MainView.as_view()),
    path('intro/', views.IntroView.as_view()),
    path('vending/', views.VendingView.as_view()),
    path('laser/', views.LaserView.as_view()),
    path('bend/', views.BendView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('board/', include('board.urls')),

    ## 견적사이트 미리보기
    path('estimate/', views.EstimateView.as_view())
]

# Summernote 설정
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [path('summernote/', include('django_summernote.urls'))]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)