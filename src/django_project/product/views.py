from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core.product.application.use_cases.create.create_product_dto import CreateProductInput
from core.product.application.use_cases.create.create_product_use_case import CreateProductUseCase
from django_project.product.repository import DjangoORMProductRepository
from django_project.product.serializers import CreateProductRequestSerializer, CreateProductResponseSerializer


class ProductViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        serializer = CreateProductRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_input = CreateProductInput(**serializer.validated_data)
        use_case = CreateProductUseCase(product_repository=DjangoORMProductRepository())
        product_output = use_case.execute(product_input)
        return Response(
            status=status.HTTP_201_CREATED,
            data=CreateProductResponseSerializer(instance=product_output).data
        )