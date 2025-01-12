from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from src.core.product.application.use_cases.update.update_product_dto import UpdateProductInput
from src.core.product.application.use_cases.update.update_product_use_case import UpdateProductUseCase
from src.core.product.application.use_cases.create.create_product_dto import CreateProductInput
from src.core.product.application.use_cases.create.create_product_use_case import CreateProductUseCase
from src.core.product.application.use_cases.exceptions.exceptions import ProductNotFound
from src.core.product.application.use_cases.find.find_product_dto import GetProductInput
from src.core.product.application.use_cases.find.find_product_use_case import FindProductUseCase
from src.core.product.application.use_cases.list.list_product_dto import ListProductRequest
from src.core.product.application.use_cases.list.list_product_use_case import ListProductUseCase
from django_project.product.repository import DjangoORMProductRepository
from django_project.product.serializers import CreateProductRequestSerializer, CreateProductResponseSerializer, ListProductResponseSerializer, RetrieveProductRequestSerializer, RetrieveProductResponseSerializer, UpdateProductResponseSerializer


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
    
    def list(self, request: Request) -> Response:
        order_by = request.query_params.get('order_by', 'name')
        current_page = request.query_params.get('current_page', 1)
        input = ListProductRequest(order_by=order_by, current_page=current_page)
        use_case = ListProductUseCase(product_repository=DjangoORMProductRepository())
        output = use_case.execute(input)

        serializer = ListProductResponseSerializer(instance=output)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request: Request, pk: str = None) -> Response:
        serializer = RetrieveProductRequestSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)

        use_case = FindProductUseCase(product_repository=DjangoORMProductRepository())
        try:
            result = use_case.execute(
                GetProductInput(id=serializer.validated_data['id'])
            )
            
        except ProductNotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        product_output = RetrieveProductResponseSerializer(instance=result)
        return Response(
            status=status.HTTP_200_OK,
            data=product_output.data
        )
    
    def update(self, request: Request, pk: str = None) -> Response:
        serializer = UpdateProductResponseSerializer(data={
            **request.data,
            "id": pk
        })
        serializer.is_valid(raise_exception=True)

        product_input = UpdateProductInput(**serializer.validated_data)
        use_case = UpdateProductUseCase(product_repository=DjangoORMProductRepository())
        try:
            product_output = use_case.execute(product_input)
        except ProductNotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(
            status=status.HTTP_202_ACCEPTED,
            data=CreateProductResponseSerializer(instance=product_output).data
        )

            
            
