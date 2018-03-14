from django       import forms
from .models      import Posts
from django.forms import PasswordInput





class LoginSenha(forms.ModelForm):

    class Meta:
        model = Posts

        senha  = forms.CharField(label=("Senha"), widget=forms.PasswordInput)

        fields =    [   'login',
                        'senha',
                    ]

        widgets = { 'senha':  PasswordInput() }


class NewPostForm2(forms.ModelForm):

    class Meta:
        model = Posts

        senha2 = forms.CharField(label=("Redigite a senha"), widget=forms.PasswordInput)
        senha  = forms.CharField(label=("Senha"),            widget=forms.PasswordInput)

        fields =    [
                        'nome',
                        'email',
                        'celular',
                        'areadeatuacao',
                        'perfil',
                        'historicoprofissional',
                        'formacao',
                        'conhecimentos',
                        'cursos',
                        'idiomas',
                        'dadospessoais'
        ]

    areadeatuacao         = forms.CharField(required=False)
    perfil                = forms.CharField(required=False)
    historicoprofissional = forms.CharField(required=False)
    formacao              = forms.CharField(required=False)
    conhecimentos         = forms.CharField(required=False)
    cursos                = forms.CharField(required=False)
    idiomas               = forms.CharField(required=False)
    dadospessoais         = forms.CharField(required=False)
    

