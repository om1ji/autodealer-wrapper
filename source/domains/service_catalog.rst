Домен: Справочник услуг
=======================

Комплексные и обычные услуги, используемые при создании заказ-нарядов.

.. contents:: Содержание
   :local:
   :depth: 2

---

Схема связей
------------

.. code-block:: text

   service_complex_work_tree          ← дерево категорий (напр. «Кат.01 Седан»)
       │
       └── service_complex_work_item  ← группа работ внутри категории
               │
               └── service_complex_work  ← конкретная работа (name, price, time_value)

   service_common_work_tree           ← дерево каталога услуг
       │
       └── service_common_work        ← услуга в каталоге (bar_code, price)

---

ORM-модели
----------

ServiceComplexWorkTree
~~~~~~~~~~~~~~~~~~~~~~

Таблица ``service_complex_work_tree`` — корневые категории комплексных работ.
Каждой категории RocketWash соответствует свой ``service_complex_work_tree_id``.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``service_complex_work_tree_id``
     - Категория
   * - 11
     - Кат.01 — Седан / хетчбэк
   * - 15
     - Кат.02 — Внедорожник / кроссовер
   * - 16
     - Кат.03 — Микроавтобус
   * - 17
     - Кат.04 — Крупный внедорожник / минивэн

.. code-block:: python

   from autodealer.domain.service_complex_work_tree import ServiceComplexWorkTree
   trees = ServiceComplexWorkTree.objects.all()

ServiceComplexWorkItem
~~~~~~~~~~~~~~~~~~~~~~

Таблица ``service_complex_work_item`` — группа работ внутри дерева.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``service_complex_work_item_id``
     - ``int`` PK
     - Первичный ключ
   * - ``service_complex_work_tree_id``
     - ``int`` FK
     - Дерево / категория
   * - ``name``
     - ``str``
     - Название группы

ServiceComplexWork
~~~~~~~~~~~~~~~~~~

Таблица ``service_complex_work`` — конкретная работа в комплексе.
Строки этой таблицы передаются в ``create_service_order`` как ``ServiceOrderItem``.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``service_complex_work_id``
     - ``int`` PK
     - Первичный ключ
   * - ``service_complex_work_item_id``
     - ``int`` FK
     - Группа работ
   * - ``name``
     - ``str(255)``
     - Название (макс. 255 символов)
   * - ``price``
     - ``Decimal``
     - Цена за единицу
   * - ``time_value``
     - ``Decimal``
     - Длительность в минутах
   * - ``quantity``
     - ``int``
     - Количество (по умолчанию 1)
   * - ``position_number``
     - ``int``
     - Порядок отображения
   * - ``external_id``
     - ``str(512)``
     - Внешний ID

.. code-block:: python

   from autodealer.domain.service_complex_work import ServiceComplexWork
   from autodealer.domain.service_complex_work_item import ServiceComplexWorkItem

   # Все работы категории Кат.01
   item_ids = [
       i.service_complex_work_item_id
       for i in ServiceComplexWorkItem.objects.filter(service_complex_work_tree_id=11).all()
   ]
   works = ServiceComplexWork.objects.filter(service_complex_work_item_id__in=item_ids).all()

ServiceCommonWork
~~~~~~~~~~~~~~~~~

Таблица ``service_common_work`` — общий каталог услуг (не привязан к категориям авто).
Используется функцией ``get_or_create_service``.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``service_common_work_id``
     - ``int`` PK
     - Первичный ключ
   * - ``service_common_work_tree_id``
     - ``int`` FK
     - Папка каталога
   * - ``name``
     - ``str``
     - Название
   * - ``price``
     - ``Decimal``
     - Цена
   * - ``time_value``
     - ``Decimal``
     - Длительность в минутах
   * - ``bar_code``
     - ``str``
     - Уникальный ключ (напр. ``"rw:821460"``) — используется для идемпотентности

---

Высокоуровневые функции (``services``)
---------------------------------------

iter_complex_works_by_tree
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: autodealer.services.iter_complex_works_by_tree(tree_id)

   Генератор всех работ из дерева ``service_complex_work_tree``.
   Не загружает все записи в память сразу.

   :param int tree_id: ``service_complex_work_tree_id``.
   :yields: Экземпляры :class:`~autodealer.domain.service_complex_work.ServiceComplexWork`.

   .. code-block:: python

      from autodealer.services import iter_complex_works_by_tree

      for work in iter_complex_works_by_tree(11):   # Кат.01
          print(work.name, work.price, work.time_value)

get_or_create_service
~~~~~~~~~~~~~~~~~~~~~

.. function:: autodealer.services.get_or_create_service(name, price=None, time_value=None, bar_code=None, tree_id=None)

   Найти услугу в ``service_common_work`` по ``bar_code`` или создать новую.
   Идемпотентно: повторный вызов с тем же ``bar_code`` вернёт существующую запись.

   :param str name: Название услуги.
   :param float price: Цена по умолчанию.
   :param float time_value: Длительность в минутах.
   :param str bar_code: Уникальный ключ (напр. ``"rw:821460"``).
   :param int tree_id: FK → ``service_common_work_tree``.
   :returns: ``service_common_work_id``.
   :rtype: int

   .. code-block:: python

      from autodealer.services import get_or_create_service

      svc_id = get_or_create_service(
          "Комплекс",
          price=2300.0,
          time_value=90,
          bar_code="rw:821460",
      )
