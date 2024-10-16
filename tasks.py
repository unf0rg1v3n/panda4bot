# from datetime import datetime
# from celery_app import app
# import time
#
#
# # Задача, которая будет выполняться в указанное время
# @app.task
# def send_reminder(message):
#     print(f"Reminder: {message} at {datetime.now()}")
#
#
# # Функция для планирования задачи
# def schedule_reminder(reminder_time, message):
#     current_time = datetime.now()
#     delay = (reminder_time - current_time).total_seconds()
#
#     if delay > 0:
#         print(f"Reminder scheduled in {delay} seconds.")
#         # Планируем задачу через delay секунд
#         send_reminder.apply_async((message,), countdown=delay)
#     else:
#         print("The reminder time is in the past. Please enter a future time.")


# if __name__ == "__main__":
#     # Пример ввода даты и сообщения
#     reminder_time_str = input("Enter reminder time (YYYY-MM-DD HH:MM:SS): ")
#     reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M:%S")
#
#     message = input("Enter reminder message: ")
#
#     schedule_reminder(reminder_time, message)
