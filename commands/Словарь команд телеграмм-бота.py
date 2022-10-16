# Словарь команд телеграм бота
commands = {
    'start': {  # command_name - название команды для телеграм бота
        'command_handler': start_command,  # обработчик команды
        'description': 'Отправляет приветственное сообщение'  # описание команды
    },
    'convert_to': {
        'command_handler': convert_to_command,
        'description': "Преобразование формата хранения данных в заданный formatId. Пример использования: '/convert_to {formatId}'"
    },
    'help': {
        'command_handler': help_command,
        'description': 'Отображает список доступных команд'
    },
    'show': {
        'command_handler': show_phone_book_command, 
        'description': 'Отображает данные из телефонного справочника'
    }
}
