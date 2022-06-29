import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from . import get_url_title
from .forms import LongReply, PostingForm, QuickReply
from .models import Board, IndexPage, Post, Reply, Tag


# Create your views here.
def index(request):
    """index page"""
    default_index = IndexPage.objects.get(is_default=True)
    context = {
        "page_title": "Index",
        "page_welcome_note": default_index.welcome_title,
        "header_describtion": default_index.welcome_description,
        "tags": Board.objects.all(),
        "is_index": True,
    }
    return render(request, "board/index.html", context)


def board(request, board):
    """show board first page

    Args:
        board (string): board name

    Returns:
        html: board page with its posts
    """
    board_obj = Board.objects.get(name=board)

    context = {
        "page_title": board_obj.name,
        "page_welcome_note": f"Welcome To The {board_obj.name} Board!",
        "header_describtion": board_obj.desc,
        "tags": board_obj.tag_set.filter(show_in_header=True),
        "posts": board_obj.post_set.all(),
    }
    return render(request, "board/board.html", context=context)


def tags_view(request, board, tag):
    """show all posts containig this tag

    Args:

        board (string): board name
        tag (string): tag name

    Returns:
        html: all posts witch contain this tag
    """
    board_obj = Board.objects.get(name=board)
    context = {
        "page_title": board_obj.name,
        "page_welcome_note": f"Welcome To The {board_obj.name} Board!",
        "header_describtion": board_obj.desc,
        "tags": board_obj.tag_set.filter(show_in_header=True),
        "posts": Tag.objects.get(name=tag).post_set.all(),
        "message": f"Showing results with {tag} tag",
    }
    return render(request, "board/board.html", context=context)


def posting_page(request, board, **kwargs):
    """users can post here

    Args:
        board (string): board name where this posting is going to submit to
    """
    board_obj = Board.objects.get(name=board)
    contex = {
        "page_title": board_obj.name,
        "board_rules": board_obj.rules,
        "result": kwargs.get("results", False),
        "form": PostingForm(),
    }
    if request.method == "POST":
        form = PostingForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data["post_title"],
                date_posted=timezone.now(),
                url=form.cleaned_data["url"],
                url_title=get_url_title.get_title(form.cleaned_data["url"]),
                post_text=form.cleaned_data["post_message"],
                board=board_obj,
            )
            post.save()

            if len(form.cleaned_data["tags"]) != 0:
                input_tags = form.cleaned_data["tags"].split(",")
                for tag in input_tags:
                    tag = Tag.objects.get_or_create(
                        name=tag, board=board_obj, defaults={"board": board_obj}
                    )
                    post.tags.add(tag[0].id)
            return HttpResponseRedirect(
                reverse("board:show_replies", args=(board_obj.name, post.id))
            )
        else:
            contex["form"] = form
            return render(request, "board/posting_form.html", context=contex)

    else:
        # show posting form
        return render(request, "board/posting_form.html", context=contex)


def posting_success(request, board, post_id, **kwargs):
    """**not implemented yet
    page to show after a post request was successful
    """
    board_obj = Board.objects.get(name=board)
    context = {
        "content": "posting was succesfull",
        "page_title": board_obj.name,
        "post_id": post_id,
    }

    if kwargs.get("is_reply", False):
        context["message"] = "Posting reply was successful"
    else:
        context["message"] = "Posting was successful"
    return render(
        request,
        "board/show_replies.html",
        context=context,
    )


def replies_page(request, board, post_id, **kwargs):
    """show replies to a post, also allows a quick reply

    Args:
        board (string): board name
        post_id (int): post's id

    """
    board_obj = Board.objects.get(name=board)
    post_obj = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = QuickReply(request.POST)
        if form.is_valid():
            reply = Reply(
                date_posted=timezone.now(),
                post_text=form.cleaned_data["post_message"],
                post=post_obj,
            )
            reply.save()
            return HttpResponseRedirect(
                reverse(
                    "board:show_replies_selected",  # highlight the reply just posted
                    args=(board_obj.name, post_obj.id, reply.id),
                )
            )
    else:
        context = {
            "page_title": board_obj.name,
            "post": post_obj,
            "replies": post_obj.reply_set.all(),
            "form": QuickReply(),
            "board_rules": board_obj.rules,
        }
        reply_id = kwargs.get("reply_id", None)
        if reply_id:
            context["selected_reply"] = Reply.objects.get(pk=reply_id)
        return render(request, "board/replies_page.html", context=context)


def long_reply_page(request, board, post_id):
    """dedicated page for writing long replies

    Args:
        board (string): board name
        post_id (int): id of the post user is replying to
    """
    board_obj = Board.objects.get(name=board)
    post_obj = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = LongReply(request.POST)
        if form.is_valid():
            reply = Reply(
                date_posted=datetime.datetime.now(),
                post_text=form.cleaned_data["post_message"],
                post=post_obj,
            )
            reply.save()
            return HttpResponseRedirect(
                reverse(
                    "board:show_replies_selected",  # highlight the reply just posted
                    args=(board_obj.name, post_obj.id, reply.id),
                )
            )

    else:
        contex = {
            "page_title": board_obj.name,
            "board_rules": board_obj.rules,
            "form": LongReply(),
        }
        return render(request, "board/posting_form.html", context=contex)
