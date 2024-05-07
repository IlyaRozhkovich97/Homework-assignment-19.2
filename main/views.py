from django.shortcuts import render


# http://127.0.0.1:8000 - ссылка для перехода
# Обработка запросов на главную страницу
def home_page(request):
    # Проверяем, был ли отправлен POST-запрос
    if request.method == "POST":
        # Если запрос методом POST, извлекаем данные из формы
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Выводим данные в консоль
        print(
            f"\nСообщение из формы заказа:\n\033[91mИмя пользователя:\033[0m {name}\n\033[91mЭлектронная почта:"
            f"\033[0m {email}\n\033[91mТелефон:\033[0m {phone}\n\033[91mСообщение:\033[0m {message} ")
    # Возвращаем HTML-шаблон страницы home_page.html
    return render(request, 'main/home_page.html')


# http://127.0.0.1:8000/contacts - ссылка для перехода
# Обработка запросов на страницу контактов
def contacts(request):
    # Проверяем, был ли отправлен POST-запрос
    if request.method == "POST":
        # Если запрос методом POST, извлекаем данные из формы
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Выводим данные в консоль
        print(
            f"\nСообщение из формы обратной связи:\n\033[91mИмя пользователя:\033[0m {name}\n\033[91mЭлектронная почта:"
            f"\033[0m {email}\n\033[91mТелефон:\033[0m {phone}\n\033[91mСообщение:\033[0m {message} ")
    # Возвращаем HTML-шаблон страницы contacts.html
    return render(request, 'main/contacts.html')
