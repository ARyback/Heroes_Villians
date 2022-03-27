from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from super_types.models import SuperType

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type_name = request.query_params.get('super_type')
        print(super_type_name)
        if super_type_name:
            super_type_name = request.query_params.get('super_type')
            print(super_type_name)
            queryset = Super.objects.all()
            queryset = queryset.filter(super_type__type=super_type_name)
            serializer = SuperSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            super_types = SuperType.objects.all()
            custom_response_dictionary = {}
            for super_type in super_types:
                supers = Super.objects.filter(super_type_id=super_type.id)
                super_serializer = SuperSerializer(supers, many=True)
                custom_response_dictionary[super_type.type] = {
                    "supers": super_serializer.data
                }
            return Response(custom_response_dictionary)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def supers_list(request):
#     if request.method == 'GET':
#         super_type_name = request.query_params.get('super_type')
#         print(super_type_name)
#         queryset = Super.objects.all()
#         if super_type_name:
#             queryset = queryset.filter(super_type__type=super_type_name)
#         serializer = SuperSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SuperSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def super_type_list(request):
#     appending_dict_super_type = {}
#     appending_dict_super_type['name'] = 'David'
#     print(appending_dict_super_type)
#     super_types = SuperType.object.all()
#     custom_response_dictionary = {}
#     for super_type in super_types:
#         supers = Super.objects.filter(super_type_id=super_type.id)
#         supers_serializer = SuperSerializer(supers, many=True)
#         custom_response_dictionary[super_type.name] = {
#             "type": super_type.type,
#             "supers": supers_serializer.data
#         }
#     return Response(custom_response_dictionary)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)