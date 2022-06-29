from django.urls import path

from . import views

app_name = "board"
urlpatterns = [
    path("", views.index, name="index"),
    path("board/<board>", views.board, name="board"),
    path("board/<board>/add_post", views.posting_page, name="posting_page"),
    path(
        "board/<board>/<int:post_id>",
        views.replies_page,
        name="show_replies",
    ),
    path(
        "board/<board>/<int:post_id>/<int:reply_id>",
        views.replies_page,
        name="show_replies_selected",
    ),
    path(
        "board/<board>/<int:post_id>/success",
        views.posting_success,
        name="reply_success",
    ),
    path("board/<board>/<int:post_id>/reply", views.long_reply_page, name="long_reply"),
    path(
        "board/<board>/<int:post_id>/reply/success",
        views.posting_success,
        name="long_reply_success",
    ),
    path("board/<board>/add_post/sucess", views.posting_success, name="post_success"),
    path("board/<board>/<tag>", views.tags_view, name="tag_search"),
]
