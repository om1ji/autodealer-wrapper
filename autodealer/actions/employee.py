"""High-level actions: employee and executor management."""

from __future__ import annotations

from sqlalchemy import text

from autodealer.connection import session_scope


def add_executor(
    service_work_id: int,
    employee_id: int,
    *,
    percent_work_party: float = 100.0,
    percent_exec_work: float = 0.0,
    tariff: float = 0.0,
) -> int:
    """Привязать исполнителя (сотрудника) к строке работы заказ-наряда.

    Создаёт запись в ``brigade_structure`` (физическая таблица связки работ
    с исполнителями; VIEW ``executor`` подтянет данные автоматически).

    Один вызов — один исполнитель. Для бригады из нескольких человек
    функцию нужно вызвать несколько раз — по одному разу на каждого.

    Идемпотентность: если пара ``(service_work_id, employee_id)`` уже
    существует, новая запись не создаётся, возвращается ``brigade_structure_id``
    существующей.

    Args:
        service_work_id: PK строки работы (``service_work.service_work_id``).
        employee_id: PK сотрудника (``employee.employee_id``).
        percent_work_party: Доля исполнителя в работе (0..100). По умолчанию
            ``100`` — один исполнитель забирает всю работу. Для бригады
            уточни политику начисления и подели между исполнителями.
        percent_exec_work: % суммы работы, идущий в ЗП исполнителю.
            По умолчанию ``0``.
        tariff: Часовая ставка. По умолчанию ``0``.

    Returns:
        ``brigade_structure_id`` записи (новой или существующей).

    Raises:
        ValueError: Если ``service_work_id`` или ``employee_id`` не найдены.

    Example::

        from autodealer.actions.employee import add_executor

        # привязать Винокурова А.Ю. (id=8) к строке работы 1537
        bs_id = add_executor(service_work_id=1537, employee_id=8)
    """
    from autodealer.domain.brigade_structure import BrigadeStructure

    with session_scope() as session:
        sw_exists = session.execute(
            text("SELECT 1 FROM service_work WHERE service_work_id = :id"),
            {"id": service_work_id},
        ).scalar()
        if not sw_exists:
            raise ValueError(
                f"service_work service_work_id={service_work_id} не найден"
            )

        emp_exists = session.execute(
            text("SELECT 1 FROM employee WHERE employee_id = :id"),
            {"id": employee_id},
        ).scalar()
        if not emp_exists:
            raise ValueError(f"employee employee_id={employee_id} не найден")

        existing = session.execute(
            text(
                "SELECT brigade_structure_id FROM brigade_structure"
                " WHERE service_work_id = :sw AND employee_id = :emp"
            ),
            {"sw": service_work_id, "emp": employee_id},
        ).scalar()
        if existing is not None:
            return existing

        bs = BrigadeStructure(
            service_work_id=service_work_id,
            employee_id=employee_id,
            percent_work_party=percent_work_party,
            percent_exec_work=percent_exec_work,
            tariff=tariff,
        )
        session.add(bs)
        session.flush()
        return bs.brigade_structure_id
