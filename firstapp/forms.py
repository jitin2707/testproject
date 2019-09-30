from django import forms
from firstapp.models import SiteUser,UserRole,NewSiteUser
class SiteUserForm(forms.ModelForm):
    class Meta():
        model=SiteUser
        exclude=["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "isActive"
                ]


class NewSiteUserForm(forms.ModelForm):
    class Meta():
        model=NewSiteUser
        exclude=["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "isActive",
                 "image",
                ]

class UserRoleForm(forms.ModelForm):
    class Meta():
        model=UserRole
        exclude=["roleId","roleName","isActive"]
