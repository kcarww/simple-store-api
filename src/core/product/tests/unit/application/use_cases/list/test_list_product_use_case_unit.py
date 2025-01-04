import pytest
from unittest.mock import Mock
from datetime import datetime
from uuid import uuid4

from core.product.application.use_cases.list.list_product_dto import ListProductRequest
from core.product.application.use_cases.list.list_product_use_case import ListProductUseCase
from core.product.domain.product import Product



class TestListProductUseCase:
    @pytest.fixture
    def mock_repository(self):
        return Mock()

    @pytest.fixture
    def use_case(self, mock_repository):
        return ListProductUseCase(product_repository=mock_repository)

    def test_execute_returns_paginated_sorted_products(self, use_case, mock_repository):
        products = [
            Product(
                id=uuid4(),
                name="Product B",
                price=200.0,
                stock=20,
                active=True,
                description="Product B description",
                created_at=datetime(2024, 1, 1, 12, 0, 0),
                updated_at=datetime(2024, 1, 1, 12, 0, 0),
            ),
            Product(
                id=uuid4(),
                name="Product A",
                price=100.0,
                stock=10,
                active=True,
                description="Product A description",
                created_at=datetime(2024, 1, 1, 12, 0, 0),
                updated_at=datetime(2024, 1, 1, 12, 0, 0),
            ),
        ]
        mock_repository.find_all.return_value = products
        request = ListProductRequest(order_by="name", current_page=1)

        response = use_case.execute(request)

        mock_repository.find_all.assert_called_once()
        assert len(response.data) == 2
        assert response.data[0].name == "Product A" 
        assert response.data[1].name == "Product B"
        assert response.meta.current_page == 1
        assert response.meta.per_page == 2  
        assert response.meta.total == 2

    def test_execute_with_empty_repository(self, use_case, mock_repository):
        mock_repository.find_all.return_value = []
        request = ListProductRequest(order_by="name", current_page=1)

        response = use_case.execute(request)

        mock_repository.find_all.assert_called_once()
        assert len(response.data) == 0
        assert response.meta.total == 0
        assert response.meta.current_page == 1
