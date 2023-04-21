from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewVeiwSet, SignUpView, TitleViewSet, TokenView,
                    UsersViewSet)

API_VERSION = 'v1'

router = SimpleRouter()
router.register('users', UsersViewSet, basename='users')
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews(?P<review_id>[\d]*)',
    ReviewVeiwSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/'
    r'comments(?P<comment_id>[\d]*)',
    CommentViewSet,
    basename='comments'
)
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path(f'{API_VERSION}/', include(router.urls)),
    path(f'{API_VERSION}/auth/signup/', SignUpView.as_view()),
    path(f'{API_VERSION}/auth/token/', TokenView.as_view())
]
