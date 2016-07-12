from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import ParaSet
from .forms import ParaSetForm


# Create your views here.
def index(request):
    """The home page for crm_input_app"""
    return render (request, 'crm_input_app/index.html')

@login_required
def parasList(request):
    """Show all parameters sets"""
    paraslist=ParaSet.objects.filter(owner=request.user).order_by('id')
    context={'paraslist':paraslist}
    return render(request, 'crm_input_app/parasList.html',context)

@login_required
def parasDetail(request, paras_id):
    """show parameter set details"""
    paras=ParaSet.objects.get(id=paras_id)
    #make sure the parameter set belongs to the current user.

    if paras.owner!= request.user:
        raise Http404
    context={'paras':paras}
    return render (request, 'crm_input_app/parasDetail.html',context)

@login_required
def new_paras(request):
    """Add new parameter set"""
    if request.method!='POST':
        #No data submitted;create a a blank form
        form=ParaSetForm()
    else:
        #POST data submitted; process data
        form=ParaSetForm(request.POST)
        if form.is_valid():
            new_data=form.save(commit=False)
            new_data.owner=request.user
            new_data.save()
            return HttpResponseRedirect(reverse ('crm_input_app:parasDetail',args=[new_data.id]))

    
    context= {'form':form}
    return render(request, 'crm_input_app/new_paras.html', context)    

@login_required
def getResult(request, paras_id):
    """show parameter set details"""
    paras=ParaSet.objects.get(id=paras_id)
    #make sure the parameter set belongs to the current user.

    if paras.owner!= request.user:
        raise Http404

    context={'paras':paras}
    return render (request, 'crm_input_app/result.html',context)

@login_required
def edit_paras(request, paras_id):
    """Edit an existing parameterset"""

    paras=ParaSet.objects.get(id=paras_id)

    #make sure the parameter set belongs to the current user.

    if paras.owner!= request.user:
        raise Http404

    if request.method!='POST':
        #initial request; pre-fill form with the current parameter set.
        form = ParaSetForm(instance=paras)
    else:
        #Post data submitted
        form=ParaSetForm(instance = paras, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse ('crm_input_app:parasDetail',args=[paras.id]))

    context={'paras':paras,'form':form}
    return render(request,'crm_input_app/edit_paras.html', context)