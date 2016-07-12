from django import forms
from .models import ParaSet

class ParaSetForm(forms.ModelForm):
    class Meta:
        model=ParaSet
        
        fields=['control_fail_id','asset_id','control_name',
        'ctr_fail_desc','sensitive_data','asset_loc','solution_prov','pocs','auth_meth',
        'cri_met','wide_vul','comp_ctr','internet_exp']