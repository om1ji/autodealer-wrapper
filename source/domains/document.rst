Домен: Документы / Заказ-наряды
================================

Создание и чтение заказ-нарядов (``document_out``) и связанных цепочек записей.

.. contents:: Содержание
   :local:
   :depth: 2

---

Схема связей
------------

.. code-block:: text

   document_out  (document_type_id=11, client_id, summa, date_accept)
       │
       ├── service_work × N           ← строки услуг (name, price, time_value)
       │
       └── document_registry          ← метазапись (аудит: кто создал, когда)
               │
               └── document_out_header  (номер, дата, prefix="АВТ", state=2)
                       │
                       └── document_service_detail  ← привязка авто (если передан client_car)

---

ORM-модели
----------

DocumentOut
~~~~~~~~~~~

Таблица ``document_out`` — основная запись документа.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``document_out_id``
     - ``int`` PK
     - Первичный ключ; возвращается из ``create_service_order``
   * - ``document_type_id``
     - ``int`` FK
     - Тип документа (11=Заказ-наряд)
   * - ``client_id``
     - ``int`` FK
     - Клиент
   * - ``organization_id``
     - ``int`` FK
     - Организация-исполнитель
   * - ``summa``
     - ``Decimal``
     - Итоговая сумма
   * - ``date_accept``
     - ``datetime``
     - Дата/время приёма / окончания работ
   * - ``date_payment``
     - ``datetime``
     - Дата оплаты (обновляется при ``create_payment``)

DocumentRegistry
~~~~~~~~~~~~~~~~

Таблица ``document_registry`` — метазапись для каждого документа (аудит + связь с платежами).

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``document_registry_id``
     - ``int`` PK
     - Первичный ключ
   * - ``metatable_id``
     - ``int``
     - Тип сущности (12=document_out)
   * - ``create_user_id``
     - ``int`` FK
     - Кто создал
   * - ``create_date``
     - ``datetime``
     - Когда создал
   * - ``change_user_id``
     - ``int`` FK
     - Кто изменил последним
   * - ``change_date``
     - ``datetime``
     - Когда изменил
   * - ``document_type_id_cache``
     - ``int`` FK
     - Кэш типа документа

DocumentOutHeader
~~~~~~~~~~~~~~~~~

Таблица ``document_out_header`` — заголовок документа (номер, дата, исполнитель).

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``document_out_header_id``
     - ``int`` PK
     - Первичный ключ
   * - ``document_out_id``
     - ``int`` FK
     - Ссылка на ``document_out``
   * - ``document_registry_id``
     - ``int`` FK
     - Ссылка на ``document_registry``
   * - ``document_out_tree_id``
     - ``int`` FK
     - Папка документов
   * - ``user_id``
     - ``int`` FK
     - Исполнитель
   * - ``prefix``
     - ``str(5)``
     - Префикс номера (``"АВТ"``)
   * - ``number``
     - ``int``
     - Порядковый номер
   * - ``suffix``
     - ``str(5)``
     - Суффикс номера (напр. ``"К"``)
   * - ``fullnumber``
     - ``str(21)``
     - Вычисляемое поле: ``prefix + number + suffix`` (COMPUTED BY в Firebird)
   * - ``date_create``
     - ``datetime``
     - Дата создания документа
   * - ``state``
     - ``int``
     - Статус: 2=Черновик, 4=Оформлен, -1=Удалён
   * - ``notes``
     - ``text``
     - Примечание

DocumentServiceDetail
~~~~~~~~~~~~~~~~~~~~~

Таблица ``document_service_detail`` — привязка автомобиля к заказ-наряду.
Создаётся только если в ``create_service_order`` передан ``client_car``.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``document_service_detail_id``
     - ``int`` PK
     - Первичный ключ
   * - ``document_out_header_id``
     - ``int`` FK
     - Заголовок документа
   * - ``model_link_id``
     - ``int`` FK
     - Привязка авто клиента (``model_link.model_link_id``)

ServiceWork
~~~~~~~~~~~

Таблица ``service_work`` — строки услуг в заказ-наряде.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``service_work_id``
     - ``int`` PK
     - Первичный ключ
   * - ``document_out_id``
     - ``int`` FK
     - Заказ-наряд
   * - ``name``
     - ``str(255)``
     - Название услуги
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
     - Порядок строки
   * - ``external_id``
     - ``str(512)``
     - Внешний ID (напр. из RocketWash)

DocumentOutTree
~~~~~~~~~~~~~~~

Таблица ``document_out_tree`` — иерархия папок для документов реализации.

.. code-block:: python

   from autodealer.domain.document_out_tree import DocumentOutTree

   folders = DocumentOutTree.objects.filter(hidden=0).all()
   # document_out_tree_id=3 → «АвтоМойка»

---

Высокоуровневые функции (``services``)
---------------------------------------

create_service_order
~~~~~~~~~~~~~~~~~~~~

.. function:: autodealer.services.create_service_order(*, client_id, items, document_out_tree_id, organization_id, client_car=None, date_start, date_finish, created_by_user_id=1, notes=None, service_order_suffix=None)

   Создать заказ-наряд. Все записи — в одной транзакции.

   :param int client_id: PK клиента.
   :param list[ServiceOrderItem] items: Строки услуг. Не может быть пустым.
   :param int document_out_tree_id: Папка документов.
   :param int organization_id: Организация-исполнитель.
   :param int client_car: ``model_link_id`` — привязка авто (опционально).
   :param datetime date_start: Дата начала.
   :param datetime date_finish: Дата окончания / приёма.
   :param int created_by_user_id: Исполнитель (по умолчанию 1).
   :param str notes: Примечание.
   :param str service_order_suffix: Суффикс номера (напр. ``"К"``).
   :returns: ``document_out_id``.
   :rtype: int
   :raises ValueError: Если ``items`` пустой.

   .. code-block:: python

      from datetime import datetime, timedelta
      from autodealer.services import create_service_order, ServiceOrderItem

      now = datetime.now()
      doc_id = create_service_order(
          client_id=920,
          organization_id=1,
          document_out_tree_id=3,
          date_start=now,
          date_finish=now + timedelta(hours=1),
          client_car=959,
          notes="Комплексная мойка",
          service_order_suffix="К",
          items=[
              ServiceOrderItem("Комплекс",    price=2300.0, time_value=90, external_id="821460"),
              ServiceOrderItem("Вторая Фаза", price=800.0,  time_value=20, external_id="821462"),
          ],
      )

get_service_order
~~~~~~~~~~~~~~~~~

.. function:: autodealer.services.get_service_order(document_out_id)

   Прочитать заказ-наряд со строками услуг.

   :returns: :class:`~autodealer.services.ServiceOrder` или ``None``.

   .. code-block:: python

      order = get_service_order(42)
      print(order.summa, order.date_accept)
      for item in order.items:
          print(item.name, item.price)

.. class:: autodealer.services.ServiceOrderItem

   .. attribute:: name: str
   .. attribute:: price: float
   .. attribute:: time_value: float
   .. attribute:: quantity: int = 1
   .. attribute:: external_id: str | None

.. class:: autodealer.services.ServiceOrder

   .. attribute:: document_out_id: int
   .. attribute:: client_id: int | None
   .. attribute:: summa: float
   .. attribute:: date_accept: datetime | None
   .. attribute:: date_payment: datetime | None
   .. attribute:: document_number: int | None
   .. attribute:: client_car: int | None
   .. attribute:: items: list[ServiceOrderItem]

---

Константы
---------

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Константа
     - Значение
     - Описание
   * - ``document_type_id``
     - ``11``
     - Заказ-наряд
   * - ``prefix``
     - ``"АВТ"``
     - Префикс номера
   * - ``state`` (Черновик)
     - ``2``
     - Статус при создании
   * - ``metatable_id``
     - ``12``
     - ``document_registry.metatable_id``
