from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    repassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = []

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        repassword = self.cleaned_data.get("repassword")
        if password and repassword and password != repassword:
            raise forms.ValidationError("密码不匹配")
        return repassword

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = ("username", "user_id", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (None, {"fields": ("is_admin",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password", "repassword", "is_admin"),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = ()


admin.site.unregister(Group)
