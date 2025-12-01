def convert_gas_flow_from_std(
    flow_std: float,
    pressure_excess_mpa: float,
    temperature_oper_c: float
) -> float:
    """
    Пересчитать расход газа из стандартных условий в рабочие.


    Параметры:
        flow_std (float): Расход при стандартных условиях, м³/ч.
        pressure_excess_mpa (float): Избыточное давление, МПа.
        temperature_oper_c (float): Рабочая температура, °C.

    Возвращает:
        float: Расход при рабочих условиях, м³/ч.
    Raises:
        TypeError: Если введены не числовые значения.
        ValueError: Если входные значения некорректны.
    """
    
    # Стандартные условия (по ГОСТ)
    PRESSURE_STD_MPA = 0.101325      # МПа (абсолютное)
    TEMPERATURE_STD_K = 293.15       # К (20 °C)

    # Атмосферное давление (для перевода избыточного в абсолютное)
    ATMOSPHERIC_PRESSURE_MPA = 0.101325

    #Проверка входных данных
    if not isinstance(flow_std, (int, float)):
        raise TypeError("Введите числовое значение расхода")
    if not isinstance(pressure_excess_mpa, (int, float)):
        raise TypeError("Введите числовое значение давления")
    if not isinstance(temperature_oper_c, (int, float)):
        raise TypeError("Введите числовое значение температуры")
    if flow_std <= 0:
        raise ValueError("Расход при стандартных условиях должен быть > 0 м³/ч.")
    if pressure_excess_mpa < 0:
        raise ValueError("Избыточное давление не может быть отрицательным (МПа).")
    if temperature_oper_c < -273.15:
        raise ValueError("Температура не может быть ниже -273.15 °C.")

    try:
        # Пересчёт в абсолютное давление
        pressure_abs_mpa = pressure_excess_mpa + ATMOSPHERIC_PRESSURE_MPA

        # Пересчёт температуры в Кельвины
        temperature_oper_k = temperature_oper_c + 273.15

        # Формула пересчёта
        flow_oper = flow_std * (
            (PRESSURE_STD_MPA * temperature_oper_k) /
            (pressure_abs_mpa * TEMPERATURE_STD_K)
        )
        return flow_oper
       
    except (TypeError, ValueError) as err:
        print(err)
        

    
        






