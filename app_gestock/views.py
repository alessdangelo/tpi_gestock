# Import the necessary modules and models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import t_borrow, t_article, t_categories, t_cupboard, t_products, t_room, t_types
from datetime import date, timedelta, datetime
from django.db.models.functions import Cast
from django.db.models import CharField
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *

# Views


def index(request):
    menuTypes = dynMenu()
    return render(request, 'index.html', context={'menuTypes': menuTypes, 'borTotal': getTotalUserBorrows(request)})

@login_required
def product(request):
    menuTypes = dynMenu()
    id = request.GET.get('id')
    product = t_products.objects.get(idProduct=id)
    return render(request, 'product.html', context={'menuTypes': menuTypes, 'product': product, 'borTotal': getTotalUserBorrows(request)})

@login_required
def article(request):
    menuTypes = dynMenu()
    id = request.GET.get('id')
    article = t_article.objects.get(idArticle=id)
    qr_content = f"ETML - Informatique - {article.artName} - {article.fkProduct.proName} - {article.artNote} - {article.fkRoom} / {article.fkCupboard}"
    return render(request, 'article.html', context={'menuTypes': menuTypes, 'article': article, 'borTotal': getTotalUserBorrows(request), 'qr_content': qr_content})

@login_required
def borrow(request):
    menuTypes = dynMenu()
    id = request.GET.get('id')
    borrow = t_borrow.objects.get(idBorrow=id)
    return render(request, 'borrow.html', context={'menuTypes': menuTypes, 'borrow': borrow, 'borTotal': getTotalUserBorrows(request)})

@login_required
def borrows(request):
    menuTypes = dynMenu()
    return render(request, 'borrows.html', context={'menuTypes': menuTypes, 'borTotal': getTotalUserBorrows(request)})

@login_required
def products(request):
    menuTypes = dynMenu()
    return render(request, 'products.html', context={'menuTypes': menuTypes, 'borTotal': getTotalUserBorrows(request)})

@login_required
def articles(request):
    menuTypes = dynMenu()
    return render(request, 'articles.html', context={'menuTypes': menuTypes, 'borTotal': getTotalUserBorrows(request)})


@login_required
def addProduct(request):
    if request.method == 'POST':
        form = addProductForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            id = t_products.objects.latest('idProduct').idProduct
            # Redirect to the product page
            return HttpResponseRedirect(f'/product?id={id}')
    else:
        form = addProductForm()
    return render(request, 'addProduct.html', {'form': form, 'borTotal': getTotalUserBorrows(request)})

@login_required
def editProduct(request):
    id = request.GET.get('id')
    product = t_products.objects.get(idProduct=id)
    
    if request.method == 'POST':
        form = addProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            # Redirect to success page or display a success message
            return HttpResponseRedirect('/product?id='+id+'')
    else:
        form = addProductForm(instance=product)
    
    return render(request, 'editProduct.html', {'form': form, 'borTotal': getTotalUserBorrows(request)})

@login_required
def deleteProduct(request):
    id = request.GET.get('id')
    # product = t_products.objects.get(idProduct=id)
    product = get_object_or_404(t_products, idProduct=id)
    
    product.delete()
    return HttpResponseRedirect('/')

@login_required
def addArticle(request):
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            id = t_article.objects.latest('idArticle').idArticle
            # Redirect to the product page
            return HttpResponseRedirect(f'article?id={id}')
    else:
        form = articleForm()
    return render(request, 'addArticle.html', {'form': form, 'borTotal': getTotalUserBorrows(request)})

@login_required
def editArticle(request):
    id = request.GET.get('id')
    article = t_article.objects.get(idArticle=id)
    
    if request.method == 'POST':
        form = articleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # Redirect to success page or display a success message
            return HttpResponseRedirect('/article?id='+id+'')
    else:
        form = articleForm(instance=article)
    
    return render(request, 'editArticle.html', {'form': form})

@login_required
def deleteArticle(request):
    id = request.GET.get('id')
    article = get_object_or_404(t_article, idArticle=id)
    
    article.delete()
    return HttpResponseRedirect('/')

@login_required
def addBorrow(request):
    menuTypes = dynMenu()
    article_id = request.GET.get('id')
    article = get_object_or_404(t_article, idArticle=article_id)

    if article.t_borrow_set.exists():
        messages.error(request, 'Cet article est déjà emprunté.')
        return redirect('/')

    if request.method == 'POST':
        form = borrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.fkArticle = article
            borrow.save()
            messages.success(request, 'L\'emprunt a été ajouté avec succès.')
            return redirect('/')
    else:
        form = borrowForm()

    return render(request, 'addBorrow.html', {'form': form, 'menuTypes': menuTypes, 'borTotal': getTotalUserBorrows(request)})

@login_required
def editBorrow(request):
    menuTypes = dynMenu()
    id = request.GET.get('id')
    borrow = t_borrow.objects.get(idBorrow=id)
    
    if request.method == 'POST':
        form = borrowForm(request.POST, instance=borrow)
        if form.is_valid():
            form.save()
            # Redirect to success page or display a success message
            return HttpResponseRedirect(f'/borrow?id={id}')
    else:
        form = borrowForm(instance=borrow)
    
    return render(request, 'editBorrow.html', {'form': form, 'menuTypes': menuTypes, 'borrow': borrow, 'borTotal': getTotalUserBorrows(request)})

@login_required
def deleteBorrow(request):
    id = request.GET.get('id')
    borrow = get_object_or_404(t_borrow, idBorrow=id)
    
    borrow.delete()
    return HttpResponseRedirect('/')

def dynMenu():
    return list(t_types.objects.all().values_list('typName', flat=True))

def getTotalUserBorrows(request):
    if request.user.is_authenticated:
        # Get the connected user
        connected_user = request.user
        # Query the Borrow model to get the number of borrows for the connected user
        num_borrows = t_borrow.objects.filter(borUser_id=connected_user).count()
        print(num_borrows)
        return num_borrows
    else: return 0

# Define the jsondata view function
def jsondata(request):
    # Get the 'table' parameter from the GET request
    table = request.GET.get('table')
    
    # If the table parameter is 't_borrow', retrieve data from the t_borrow table
    if table == 't_borrow':
        data = list(t_borrow.objects.select_related(
            'borUser',
            'fkArticle__fkProduct__fkType',
            'fkArticle__fkProduct__fkCategory',
            'fkArticle__fkCupboard__fkRoom'
        ).annotate(
            borDate_str=Cast('borDate', output_field=CharField()),
            borReturnDate_str=Cast('borReturnDate', output_field=CharField())
        ).values(
            'fkArticle__fkProduct__fkType__typName',
            'fkArticle__fkProduct__fkCategory__catName',
            'fkArticle__fkProduct__proName',
            'fkArticle__artName',
            'borLocation',
            'fkArticle__artNote',
            'borDate_str',
            'borReturnDate_str',
            'borUser__username',
        ))
    # If the table parameter is 't_article', retrieve data from the t_article table
    elif table == 't_article':
        data = list(t_article.objects.select_related(
            'fkProduct__fkType',
            'fkProduct__fkCategory',
            'fkCupboard__fkRoom'
        ).annotate(
            borDate_str=Cast('t_borrow__borDate', output_field=CharField()),
            borReturnDate_str=Cast('t_borrow__borReturnDate', output_field=CharField())
        ).values(
            'fkProduct__fkType__typName',
            'fkProduct__fkCategory__catName',
            'fkProduct__proName',
            'artName',
            't_borrow__borLocation',
            'artNote',
            'borDate_str',
            'borReturnDate_str',
            't_borrow__borUser__username',
            'idArticle',
        ))
    if table == 't_borrow':
        data = list(t_borrow.objects.select_related(
            'borUser',
            'fkArticle__fkProduct__fkType',
            'fkArticle__fkProduct__fkCategory',
            'fkArticle__fkCupboard__fkRoom'
        ).annotate(
            borDate_str=Cast('borDate', output_field=CharField()),
            borReturnDate_str=Cast('borReturnDate', output_field=CharField())
        ).values(
            'fkArticle__fkProduct__fkType__typName',
            'fkArticle__fkProduct__fkCategory__catName',
            'fkArticle__fkProduct__proName',
            'fkArticle__artName',
            'borLocation',
            'idBorrow',
            'fkArticle__artNote',
            'borDate_str',
            'borReturnDate_str',
            'borUser__username',
        ))
    elif table == 't_article':
        data = list(t_article.objects.select_related(
                'fkProduct__fkType',
                'fkProduct__fkCategory',
                'fkCupboard__fkRoom'
            ).annotate(
                borDate_str=Cast('t_borrow__borDate', output_field=CharField()),
                borReturnDate_str=Cast('t_borrow__borReturnDate', output_field=CharField())
            ).values(
                'fkProduct__fkType__typName',
                'fkProduct__fkCategory__catName',
                'fkProduct__proName',
                'artName',
                't_borrow__borLocation',
                'artNote',
                'borDate_str',
                'borReturnDate_str',
                't_borrow__borUser__username',
                'idArticle',
            ))
    elif table == 't_products':
        data = list(t_products.objects.select_related(
                'fkType',
                'fkCategory'
            ).values(
                'fkType__typName',
                'fkCategory__catName',
                'proName',
                'proNote',
                'idProduct',
            ))
    # If the table parameter is invalid, return a JSON response with an error message and a 400 status code
    else:
        return JsonResponse({'error': 'Invalid table'}, status=400)
    
    # Return a JSON response with the retrieved data
    return JsonResponse(data, safe=False)
