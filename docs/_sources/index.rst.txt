autodealer
==========

Python ORM-обёртка над базой данных системы **АвтоДилер** (Firebird).

Библиотека предоставляет:

- Автоматически сгенерированные ORM-модели для всех таблиц БД
- Django-подобный QuerySet API (``Model.objects.filter(...).all()``)
- Управление подключением и транзакциями через SQLAlchemy 2.0
- Высокоуровневые функции для клиентов, заказ-нарядов, платежей

.. toctree::
   :maxdepth: 2
   :caption: Начало работы

   quickstart

.. toctree::
   :maxdepth: 2
   :caption: Бизнес-домены

   domains/client
   domains/vehicle
   domains/document
   domains/payment
   domains/service_catalog
   domains/organization

.. toctree::
   :maxdepth: 2
   :caption: Интеграции

   api/rocketwash

.. toctree::
   :maxdepth: 1
   :caption: Инфраструктура

   api/queryset
   api/connection
