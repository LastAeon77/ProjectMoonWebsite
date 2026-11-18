from django import forms


# Django 4.2+ rejects ClearableFileInput(attrs={"multiple": True}); this is the
# replacement recommended in the Django docs for uploading several files at once.
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return [single_file_clean(data, initial)]


class JSONUploadForm(forms.Form):
    files = MultipleFileField()
