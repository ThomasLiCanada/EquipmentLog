from .models import Equipment
from django import forms


class InputEquipmentForm(forms.ModelForm):
    cal_due_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        help_text='e.g."25-12-2023", not accept "25-Dec-2023"',
        widget=forms.TextInput(attrs={'placeholder': 'dd-mm-yyyy'}),
    )
    CR_number = forms.CharField(
        max_length=50,
        help_text='e.g."34", not accept "CR-34"',
        widget=forms.TextInput(attrs={'placeholder': 'number only'}),
    )

    class Meta:
        model = Equipment
        fields = ['CR_number',
                  'cal_due_date',
                  'temperature',
                  'pin_size',
                  'part_number',
                  'lot_number',
                  'inspector'
                  ]


class InputEquipmentSuperuserForm(forms.ModelForm):
    cal_due_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        help_text='e.g."25-12-2023", not accept "25-Dec-2023"',
        widget=forms.TextInput(attrs={'placeholder': 'dd-mm-yyyy'}),
    )

    class Meta:
        model = Equipment
        fields = ['CR_number',
                  'cal_due_date',
                  'temperature',
                  'pin_size',
                  'part_number',
                  'lot_number',
                  'inspector',
                  'correction_remark'
                  ]


class EquipmentSearchForm(forms.Form):
    cr_number = forms.CharField(label='CR Number', max_length=50, required=False)
    start_date = forms.DateField(
        label='Start Date',
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),  # Add placeholder attribute
        help_text='e.g."2023-12-25", not accept "25-12-2023"',
    )
    end_date = forms.DateField(
        label='End Date',
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),  # Add placeholder attribute
        help_text='e.g."2023-12-25", not accept "25-12-2023"',
    )
