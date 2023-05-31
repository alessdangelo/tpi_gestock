from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import t_borrow, t_article, t_categories, t_cupboard, t_products, t_room, t_types
from datetime import date, timedelta, datetime
from django.db.models.functions import Cast
from django.db.models import CharField
from django.contrib.auth.decorators import login_required

# Views

def index(request):
    menuTypes = dynMenu()
    # products = t_products.objects.all()
    # print(t_products.proName)
    # populate_database()
    return render(request, 'index.html', context={'menuTypes': menuTypes})

@login_required
def borrows(request):
    menuTypes = dynMenu()
    return render(request, 'borrows.html', context={'menuTypes': menuTypes})

def product(request):

    return render(request, 'product.html')

def dynMenu():
    return list(t_types.objects.all().values_list('typName', flat=True))

def jsondata(request):
    table = request.GET.get('table')
    
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
        ))
    else:
        # Handle invalid table parameter
        return JsonResponse({'error': 'Invalid table'}, status=400)
    
    return JsonResponse(data, safe=False)


def populate_database():
    # Get the user object
    # User = get_user_model()
    # user = User.objects.get(id=1)  # Assuming the user with ID 1 already exists

    # get a room
    room = t_room.objects.filter(rooName='A13').first()
    
    # get categories
    category1 = t_categories.objects.filter(catName='Câble').first()
    print(category1)
    # category2 = t_categories.objects.create(catName='Moniteurs')
    
    # # get a cupboard
    cupboard = t_cupboard.objects.filter(cupName='ARM-203').first()

    # get a type
    type1 = t_types.objects.filter(typName='Câble & Adaptateurs').first()

    #Create a product
    product = t_products.objects.create(
        proName='Digital HDMI Cable',
        proNote='HDMI 2.0 Cable',
        proImage='image_url',
        proBoughtPrice=999.95,
        proBoughtDate=date.today(),
        fkCategory=category1,
        fkType=type1
    )

     # Create an article
    article = t_article.objects.create(artName='INF-103', artNote='Bon état', fkCupboard=cupboard, fkRoom=room, fkProduct=product)
    article.save()
    product.fkArticle = article
    # print(article)
    # Create a borrow entry
    # borrow = t_borrow.objects.create(
    #     borLocation='Home',
    #     borDate=date.today(),
    #     borReturnDate=date.today() + timedelta(days=60),
    #     borNote='-',
    #     borUser=user,
    # )
