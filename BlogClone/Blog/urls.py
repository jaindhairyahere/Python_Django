from django.urls import path
from .views import *

urlpatterns = [
	path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
	path('',PostListView.as_view(),name='post_list'),
	path('post/new',PostCreateView.as_view(),name='post_new'),
	path('post/<int:pk>/edit',PostUpdateView.as_view(),name='post_edit'),
	path('post/<int:pk>/detete',PostDeleteView.as_view(),name='post_remove'),
	path('drafts/',DraftListView.as_view(),name='post_draft_list'),
	path('about/',AboutView.as_view(),name='about'),
	path('post/<int:pk>/comment/',add_comment_to_post,name='add_comment_to_post'),
	path('comment/<int:pk>/approve/',comment_approve,name='comment_approve'),
	path('comment/<int:pk>/remove/',comment_remove,name='comment_remove'),
	path('post/<int:pk>/publish/',post_publish,name='post_publish'),
]
