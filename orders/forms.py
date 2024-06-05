import re

from django import forms


class CreateOrderForm(forms.Form):

    """
    This form is used to create an order.
    It includes the following fields: name, last_name, phone_number, requires_delivery,
     delivery_address, and payment_on_get.
    """

    name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(choices=[("0", 'False'), ("1", 'True')])
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(choices=[("0", 'False'), ("1", 'True')])

    def clean_phone_number(self):

        """
        This method is used to clean the phone_number field.
        It includes the following fields: data, pattern, and raise forms.ValidationError.
        :return: data
        """

        data = self.cleaned_data['phone_number']

        pattern = re.compile(r'^(\+?\d{1,3})?\d{10,14}$')
        if not pattern.match(data):
            raise forms.ValidationError('f"{number} is not a valid phone number"')

        return data




    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    #
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    #
    # phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    #
    # requires_delivery = forms.ChoiceField(widget=forms.RadioSelect(), choices=[(True, '1'), (False, '0')], initial=False)
    #
    # delivery_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'delivery_address',
    #                                                                 'rows': 2,  'placeholder': 'Delivery address'}),
    #                                    required=False)
    #
    # payment_on_get = forms.ChoiceField(widget=forms.RadioSelect(), choices=[(True, '1'), (False, '0')], initial=False)
