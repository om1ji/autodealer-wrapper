Домен: Автомобили
=================

Модели, марки, привязка авто к клиентам.

.. contents:: Содержание
   :local:
   :depth: 2

---

Схема связей
------------

.. code-block:: text

   client.directory_registry_id
       │
       └── model_link.directory_registry_link_id   ← «авто принадлежит клиенту»
               │
               └── model_link.model_detail_id ──► model_detail  (VIN, regno, specs)
                                                       │
                                                       └── model.model_id ──► mark

---

ORM-модели
----------

ModelLink
~~~~~~~~~

Таблица ``model_link`` — связь «клиент ↔ автомобиль».

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``model_link_id``
     - ``int`` PK
     - Первичный ключ; передаётся в ``create_service_order(client_car=...)``
   * - ``directory_registry_link_id``
     - ``int`` FK
     - ``directory_registry_id`` клиента-владельца
   * - ``model_detail_id``
     - ``int`` FK
     - Конкретный экземпляр автомобиля
   * - ``default_car``
     - ``int``
     - 1=основное авто клиента
   * - ``hidden``
     - ``int``
     - 0=активна

ModelDetail
~~~~~~~~~~~

Таблица ``model_detail`` — конкретный экземпляр автомобиля (VIN, номера, характеристики).

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Поле
     - Тип
     - Описание
   * - ``model_detail_id``
     - ``int`` PK
     - Первичный ключ
   * - ``model_id``
     - ``int`` FK
     - Марка + модель
   * - ``regno``
     - ``str(20)``
     - Государственный номер
   * - ``vin``
     - ``str(20)``
     - VIN-номер
   * - ``year_of_production``
     - ``date``
     - Год выпуска
   * - ``color_id``
     - ``int`` FK
     - Цвет кузова
   * - ``car_engine_type_id``
     - ``int`` FK
     - Тип двигателя
   * - ``car_gearbox_type_id``
     - ``int`` FK
     - Тип КПП
   * - ``car_body_type_id``
     - ``int`` FK
     - Тип кузова
   * - ``car_fuel_type_id``
     - ``int`` FK
     - Тип топлива
   * - ``engine_number``
     - ``str(20)``
     - Номер двигателя
   * - ``chassis``
     - ``str(20)``
     - Номер шасси
   * - ``body``
     - ``str(20)``
     - Номер кузова

Model / Mark
~~~~~~~~~~~~

Таблица ``model`` — модель автомобиля (напр. «Camry»).
Таблица ``mark`` — марка (напр. «Toyota»).

.. code-block:: python

   from autodealer.domain.mark import Mark
   from autodealer.domain.model import Model

   toyota = Mark.objects.filter(name__icontains="Toyota").first()
   camry  = Model.objects.filter(mark_id=toyota.mark_id, name="Camry").first()

Справочники типов
~~~~~~~~~~~~~~~~~

Таблицы ``car_body_type``, ``car_engine_type``, ``car_fuel_type``,
``car_gearbox_type``, ``car_brake_type`` — классификаторы автомобиля.

.. code-block:: python

   from autodealer.domain.car_body_type import CarBodyType
   types = CarBodyType.objects.all()

---

Высокоуровневые действия (``actions.client``)
----------------------------------------------

get_client_vehicles
~~~~~~~~~~~~~~~~~~~

.. function:: autodealer.actions.client.get_client_vehicles(client_id)

   Вернуть все автомобили клиента.

   :param int client_id: PK клиента.
   :returns: ``list[ModelLink]`` — пустой если авто нет.

   .. code-block:: python

      from autodealer.actions.client import get_client_vehicles

      cars = get_client_vehicles(920)
      for car in cars:
          print(car.model_link_id, car.model_detail_id, car.default_car)

      # Передать в create_service_order:
      doc_id = create_service_order(..., client_car=cars[0].model_link_id)

add_vehicle_to_client
~~~~~~~~~~~~~~~~~~~~~

.. function:: autodealer.actions.client.add_vehicle_to_client(client_id, make, model_name, *, regno=None, vin=None, year=None, color=None, default_car=False, created_by_user_id=1)

   Добавить авто клиенту по имени марки/модели. Идемпотентно по ``regno``.

   :returns: ``model_detail_id``.

   .. code-block:: python

      from autodealer.actions.client import add_vehicle_to_client

      md_id = add_vehicle_to_client(
          client_id=42,
          make="Toyota",
          model_name="Camry",
          regno="А001ВС77",
          year=2020,
          color="Белый",
          default_car=True,
      )

create_vehicle_for_client
~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: autodealer.actions.client.create_vehicle_for_client(*, client_id, model_id, vin=None, regno=None, year_of_production=None, color_id=None, car_engine_type_id=None, car_gearbox_type_id=None, car_body_type_id=None, car_fuel_type_id=None, engine_number=None, chassis=None, body=None, notes=None, default_car=False, created_by_user_id=1)

   Создать авто напрямую через ``model_id`` (если марка/модель уже известны).

   :returns: Экземпляр :class:`~autodealer.domain.model_link.ModelLink`.

Вспомогательные
~~~~~~~~~~~~~~~

.. function:: autodealer.actions.client.get_or_create_mark(name)

   Найти или создать марку. Возвращает ``mark_id``.

.. function:: autodealer.actions.client.get_or_create_model(mark_id, model_name)

   Найти или создать модель. Возвращает ``model_id``.

.. function:: autodealer.actions.client.get_or_create_color(name)

   Найти или создать цвет. Возвращает ``color_id`` или ``None``.

.. function:: autodealer.actions.client.find_vehicle_by_regno(regno)

   Поиск по госномеру. Возвращает ``model_detail_id`` или ``None``.

.. function:: autodealer.actions.client.find_vehicle_by_vin(vin)

   Поиск по VIN. Возвращает ``model_detail_id`` или ``None``.
