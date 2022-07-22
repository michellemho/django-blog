from django.urls import path
from blogging.views import stub_view, BlogListView, BlogDetailView

urlpatterns = [
    # path('', stub_view, name="blog_index"),
    # path('posts/<int:post_id>/', stub_view, name="blog_detail"),
    path("", BlogListView.as_view(), name="blog_index"),
    # must use pk or error, AttributeError: Generic detail view BlogDetailView must be called with either an object pk or a slug in the URLconf.
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
