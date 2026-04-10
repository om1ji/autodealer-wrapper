Домен: Платежи
==============

Создание и чтение документов оплаты, привязка к заказ-нарядам.

.. contents:: Содержание
   :local:
   :depth: 2

---

Схема связей
------------

.. code-block:: text

   document_out
       │
       └── payment_out.document_out_id ──► payment
                                               │
                                               ├── payment.wallet_id ──► wallet
                                               ├── payment.payment_type_id ──► payment_type
                                               │
                                               ├── payment_document.payment_id
                                               │       └── document_registry  (метазапись заказ-наряда)
                                               │
                                               └── money_document_payment.payment_id
                                                       └── money_document_detail
                                                               (accounting_item_id=3
                                                                «Поступление от клиента»)

---

ORM-модели
----------

Payment
~~~~~~~

Таблица ``payment`` — основная запись платежа.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``payment_id``
     - ``int`` PK
     - Первичный ключ
   * - ``payment_type_id``
     - ``int`` FK
     - Способ оплаты (``payment_type``)
   * - ``wallet_id``
     - ``int`` FK
     - Касса/счёт списания (``wallet``)
   * - ``summa``
     - ``Decimal``
     - Сумма платежа
   * - ``payment_date``
     - ``datetime``
     - Дата и время платежа
   * - ``document_registry_id``
     - ``int`` FK
     - Метазапись связанного документа
   * - ``notes``
     - ``text``
     - Примечание

PaymentOut
~~~~~~~~~~

Таблица ``payment_out`` — связь «платёж ↔ document_out» (многие-ко-многим).

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``payment_out_id``
     - ``int`` PK
     - Первичный ключ
   * - ``document_out_id``
     - ``int`` FK
     - Заказ-наряд
   * - ``payment_id``
     - ``int`` FK
     - Платёж

PaymentDocument
~~~~~~~~~~~~~~~

Таблица ``payment_document`` — связь «платёж ↔ document_registry».

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``payment_document_id``
     - ``int`` PK
     - Первичный ключ
   * - ``document_registry_id``
     - ``int`` FK
     - Метазапись документа
   * - ``payment_id``
     - ``int`` FK
     - Платёж

PaymentType
~~~~~~~~~~~

Таблица ``payment_type`` — справочник способов оплаты.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``payment_type_id``
     - Название
   * - 1
     - Наличный расчет
   * - 2
     - Безналичный расчет
   * - 7
     - Банковская карта

Wallet
~~~~~~

Таблица ``wallet`` — кассы и счета организации.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``wallet_id``
     - ``int`` PK
     - Первичный ключ
   * - ``name``
     - ``str(100)``
     - Название (напр. «Наличный расчет», «СберБанк»)
   * - ``organization_id``
     - ``int`` FK
     - Организация-владелец

MoneyDocumentDetail
~~~~~~~~~~~~~~~~~~~

Таблица ``money_document_detail`` — бухгалтерская проводка.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``money_document_detail_id``
     - ``int`` PK
     - Первичный ключ
   * - ``document_out_id``
     - ``int`` FK
     - Заказ-наряд
   * - ``wallet_id``
     - ``int`` FK
     - Касса/счёт
   * - ``payment_type_id``
     - ``int`` FK
     - Способ оплаты
   * - ``accounting_item_id``
     - ``int`` FK
     - Статья (3=«Поступление от клиента»)

MoneyDocumentPayment
~~~~~~~~~~~~~~~~~~~~

Таблица ``money_document_payment`` — связь проводки с платежом.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``money_document_payment_id``
     - ``int`` PK
     - Первичный ключ
   * - ``money_document_detail_id``
     - ``int`` FK
     - Проводка
   * - ``payment_id``
     - ``int`` FK
     - Платёж

---

Высокоуровневые действия (``actions.payment``)
-----------------------------------------------

Справочники
~~~~~~~~~~~

.. function:: autodealer.actions.payment.get_wallets(organization_id)

   Кошельки организации.

   :returns: ``list[WalletInfo]``

   .. code-block:: python

      from autodealer.actions.payment import get_wallets
      for w in get_wallets(1):
          print(w.wallet_id, w.name)

.. function:: autodealer.actions.payment.get_payment_types()

   Активные способы оплаты.

   :returns: ``list[PaymentTypeInfo]``

Чтение
~~~~~~

.. function:: autodealer.actions.payment.get_payments(document_out_id)

   Все платежи по заказ-наряду.

   :param int document_out_id: PK заказ-наряда.
   :returns: ``list[PaymentRecord]``

   .. code-block:: python

      from autodealer.actions.payment import get_payments
      for p in get_payments(42):
          print(p.payment_id, p.summa, p.payment_type_name, p.wallet_name)

Создание платежа
~~~~~~~~~~~~~~~~

.. function:: autodealer.actions.payment.create_payment(*, document_out_id, summa, wallet_id, payment_type_id, payment_date=None, notes=None)

   Создать платёж. Атомарно создаёт полную цепочку из 5 записей
   и обновляет ``document_out.date_payment``.

   :param int document_out_id: PK заказ-наряда.
   :param float summa: Сумма.
   :param int wallet_id: FK в ``wallet``.
   :param int payment_type_id: FK в ``payment_type``.
   :param datetime payment_date: По умолчанию — текущее время.
   :param str notes: Примечание.
   :returns: ``payment_id``.
   :rtype: int
   :raises ValueError: Если заказ-наряд не найден.

   .. code-block:: python

      from autodealer.actions.payment import create_payment

      payment_id = create_payment(
          document_out_id=42,
          summa=2300.0,
          wallet_id=1,        # Наличный расчёт
          payment_type_id=1,
      )

Разбивка оплаты
~~~~~~~~~~~~~~~

.. function:: autodealer.actions.payment.create_payment_split(*, document_out_id, parts, payment_date=None)

   Несколько платежей за один заказ-наряд.
   Удобно когда клиент платит частично наличными, частично картой.

   :param int document_out_id: PK заказ-наряда.
   :param list[PaymentSplitItem] parts: Части платежа.
   :param datetime payment_date: Единая дата для всех частей.
   :returns: ``list[payment_id]``
   :raises ValueError: Если ``parts`` пустой или сумма <= 0.

   .. code-block:: python

      from autodealer.actions.payment import create_payment_split, PaymentSplitItem

      ids = create_payment_split(
          document_out_id=42,
          parts=[
              PaymentSplitItem(wallet_id=1, payment_type_id=1, summa=1000.0),  # наличные
              PaymentSplitItem(wallet_id=4, payment_type_id=7, summa=1300.0),  # карта
          ],
      )

---

Типы данных
-----------

.. class:: autodealer.actions.payment.WalletInfo

   .. attribute:: wallet_id: int
   .. attribute:: name: str
   .. attribute:: organization_id: int

.. class:: autodealer.actions.payment.PaymentTypeInfo

   .. attribute:: payment_type_id: int
   .. attribute:: name: str

.. class:: autodealer.actions.payment.PaymentRecord

   .. attribute:: payment_id: int
   .. attribute:: summa: Decimal
   .. attribute:: payment_date: datetime
   .. attribute:: payment_type_id: int
   .. attribute:: payment_type_name: str | None
   .. attribute:: wallet_id: int | None
   .. attribute:: wallet_name: str | None
   .. attribute:: notes: str | None

.. class:: autodealer.actions.payment.PaymentSplitItem

   .. attribute:: wallet_id: int
   .. attribute:: payment_type_id: int
   .. attribute:: summa: float
   .. attribute:: notes: str | None
