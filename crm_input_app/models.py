from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ParaSet(models.Model):
    """A set of parameters that users enters"""
    
    YES_NO_CHS = (
        ('1', 'Yes'),
        ('0', 'No'),
    )    
    
    ASSET_LOC_CHS = (
        ('1', 'National Data Center'),
        ('2', 'Regional'),
        ('3','Server Room'),
        ('4','Exposed'),
        ('5', 'Vendor Hosted'),
    )    
    
    SOLU_PROV_CHS=(
    ('1','Reputable Vendor'),
    ('2','Not Reputable Vendor'),
    ('3','Mature Internal Team (Certified)'),
    )
    
    
    AUTHEN_CHS=(
    ('1','Anonymous (n/a)'),
    ('2','Local'),
    ('3','Central'),    
    )
    
    KNOWN_VUL_CHS=(
    ('1', 'Unknown'),
    ('2','Yes but no published exploit'),
    ('3', 'Yes but vulnerability and exploit not automated'),
    ('4', 'Yes and automated vulnerability but not automated exploit'),
    ('5',  "Yes and both vulnerability and exploit are automated")  ,  

    )
  
    
    control_fail_id=models.CharField("Control Failure ID", max_length=15)
    asset_id=models.CharField("Asset ID", max_length=15)
    control_name=models.CharField("Control Name", max_length=100)
    ctr_fail_desc=models.CharField("Control Failure Description", max_length=600)
    
    sensitive_data= models.CharField("Sensitive Data", choices=YES_NO_CHS, max_length=1)
    asset_loc=models.CharField("Asset Location", choices=ASSET_LOC_CHS, max_length=1 )    
    solution_prov=models.CharField("Solution Provider",choices=SOLU_PROV_CHS, max_length=1)
    pocs= models.CharField("Point of Care System", choices=YES_NO_CHS,max_length=1)
    auth_meth=models.CharField("Authentication Method", choices=AUTHEN_CHS, max_length=1)    
    cri_met=models.CharField("All criteria  well maintained are met", choices=YES_NO_CHS,max_length=1)
    wide_vul=models.CharField("Widely known vulnerability", choices=YES_NO_CHS,max_length=1)
    comp_ctr=models.CharField(" There is a compensating control", choices=YES_NO_CHS,max_length=1)
    internet_exp=models.CharField("Internet Exposed or in DMZ", choices=YES_NO_CHS,max_length=1)
    owner=models.ForeignKey(User)
   
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.control_name

    def __iter__(self):
            
        for field in self._meta.get_fields():
           if field.name != "owner":


                value = getattr(self, field.name, None)

                if field.choices:
                    display=dict(field.choices)[value]
            
                else:
                    display=value

       
                yield ( field.verbose_name.title(), value, display)
        