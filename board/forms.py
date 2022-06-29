from django import forms
from django.core.validators import RegexValidator


class PostingForm(forms.Form):
    post_title = forms.CharField(label="Post Title:", max_length=80)
    url = forms.URLField(label="URL:", max_length=100)
    post_message = forms.CharField(
        widget=forms.Textarea(attrs={"name": "body", "rows": 3, "cols": 5}),
        max_length=600,
    )
    tags = forms.CharField(
        label="Tags: (Seperate tags with ',' Like: tag1,tag2)(Maximum 4 tags)",
        max_length=100,
        validators=[
            RegexValidator(
                "^[0-9a-zA-Z]+(,[0-9a-zA-Z]+)*$",
                message="Tags can only be a combination of Alphabets, Numbers & Underscore",
            )
        ],
        required=False,
    )

    def clean(self):
        if len(self.cleaned_data["tags"]) != 0:
            if not self.cleaned_data["tags"].islower():
                raise forms.ValidationError("Tags should be in lowercase")
            if len(self.cleaned_data["tags"].split(",")) > 4:
                raise forms.ValidationError(
                    "Only 4 tags alowed (Make sure you have at most 3 commas in input)"
                )


class QuickReply(forms.Form):
    """Creates an small textinput for writing short replies"""

    post_message = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Write a quick reply"}),
        min_length=1,
        max_length=600,
        label=False,
    )


class LongReply(forms.Form):
    """creates a large textbox for larger replies"""

    post_message = forms.CharField(
        widget=forms.Textarea(),
        min_length=1,
        max_length=600,
        label="Reply message:",
    )
