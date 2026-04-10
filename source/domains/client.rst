Домен: Клиенты
==============

Всё, что связано с клиентами: профили, контакты, карты лояльности.

.. contents:: Содержание
   :local:
   :depth: 2

---

ORM-модели
----------

Client
~~~~~~

Таблица ``client`` — основная запись о клиенте.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Поле
     - Тип
     - Описание
   * - ``client_id``
     - ``int`` PK
     - Первичный ключ
   * - ``directory_registry_id``
     - ``int`` FK
     - Ссылка на ``directory_registry`` (аудит)
   * - ``client_tree_id``
     - ``int`` FK
     - Папка клиентов (1=Физлица, 2=Юрлица, 3=VIP)
   * - ``fullname``
     - ``str(255)``
     - Полное имя
   * - ``shortname``
     - ``str(30)``
     - Краткое имя (первые 30 символов fullname)
   * - ``birth``
     - ``date``
     - Дата рождения
   * - ``sex``
     - ``int``
     - 1=муж, 2=жен, 0=не указан
   * - ``face``
     - ``int``
     - 0=юрлицо, 1=физлицо/ИП
   * - ``discount``
     - ``float``
     - Скидка на товары %
   * - ``discount_work``
     - ``float``
     - Скидка на работы %
   * - ``hidden``
     - ``int``
     - 0=активен, 1=скрыт
   * - ``notes``
     - ``text``
     - Произвольное примечание

.. code-block:: python

   from autodealer.domain.client import Client

   client = Client.objects.get(client_id=920)
   print(client.fullname, client.discount_work)

   # Поиск по имени
   results = Client.objects.filter(fullname__icontains="Иванов").all()

Contact
~~~~~~~

Таблица ``contact`` — телефоны и email клиентов/организаций.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Поле
     - Тип
     - Описание
   * - ``contact_id``
     - ``int`` PK
     - Первичный ключ
   * - ``directory_registry_link_id``
     - ``int`` FK
     - Ссылка на ``directory_registry`` владельца
   * - ``mobile``
     - ``str``
     - Мобильный телефон
   * - ``email``
     - ``str``
     - Email
   * - ``default_contact``
     - ``int``
     - 1=основной контакт
   * - ``hidden``
     - ``int``
     - 0=активен

ClientTree
~~~~~~~~~~

Таблица ``client_tree`` — иерархия папок клиентов (Физлица / Юрлица / VIP).

.. code-block:: python

   from autodealer.domain.client_tree import ClientTree

   folders = ClientTree.objects.filter(hidden=0).all()

CardInfo
~~~~~~~~

Таблица ``card_info`` — дисконтные/бонусные карты клиентов.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Поле
     - Тип
     - Описание
   * - ``card_info_id``
     - ``int`` PK
     - Первичный ключ
   * - ``directory_registry_link_id``
     - ``int`` FK
     - Владелец карты (клиент)
   * - ``number``
     - ``str``
     - Номер карты
   * - ``hidden``
     - ``int``
     - 0=активна

---

Высокоуровневые действия (``actions.client``)
----------------------------------------------

create_client
~~~~~~~~~~~~~

.. function:: autodealer.actions.client.create_client(fullname, *, phone=None, email=None, birth=None, sex=None, discount=0.0, discount_work=0.0, client_tree_id=1, created_by_user_id=1)

   Создать клиента атомарно: ``DirectoryRegistry`` → ``Client`` → ``Contact``.

   :param str fullname: Полное имя (обязательно).
   :param str phone: Мобильный телефон.
   :param str email: Email.
   :param date birth: Дата рождения.
   :param int sex: 1=муж, 2=жен.
   :param float discount: Скидка на товары %.
   :param float discount_work: Скидка на работы %.
   :param int client_tree_id: Папка (1=Физлица, 2=Юрлица, 3=VIP).
   :returns: ``client_id``.
   :rtype: int

   .. code-block:: python

      from autodealer.actions.client import create_client
      from datetime import date

      client_id = create_client(
          "Иванов Иван Иванович",
          phone="79991234567",
          birth=date(1990, 5, 15),
          discount_work=5.0,
      )
