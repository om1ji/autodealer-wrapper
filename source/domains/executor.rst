Домен: Исполнители работ
=========================

Связь «работа в заказ-наряде → исполнитель (сотрудник)» и вспомогательные
сущности. В UI АвтоДилера в строке работы отображается колонка «Исполнитель»
— её значение приходит именно отсюда.

.. contents:: Содержание
   :local:
   :depth: 2

---

Обзор связей
------------

.. code-block:: text

   service_work                (строка работы в заказ-наряде)
        │
        │  1 : N
        ▼
   brigade_structure           (связка «работа ↔ исполнитель» + ставка/проценты)
        │
        │  N : 1
        ▼
   employee                    (справочник сотрудников)
        │
        │  1 : 1
        ▼
   directory_registry          (аудит: кем/когда создан)

   executor                    (VIEW поверх brigade_structure + employee)

**Правило записи:** INSERT идёт ТОЛЬКО в ``brigade_structure``. Представление
``executor`` обновится автоматически — оно не таблица, а SQL-VIEW.

---

Таблица BRIGADE_STRUCTURE
-------------------------

Физическая таблица связки. Одна строка = один исполнитель на одной работе.
Одной работе (``service_work_id``) может соответствовать несколько исполнителей
(бригада) — тогда ``percent_work_party`` суммарно должен давать 100 %.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Поле
     - Тип
     - Описание
   * - ``brigade_structure_id``
     - ``int`` PK
     - Первичный ключ (автоинкремент через generator)
   * - ``service_work_id``
     - ``int`` FK
     - Ссылка на ``service_work.service_work_id``
   * - ``employee_id``
     - ``int`` FK (nullable)
     - Ссылка на ``employee.employee_id``. Заполняется для штатных
       сотрудников. Для внешнего подрядчика используется ``provider_id``.
   * - ``provider_id``
     - ``int`` FK (nullable)
     - Ссылка на ``provider.provider_id`` — если работу сделал внешний
       поставщик/подрядчик. Для автомойки обычно ``NULL``.
   * - ``brigade_executor_id``
     - ``int`` FK (nullable)
     - Ссылка на ``brigade_executor`` — именованная «бригада». Опционально.
   * - ``tariff``
     - ``float``
     - Почасовая ставка исполнителя. Для автомойки обычно ``0``
       (зарплата считается через проценты).
   * - ``percent_exec_work``
     - ``float``
     - Процент стоимости работы, относящийся к исполнителю
       (для зарплатного расчёта). Типичные значения: 30-40 %.
   * - ``percent_work_party``
     - ``float``
     - Доля этого исполнителя в работе (если бригада из нескольких человек
       делит одну работу). Для одиночного исполнителя — ``100.0``.

.. note::

   Поля ``fullname``, ``shortname``, ``birth``, ``sex``, ``hidden``
   *отсутствуют* в ``brigade_structure``. Они отображаются в UI через VIEW
   ``executor``, который достаёт их из ``employee`` по ``employee_id``.

Пример создания связки напрямую (SQL):

.. code-block:: python

   from sqlalchemy import text
   from autodealer.connection import session_scope

   with session_scope() as s:
       s.execute(
           text(
               "INSERT INTO brigade_structure"
               " (service_work_id, employee_id, tariff,"
               "  percent_exec_work, percent_work_party)"
               " VALUES (:sw, :emp, 0, 100, 100)"
           ),
           {"sw": 1537, "emp": 8},
       )

---

Таблица EMPLOYEE
----------------

Справочник сотрудников. Интеграции **не должны создавать** новых сотрудников
самостоятельно — ведение справочника ручное, через UI АвтоДилера. Ищи
существующих по ``fullname`` / ``firstname+lastname`` / внешним признакам
и пропусти работу без привязки, если не нашёл.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Поле
     - Тип
     - Описание
   * - ``employee_id``
     - ``int`` PK
     - Первичный ключ
   * - ``directory_registry_id``
     - ``int`` FK
     - Аудит (``directory_registry.metatable_id = 2`` для сотрудников)
   * - ``firstname``
     - ``str(30)``
     - Имя
   * - ``middlename``
     - ``str(30)``
     - Отчество
   * - ``lastname``
     - ``str(30)``
     - Фамилия
   * - ``fullname``
     - ``str(92)``
     - Полное имя («Фамилия Имя Отчество»)
   * - ``shortname``
     - ``str(94)``
     - Сокращённое («Фамилия И. О.»)
   * - ``birth``
     - ``date``
     - Дата рождения
   * - ``sex``
     - ``int``
     - 1=муж, 2=жен
   * - ``hidden``
     - ``int``
     - 0=активен, 1=уволен/скрыт
   * - ``bar_code``
     - ``str(100)``
     - Штрих-код / внешний идентификатор (часто используется для
       маппинга с внешними системами — можно положить сюда
       ``rw:<rw_employee_id>``)
   * - ``inn``
     - ``str(15)``
     - ИНН
   * - ``photo`` / ``signature``
     - ``bytes``
     - Фото и подпись (blob), для отчётов
   * - ``extention_number``
     - ``int``
     - Внутренний номер АТС

.. code-block:: python

   from autodealer.domain.employee import Employee

   # поиск по полному имени
   emp = Employee.objects.filter(fullname="Винокуров Антон Юрьевич", hidden=0).first()

   # все активные сотрудники
   employees = Employee.objects.filter(hidden=0).order_by("fullname").all()

---

VIEW EXECUTOR
-------------

Денормализованное представление, собирает ``brigade_structure`` +
``employee`` (для штатных) или ``provider`` + ``client`` (для внешних).
Используется на чтение — например, для отображения «Исполнителя» в строке
работы без дополнительных JOIN'ов.

Исходник VIEW (упрощённо)::

   SELECT S.BRIGADE_STRUCTURE_ID, S.SERVICE_WORK_ID, S.EMPLOYEE_ID,
          IIF(S.EMPLOYEE_ID IS NULL, C.FULLNAME,  E.FULLNAME)  FULLNAME,
          IIF(S.EMPLOYEE_ID IS NULL, C.SHORTNAME, E.SHORTNAME) SHORTNAME,
          ...
     FROM brigade_structure S
     LEFT JOIN employee E ON E.employee_id = S.employee_id
     LEFT JOIN provider P
          JOIN client C ON C.client_id = P.client_id
       ON P.provider_id = S.provider_id

.. warning::

   ``executor`` не поддерживает INSERT. Писать только в ``brigade_structure``.

---

Родственные сущности
--------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Таблица
     - Назначение
   * - ``brigade_executor``
     - Именованная бригада (``brigade_executor_id`` + ``name``). Может
       ссылаться на группу исполнителей, не привязанных к конкретной работе.
   * - ``service_work_executor_view``
     - Расширенный VIEW по строке работы, содержит рассчитанные суммы
       вознаграждения исполнителя (``executor_summ``,
       ``profit_work_executor``) и процент скидки.
   * - ``document_planning_executor``
     - Исполнитель в планировании (ещё не выполненная работа).
   * - ``executor_planning``
     - Парная таблица планирования.
   * - ``certificate_employee``
     - Сертификаты/допуски сотрудника.

---

Интеграция с RocketWash
-----------------------

``reservations.selected_employees`` в ``rocketwash.db`` содержит массив вида
``[{"id": 24}, ...]`` — это id сотрудника в RocketWash. Для привязки к
работе в АвтоДилере необходимо:

1. **Резолв** ``rw_employee_id → employee_id`` в АвтоДилере.
   Варианты: по совпадению ``Employee.fullname`` с ``employees.name`` из
   RocketWash, по номеру телефона через ``contact`` таблицу, или
   через ``Employee.bar_code = 'rw:<id>'`` (если заранее проставлен вручную).
2. **Создание связки** одной строкой INSERT в ``brigade_structure``.
3. **Если сотрудник не найден** — оставляем работу без исполнителя
   (парсер не имеет права создавать ``employee``; ведение справочника —
   ответственность пользователей АвтоДилера).

.. note::

   ``firebird_cw_reservation_sync.employees_json`` уже содержит raw-JSON
   из RocketWash — можно использовать как источник без перезапроса RW API.
