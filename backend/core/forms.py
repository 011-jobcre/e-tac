from django import forms
from django.urls import reverse_lazy
from .models import Daibunrui, Chubunrui, Shobunrui


class InquiryForm(forms.Form):
    daibunrui = forms.ModelChoiceField(
        queryset=Daibunrui.objects.all(),
        required=True,
        empty_label="大分類を選択してください",
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
        empty_label="中分類を選択してください",
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
        empty_label="小分類を選択してください",
        widget=forms.Select(
            attrs={
                "class": "select outline-none w-full",
                "disabled": "disabled",
            }
        ),
    )
