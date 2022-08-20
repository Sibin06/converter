from django import forms



class NumWordForm(forms.Form):
    number=forms.IntegerField(label="enter number",widget=forms.NumberInput(attrs={"class":"form-control"}))