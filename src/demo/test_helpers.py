def check(condition, success_msg="УСПЕХ", fail_msg="ОШИБКА"):
    """
    Возвращает строку статуса со случайным эмодзи.
    
    Аргументы:
        condition (bool): Условие проверки.
        success_msg (str): Сообщение при успехе.
        fail_msg (str): Сообщение при ошибке.
        
    Возвращает:
        str: Строка вида 'Эмодзи Сообщение'.
    """
    
    return success_msg if condition else fail_msg    