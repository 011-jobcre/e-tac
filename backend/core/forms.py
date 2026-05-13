from django import forms
from django.urls import reverse_lazy

# from django.utils.translation import gettext_lazy as _
from .models import Daibunrui, Chubunrui, Shobunrui


class InquiryForm(forms.Form):
    company_name = forms.CharField(required=True, max_length=255)
    daibunrui = forms.ModelChoiceField(
        queryset=Daibunrui.objects.all(),
        required=True,
        # empty_label=_("大分類を選択してください"),
        widget=forms.Select(
            attrs={
                "class": "select outline-none w-full",
                "hx-get": reverse_lazy("chubunrui-options"),  # HTMX endpoint
                "hx-target": "#chubunrui-wrapper",
                "hx-swap": "innerHTML",
                "hx-trigger": "change",
                "hx-indicator": "#chu-loading",
                "x-model": "daiSelected",
                "@change": "handleDaiChange($event)",
                ":class": "fieldErrorClass('daiSelected')",
            }
        ),
    )

    # 中・小 will be rendered dynamically via HTMX
    chubunrui = forms.ModelChoiceField(
        queryset=Chubunrui.objects.none(),  # Empty initially
        required=True,
        # empty_label=_("中分類を選択してください"),
        widget=forms.Select(
            attrs={
                "class": "select outline-none w-full",
                "disabled": "disabled",  # Disabled cho đến khi chọn 大
            }
        ),
    )

    shobunrui = forms.ModelChoiceField(
        queryset=Shobunrui.objects.none(),
        required=True,
        # empty_label="_("小分類を選択してください")",
        widget=forms.Select(
            attrs={
                "class": "select outline-none w-full",
                "disabled": "disabled",
            }
        ),
    )
    position = forms.CharField(required=True, max_length=255)
    contact_name = forms.CharField(required=True, max_length=255)
    inquiry_content = forms.CharField(required=True)
    privacy_policy = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        data = self.data if self.is_bound else None
        dai_code = data.get("daibunrui") if data else None
        chu_code = data.get("chubunrui") if data else None

        if dai_code:
            self.fields["chubunrui"].queryset = Chubunrui.objects.filter(
                daibunrui_id=dai_code
            )

        if chu_code:
            self.fields["shobunrui"].queryset = Shobunrui.objects.filter(
                chubunrui_id=chu_code
            )
