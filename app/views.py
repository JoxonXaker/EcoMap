from django.shortcuts import render
from django.contrib.auth.views import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import OrganizationModel
from .helper import STATUS, TYPES

@login_required
def home_page(request):
    return render(
        request=request,
        template_name='home.html',
        context={
        }
    )


@csrf_exempt
@login_required
def post_data(request):
    if request.POST:
        district = request.POST['district']
        organization = OrganizationModel.objects.filter(district=district)
        arr = []
        for organ in organization:
            arr.append({'name': str(organ.name), 'id': str(organ.id)})

        return JsonResponse(
            data={
                "result": arr,
                "status": 200
            },
            status=200,
        )

    organ_id = request.GET['organ']
    if organ_id.isdigit():
        organ = OrganizationModel.objects.get(id=int(organ_id))
        trees = organ.OrganizationTree.all()
        persons = organ.OrganizationPerson.all()

        persons_list = [{
            'name': person.full_name,
            'position': person.position,
            'phone': person.phone,
            'img': f"""<img src="{person.icon.url}" style="position: relative; 
                        margin:0 0 0 20px; width: 50px; border-radius: 13px;"> """
        } for person in persons]

        organization = [{
            'type': 'organization',
            'properties': {
                'id': organ.id,
                'icon': organ.icon.url,
                'name': organ.name,
                'email': organ.email,
                'phone': organ.phone,
                'area': organ.land_area,
                'count': organ.tree_count,
                'persons': persons_list,
                'img': [img.photo.url for img in organ.OrganizationPhotos.all()]
            },
            'geometry': {
                'type': organ.category,
                'coordinates': str(organ.location).split(', '),
            }
        }]
        tree = [{
            'type': 'tree',
            'properties': {
                'id': tree.id,
                'name': tree.name,
                'type': 'Archa',
                'tall': tree.tall,
                'status': 'yaxshi',
                'irrigation': 'o`rtacha',
                'create_date': tree.create_date,
                'img': [img.photo.url for img in tree.TreeInfoPhotos.all()]
            },
            'geometry': {
                'type': tree.type,
                'coordinates': str(tree.location).split(', '),
            }
        } for tree in trees]

        return JsonResponse(
            data={
                'type': 'FeatureCollection',
                'features': [] + tree + organization,
            },
            status=200
        )
