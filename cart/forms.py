from django import forms

ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class AddProductCartForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=ITEM_QUANTITY_CHOICES,
        coerce=int
    )

    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )  