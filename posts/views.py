from __future__ import unicode_literals

import sys

from django.shortcuts         import render
from django.http              import HttpResponse
from django.utils             import timezone
from django.http              import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template          import RequestContext
from django.core.exceptions   import ObjectDoesNotExist
from .models                  import Posts
from .forms                   import LoginSenha, NewPostForm2


print("views.py begin: ")

#================================================================================
#================================================================================
def index(request):
    print("views.py/index begin: ")
    
    request.session['editarmm'] = 'no'

    try:
          post = Posts.objects.get(login="marcosmunis")
    except ObjectDoesNotExist:
          print("views.py/index id=1 nao existe")
          p = Posts(
                        title = "",
                        body  = "",
                        login                 = "marcosmunis",
                        senha                 = "marc0s777",
                        senha2                = "",
                        visivel               = "S",
                        nome                  = "Fulano de Tal",
                        email                 = "fulanodetal@gmail.com",
                        celular               = "21999999999",
                        cidade                = "",
                        estado                = "",
                        objetivo              = "",
                        descricao             = "",
                        nome2                 = "",
                        areadeatuacao         = "",
                        perfil                = "",
                        historicoprofissional = "",
                        formacao              = "",
                        conhecimentos         = "",
                        cursos                = "",
                        idiomas               = "",
                        dadospessoais         = ""
                  )
          p.save(force_insert=True)
    
    post = Posts.objects.get(login="marcosmunis")    
    
    context = { 'post': post }

    print("views.py/index end: ")
    return render( request, 'posts/index.html', context )
#================================================================================
#================================================================================
def editarcv(request):
    print("views.py editarcv: BEGIN")

    request.session['editarmm'] = 'no'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views.py editarcv: POST")

        # create a form instance and populate it with data from the request:
        form = LoginSenha(request.POST)
        # check whether it's valid:

        ok = True

        if form.is_valid():
        
            post = form.save(commit=False)
            print( "views.py editarcv: Objeto post" )
            print( post.nome )
            print( post.login )
            print( post.senha )

            p2 = Posts.objects.get(login="marcosmunis")    
            print( "views.py editarcv: Objeto p2" )
            print( p2.nome )
            print( p2.login )
            print( p2.senha )
            
            if post.login == "":
                ok = False
            if post.senha == "":
                ok = False
            if post.login <> p2.login:
                ok = False
            if post.senha <> p2.senha:
                ok = False

        else:
            ok = False
            print("views.py editarcv: Formulario nao valido")


        if ok:
            print("views.py editarcv: ok")
            
            request.session['editarmm'] = 'yes'
            
            url = '../../posts/editarmm/'

            print("views.py editarcv: END ("+url+")")

            hrr = HttpResponseRedirect(url)
            return hrr

        else:
            print("views.py editarcv: END")
            return render(request, 'posts/editarcv.html', { 'form': form })

    # if a GET (or any other method) we'll create a blank form
    else:
        print("views.py editarcv: else.1")
        form = LoginSenha()
        context = { 'form': form }
        print("views.py editarcv: END")
        return render(request, 'posts/editarcv.html', context)
#================================================================================
#================================================================================
def editarmm(request):
    print("views.py editarmm: BEGIN")

    mensagem = False
    if request.session.has_key('editarmm'):
        mensagem = request.session['editarmm']
        if mensagem == 'no':
            request.session['editarmm'] = 'no'
            return HttpResponseRedirect("/")
  

    if request.method == 'POST':
        print("views.py editarmm: POST")

        post = Posts.objects.get(login="marcosmunis")

        form = NewPostForm2(request.POST, instance=post)

        if form.is_valid():
        
            ok = True

            form.save(commit=False)
            if ok:
                print("views.py editarmm: ok")
                print("views.py editarmm: END")
                form.save()

                return HttpResponseRedirect("/")
        
        else:
            print("views.py editarmm: formulario nao valido")
            
        print("views.py editarmm: END")
        
        return render(request, 'posts/editarmm.html', { 'form': form })

    else:
        print("views.py editarmm: GET")

        post = Posts.objects.get(login="marcosmunis")

        print("views.py editarmm: post.nome=["+ post.nome +"]")

        data = { 
                    'nome'                  :  post.nome,
                    'email'                 :  post.email,
                    'celular'               :  post.celular,
                    'cidade'                :  post.cidade,
                    'estado'                :  post.estado,
                    'objetivo'              :  post.objetivo,
                    'descricao'             :  post.descricao,
                    'areadeatuacao'         :  post.areadeatuacao,
                    'perfil'                :  post.perfil,
                    'historicoprofissional' :  post.historicoprofissional,
                    'formacao'              :  post.formacao,
                    'conhecimentos'         :  post.conhecimentos,
                    'cursos'                :  post.cursos,
                    'idiomas'               :  post.idiomas,
                    'dadospessoais'         :  post.dadospessoais,
        }

        form = NewPostForm2( data, initial=data )  

        context = { 'form': form }
        print("views.py editarmm: END")
        return render(request, 'posts/editarmm.html', context)
#================================================================================
#================================================================================



