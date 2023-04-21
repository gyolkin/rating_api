from rest_framework.permissions import SAFE_METHODS, BasePermission


class UsersPermission(BasePermission):
    """Работать с пользователями может только администратор."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin
        )


class CommentReviewsPermissions(BasePermission):
    """Комментарии и отзывы читать могут все,
    а редактировать и удалять - админ, модератор и автор."""
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if (
            request.user.is_authenticated
            and (
                request.user.is_admin
                or request.user.is_moderator
            )
        ):
            return True
        return (
            request.method in ('PUT', 'PATCH', 'DELETE')
            and obj.author == request.user
        )


class AdminOrReadOnly(BasePermission):
    """Изменять может админ, остальные только читать
    (для работы с категориями и жанрами)."""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and request.user.is_admin
        )
