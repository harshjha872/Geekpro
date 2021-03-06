from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('blogs/',views.ArticleListView.as_view(),name='blogs'),
    path('blog/<int:pk>/',views.ArticleDetailView.as_view(),name='article_detail'),
    path('blog/new/',views.ArticleCreateView.as_view(),name='article_new'),
    path('blog/<int:pk>/edit/',views.ArticleUpdateView.as_view(),name='article_edit'),
    path('blog/<int:pk>/delete/',views.ArticleDeleteView.as_view(),name='article_delete'),
    path('author/<str:username>/',views.AuthorArticleListView.as_view(),name='author_posts'),
    path('about/',views.about,name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
