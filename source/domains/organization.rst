Домен: Организации
==================

Организации-исполнители, их кошельки и реквизиты.

.. contents:: Содержание
   :local:
   :depth: 2

---

ORM-модели
----------

Organization
~~~~~~~~~~~~

Таблица ``organization`` — организация-исполнитель.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``organization_id``
     - ``int`` PK
     - Первичный ключ; передаётся в ``create_service_order(organization_id=...)``
   * - ``fullname``
     - ``str(255)``
     - Полное название
   * - ``shortname``
     - ``str(30)``
     - Краткое название
   * - ``face``
     - ``int``
     - 0=ЮЛ, 1=ИП/физлицо
   * - ``inn``
     - ``str(20)``
     - ИНН
   * - ``kpp``
     - ``str(20)``
     - КПП
   * - ``ogrn``
     - ``str(20)``
     - ОГРН
   * - ``address``
     - ``str``
     - Адрес
   * - ``hidden``
     - ``int``
     - 0=активна

.. code-block:: python

   from autodealer.domain.organization import Organization

   org = Organization.objects.get(organization_id=1)
   print(org.shortname, org.inn)

   active = Organization.objects.filter(hidden=0).all()

Wallet
~~~~~~

Таблица ``wallet`` — кассы и расчётные счета организации.
Также используется в домене :doc:`payment`.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``wallet_id``
     - ``int`` PK
     - Первичный ключ; передаётся в ``create_payment(wallet_id=...)``
   * - ``name``
     - ``str(100)``
     - Название кошелька
   * - ``organization_id``
     - ``int`` FK
     - Организация-владелец

DirectoryRegistry
~~~~~~~~~~~~~~~~~

Таблица ``directory_registry`` — универсальная метазапись для любой сущности.
Создаётся автоматически при создании клиента, организации, документа.

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``directory_registry_id``
     - ``int`` PK
     - Первичный ключ
   * - ``metatable_id``
     - ``int``
     - Тип сущности: 1=Organization, 3=Client, 4=ModelDetail
   * - ``create_user_id``
     - ``int`` FK
     - Кто создал
   * - ``change_user_id``
     - ``int`` FK
     - Кто изменил последним

.. note::

   ``directory_registry`` создаётся **до** основной записи. Триггеры Firebird
   читают ``USER_CONNECTION`` по ``CURRENT_CONNECTION`` для заполнения ``change_user_id``.
   Перед UPDATE на таблицах с ``directory_registry_id`` необходимо вызвать
   ``set_session_user()``.

---

Высокоуровневые функции (``services``)
---------------------------------------

get_organization
~~~~~~~~~~~~~~~~

.. function:: autodealer.services.get_organization(organization_id)

   Загрузить организацию с кошельками.

   :returns: :class:`~autodealer.services.OrganizationInfo` или ``None``.

   .. code-block:: python

      from autodealer.services import get_organization

      org = get_organization(1)
      print(org)
      # OrganizationInfo(id=1, name='ИП Кропотов', inn=None, wallets=2)

      wallet_id = org.wallet_id_by_name("наличн")   # → 1

list_organizations
~~~~~~~~~~~~~~~~~~

.. function:: autodealer.services.list_organizations()

   Все активные организации с кошельками.

   :returns: ``list[OrganizationInfo]``

create_organization
~~~~~~~~~~~~~~~~~~~

.. function:: autodealer.services.create_organization(fullname, *, shortname=None, inn=None, kpp=None, ogrn=None, address=None, face=0, wallet_names=None, created_by_user_id=1)

   Создать организацию с кошельками атомарно.

   :param str fullname: Полное название.
   :param list[str] wallet_names: Названия касс/счетов.
   :returns: :class:`~autodealer.services.OrganizationInfo`.

   .. code-block:: python

      from autodealer.services import create_organization

      org = create_organization(
          "ООО СК-Авто Казань",
          shortname="СК-Авто",
          inn="1655012345",
          address="г. Казань, ул. Скрябина 8к1",
          wallet_names=["Наличные", "Банковская карта", "СБП"],
      )
      print(org.organization_id, org.wallets)

---

Типы данных
-----------

.. class:: autodealer.services.OrganizationInfo

   .. attribute:: organization_id: int
   .. attribute:: fullname: str | None
   .. attribute:: shortname: str | None
   .. attribute:: inn: str | None
   .. attribute:: kpp: str | None
   .. attribute:: ogrn: str | None
   .. attribute:: address: str | None
   .. attribute:: face: int
   .. attribute:: hidden: int
   .. attribute:: wallets: list[dict]

      Список ``[{"wallet_id": 1, "name": "Наличные"}, ...]``

   .. method:: wallet_id_by_name(name) -> int | None

      Найти ``wallet_id`` по части названия (без учёта регистра).

      .. code-block:: python

         org.wallet_id_by_name("наличн")   # → 1
         org.wallet_id_by_name("сбер")     # → 3
