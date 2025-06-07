import {makeRequest} from "/frontend/utils.js";

async function loginUser(){
    const login = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const rememberMe = document.getElementById('rememberMe').checked;
    const errorAlert = document.getElementById('errorAlert');

    // Очищаем предыдущие ошибки
    errorAlert.classList.add('d-none');
    const user = await makeRequest({
        url: '/api/admin/login',
        method: "POST",
        data: {
            login,
            password
        }
    })
    // Простая валидация (в реальном проекте нужно проверять на сервере)
    if (user) {
        // Сохраняем в localStorage если выбрано "Запомнить меня"
        if (rememberMe) {
            localStorage.setItem('adminAuth', 'true');
        } else {
            sessionStorage.setItem('adminAuth', 'true');
        }

        // Перенаправляем в админ-панель
        window.location.href = '/admin_panel';
    } else {
        errorAlert.textContent = 'Неверный логин или пароль';
        errorAlert.classList.remove('d-none');
    }
}

// Проверка авторизации при загрузке (чтобы не показывать форму если уже авторизован)


window.loginUser = loginUser