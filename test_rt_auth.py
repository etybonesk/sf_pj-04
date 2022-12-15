import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings


# Автоматом запускается перед тестами для запуска браузера и открытия страницы
@pytest.fixture(autouse=True)
def testing():
    # Задаем браузер для тестов и путь к драйверу
    pytest.driver = webdriver.Chrome('D:\\books\\study\\skillfactory\\pj04\\chromedriver\\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//h1[text()="{settings.pauth_h1}"]')
        )
    )

    # Тут выполняются тесты
    yield

    # Закрывает браузер после тестов
    pytest.driver.close()
    pytest.driver.quit()


# Проверяем вход на аккаунт через почту по валидным данным
def test_pj_04_tc_001():

    # Находим и нажимаем на переключатель способа входа
    pytest.driver.find_element(By.XPATH, f'//div[text()="{settings.pr_base_email_tab}"]').click()

    # Находим и заполняем поле ввода "Электронная почта"
    pytest.driver.find_element(By.ID, 'username').send_keys(f'{settings.v_email}')

    # Находим и заполняем поле ввода "Пароль"
    pytest.driver.find_element(By.ID, 'password').send_keys(f'{settings.v_pass}')

    # Нажимаем кнопку "Войти"
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//h3[text()="{settings.lk_h3}"]')
        )
    )

    # Проверяем, что нужный заголовок существует, т.е. мы в ЛК
    assert pytest.driver.find_element(By.XPATH, f'//h3[text()="{settings.lk_h3}"]')
    print('\n')
    print("Проверяем вход на аккаунт через почту по валидным данным.")


# Проверяем вход на аккаунт через логин по валидным данным
def test_pj_04_tc_002():

    # Находим и нажимаем на переключатель способа входа
    pytest.driver.find_element(By.XPATH, f'//div[text()="{settings.pr_base_login_tab}"]').click()

    # Находим и заполняем поле ввода "Логин"
    pytest.driver.find_element(By.ID, 'username').send_keys(f'{settings.v_login}')

    # Находим и заполняем поле ввода "Пароль"
    pytest.driver.find_element(By.ID, 'password').send_keys(f'{settings.v_pass}')

    # Нажимаем кнопку "Войти"
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//h3[text()="{settings.lk_h3}"]')
        )
    )

    # Проверяем, что нужный заголовок существует, т.е. мы в ЛК
    assert pytest.driver.find_element(By.XPATH, f'//h3[text()="{settings.lk_h3}"]')
    print('\n')
    print("Проверяем вход на аккаунт через логин по валидным данным.")


# Проверяем невозможность входа не аккаунт по невалидным данным (неправильный пароль)
def test_pj_04_tc_003():

    # Находим и нажимаем на переключатель способа входа
    pytest.driver.find_element(By.XPATH, f'//div[text()="{settings.pr_base_email_tab}"]').click()

    # Находим и заполняем поле ввода "Электронная почта"
    pytest.driver.find_element(By.ID, 'username').send_keys(f'{settings.v_email}')

    # Находим и заполняем поле ввода "Пароль"
    pytest.driver.find_element(By.ID, 'password').send_keys('SSSsss13')

    # Нажимаем кнопку "Войти"
    pytest.driver.find_element(By.ID, 'kc-login').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.ID, 'form-error-message')
        )
    )

    # Проверяем, что нужный элемент видимый
    assert pytest.driver.find_element(By.ID, 'form-error-message').is_displayed()
    print('\n')
    print("Проверяем невозможность входа не аккаунт по невалидным данным (неправильный пароль).")


# Проверяем, что текст в поле ввода номера меняется в зависимости от выбранного способа входа
def test_pj_04_tc_004():

    # Берем значение по-умолчанию для последующего сравнения
    text_f_1 = pytest.driver.find_element(
        By.CSS_SELECTOR, '.rt-input-container.tabs-input-container__login > * > .rt-input__placeholder'
    ).text

    # Находим и нажимаем на переключатель способа входа
    pytest.driver.find_element(By.XPATH, f'//div[text()="{settings.pr_base_email_tab}"]').click()

    # Берем измененное значение
    text_f_2 = pytest.driver.find_element(
        By.CSS_SELECTOR, '.rt-input-container.tabs-input-container__login > * > .rt-input__placeholder'
    ).text

    # Проверяем, что в поле ввода текст по-умолчанию заменен на новый
    assert text_f_1 != text_f_2 and text_f_2 == settings.pr_base_email
    print('\n')
    print("Проверяем, что текст в поле ввода номера меняется в зависимости от выбранного способа входа.")


# Проверяем, что кнопка “Зарегистрироваться” на странице входа ведет на страницу регистрации
def test_pj_04_tc_005():
    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.NAME, 'register')
        )
    )

    # Находим заголовок "Регистрация"
    auth = pytest.driver.find_element(By.XPATH, f'//h1[text()="{settings.preg_h1}"]')

    # Проверяем, что нужный заголовок существует, т.е. мы на странице авторизации
    assert auth
    print('\n')
    print('Проверяем, что кнопка “Зарегистрироваться” на странице входа ведет на страницу регистрации.')


# Проверяем, что кнопка “Забыл пароль” на странице входа ведет на страницу восстановления пароля
def test_pj_04_tc_006():
    # Нажимаем ссылку "Забыл пароль"
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.ID, 'reset-back')
        )
    )

    # Находим заголовок "Восстановление пароля"
    auth = pytest.driver.find_element(By.XPATH, f'//h1[text()="{settings.pr_h1}"]')

    # Проверяем, что нужный заголовок существует, т.е. мы на странице восстановления пароля
    assert auth
    print('\n')
    print('Проверяем, что кнопка “Забыл пароль” на странице входа ведет на страницу восстановления пароля.')


# Проверяем появление предупреждения при некорректном заполнении поля "Имя"
def test_pj_04_tc_007():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.NAME, 'register')
        )
    )

    # Находим и заполняем поле ввода "Имя"
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('1')

    # Находим и кликаем по полю ввода "Фамилия" чтобы убрать фокус с поля "Имя"
    pytest.driver.find_element(By.NAME, 'lastName').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//input[@name="firstName"]/../../span[text()="{settings.preg_err_name}"]')
        )
    )

    # Находим предупреждение о незаполненном поле ввода
    element = pytest.driver.find_element(
        By.XPATH, f'//input[@name="firstName"]/../../span[text()="{settings.preg_err_name}"]'
    )

    # Проверяем, что нужный элемент видимый
    assert element.is_displayed()
    print('\n')
    print('Проверяем появление предупреждения при некорректном заполнении поля "Имя".')


# Проверяем появление предупреждения при некорректном заполнении поля "Фамилия"
def test_pj_04_tc_008():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.NAME, 'register')
        )
    )

    # Находим и заполняем поле ввода "Фамилия"
    pytest.driver.find_element(By.NAME, 'lastName').send_keys('1')

    # Находим и кликаем по полю ввода "Имя" чтобы убрать фокус с поля "Фамилия"
    pytest.driver.find_element(By.NAME, 'firstName').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//input[@name="lastName"]/../../span[text()="{settings.preg_err_name}"]')
        )
    )

    # Находим предупреждение о незаполненном поле ввода
    element = pytest.driver.find_element(
        By.XPATH, f'//input[@name="lastName"]/../../span[text()="{settings.preg_err_name}"]'
    )

    # Проверяем, что нужный элемент видимый
    assert element.is_displayed()
    print('\n')
    print('Проверяем появление предупреждения при некорректном заполнении поля "Фамилия".')


# Проверяем текст по-умолчанию в поле выбора региона при регистрации
def test_pj_04_tc_009():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[id="kc-register"]').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button[name="register"]')
        )
    )

    # Проверяем, что на странице есть невидимый элемент с нужным значением
    assert pytest.driver.find_element(By.CSS_SELECTOR, f'input[value="{settings.preg_in_val}"]')
    print('\n')
    print("Проверяем текст по-умолчанию в поле выбора региона при регистрации.")


# Проверяем появление предупреждения при некорректном заполнении поля "E-mail"
def test_pj_04_tc_010():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.NAME, 'register')
        )
    )

    # Находим и заполняем поле ввода "E-mail"
    pytest.driver.find_element(By.ID, 'address').send_keys('1')

    # Находим и кликаем по полю ввода "Имя" чтобы убрать фокус с поля "E-mail"
    pytest.driver.find_element(By.NAME, 'firstName').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//input[@id="address"]/../../span[text()="{settings.preg_err_email}"]')
        )
    )

    # Находим предупреждение о незаполненном поле ввода
    element = pytest.driver.find_element(
        By.XPATH, f'//input[@id="address"]/../../span[text()="{settings.preg_err_email}"]'
    )

    # Проверяем, что нужный элемент видимый
    assert element.is_displayed()
    print('\n')
    print('Проверяем появление предупреждения при некорректном заполнении поля "E-mail".')


# Проверяем появление предупреждения при некорректном заполнении поля "Пароль"
def test_pj_04_tc_011():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.NAME, 'register')
        )
    )

    # Находим и заполняем поле ввода "Пароль"
    pytest.driver.find_element(By.ID, 'password').send_keys('1')

    # Находим и кликаем по полю ввода "Имя" чтобы убрать фокус с поля "Пароль"
    pytest.driver.find_element(By.NAME, 'firstName').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//input[@id="password"]/../../span[text()="{settings.preg_err_pass}"]')
        )
    )

    # Находим предупреждение о незаполненном поле ввода
    element = pytest.driver.find_element(
        By.XPATH, f'//input[@id="password"]/../../span[text()="{settings.preg_err_pass}"]'
    )

    # Проверяем, что нужный элемент видимый
    assert element.is_displayed()
    print('\n')
    print('Проверяем появление предупреждения при некорректном заполнении поля "Пароль".')


# Проверяем появление предупреждения при несовпадении ввода в полях "Пароль" и "Подтверждение пароля"
def test_pj_04_tc_012():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.NAME, 'register')
        )
    )

    # Находим и заполняем поле ввода "Пароль"
    pytest.driver.find_element(By.ID, 'password').send_keys('SSSsss12')

    # Находим и заполняем поле ввода "Подтверждение пароля"
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('SSSsss13')

    # Проверяем, что нужный элемент видимый
    assert pytest.driver.find_element(
            By.XPATH, f'//input[@name="password-confirm"]/../../span[text()="{settings.preg_err_pass_sr}"]'
        ).is_displayed()
    print('\n')
    print('Проверяем появление предупреждения при несовпадении ввода в полях "Пароль" и "Подтверждение пароля".')


# Проверяем, что ссылка “пользовательское соглашение” на странице регистрации
# ведет на страницу с пользовательским соглашением
def test_pj_04_tc_013():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.CSS_SELECTOR, 'a[id="kc-register"]').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button[name="register"]')
        )
    )

    # Достаем адрес ссылки из тега
    str_row = pytest.driver.find_elements(By.CSS_SELECTOR, 'div.auth-policy > a')
    agree_link = ''
    for i in range(len(str_row)):
        if str_row[i].get_attribute('href') != '':
            agree_link = str_row[i].get_attribute('href')

    # Переходим по ссылке
    pytest.driver.get(agree_link)

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//li[text()="{settings.preg_po}"]')
        )
    )

    # Проверяем, что нужный заголовок существует, т.е. мы на странице соглашения
    assert pytest.driver.find_element(By.XPATH, f'//li[text()="{settings.preg_po}"]')
    print('\n')
    print('Проверяем, что ссылка “пользовательское соглашение” на странице регистрации'
          ' ведет на страницу пользовательским соглашением.')


# Проверяем невозможность регистрации при заполнении не всех полей на странице регистрации
def test_pj_04_tc_014():

    # Нажимаем ссылку "Зарегистрироваться"
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.NAME, 'register')
        )
    )

    # Находим и заполняем поле ввода "Фамилия"
    pytest.driver.find_element(By.NAME, 'lastName').send_keys('Иванов')

    # Находим и заполняем поле ввода "E-mail"
    pytest.driver.find_element(By.ID, 'address').send_keys('mail@mail.ru')

    # Находим и заполняем поле ввода "Пароль"
    pytest.driver.find_element(By.ID, 'password').send_keys('SSSsss12')

    # Находим и заполняем поле ввода "Подтверждение пароля"
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('SSSsss12')

    # Находим и нажимаем кнопку "Зарегистрироваться"
    pytest.driver.find_element(By.NAME, 'register').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//input[@name="firstName"]/../../span[text()="{settings.preg_err_name}"]')
        )
    )

    # Находим предупреждение о незаполненном поле ввода
    element = pytest.driver.find_element(
        By.XPATH, f'//input[@name="firstName"]/../../span[text()="{settings.preg_err_name}"]'
    )

    # Проверяем, что нужный элемент видимый
    assert element.is_displayed()
    print('\n')
    print('Проверяем невозможность регистрации при заполнении не всех полей на странице регистрации.')


# Проверяем, что текст в поле ввода номера меняется в зависимости от выбранного способа восстановления
def test_pj_04_tc_015():
    # Нажимаем ссылку "Забыл пароль"
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.rt-input-container.tabs-input-container__login')
        )
    )

    # Берем значение по-умолчанию для последующего сравнения
    text_f_1 = pytest.driver.find_element(
        By.CSS_SELECTOR, '.rt-input-container.tabs-input-container__login > * > .rt-input__placeholder'
    ).text

    # Находим и нажимаем на переключатель способа входа
    pytest.driver.find_element(By.XPATH, f'//div[text()="{settings.pr_base_email_tab}"]').click()

    # Берем измененное значение
    text_f_2 = pytest.driver.find_element(
        By.CSS_SELECTOR, '.rt-input-container.tabs-input-container__login > * > .rt-input__placeholder'
    ).text

    # Проверяем, что в поле ввода текст по-умолчанию заменен на новый
    assert text_f_1 != text_f_2 and text_f_2 == settings.pr_base_email
    print('\n')
    print("Проверяем, что текст в поле ввода номера меняется в зависимости от выбранного способа восстановления.")


# Проверяем, что название кнопки “Продолжить” меняется в зависимости от выбранного способа восстановления
def test_pj_04_tc_016():
    # Нажимаем ссылку "Забыл пароль"
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.rt-input-container.tabs-input-container__login')
        )
    )

    # Берем значение по-умолчанию для последующего сравнения
    text_btn_1 = pytest.driver.find_element(By.ID, 'reset').text

    # Находим и нажимаем на переключатель способа входа
    pytest.driver.find_element(By.XPATH, f'//div[text()="{settings.pr_base_email_tab}"]').click()

    # Берем измененное значение
    text_btn_2 = pytest.driver.find_element(By.ID, 'reset').text

    # Проверяем, что на кнопке текст по-умолчанию заменен на новый
    assert text_btn_1 != text_btn_2 and text_btn_2 == f'{settings.pr_btn_res_email}'
    print('\n')
    print("Проверяем, что название кнопки “Продолжить” меняется в зависимости от выбранного способа восстановления.")


# Проверяем, что поле ввода капчи на странице восстановления пароля называется "Капча"
def test_pj_04_tc_017():
    # Нажимаем ссылку "Забыл пароль"
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.rt-input-container.rt-captcha__input')
        )
    )

    # Проверяем, что в поле ввода нужный текст
    assert pytest.driver.find_element(
        By.CSS_SELECTOR, '.rt-input-container.rt-captcha__input .rt-input__placeholder'
    ).text == settings.pr_captha  # На странице текст - Символы
    print('\n')
    print('Проверяем, что поле ввода капчи на странице восстановления пароля называется "Капча".')


# Проверяем, что кнопка “Вернуться назад” на странице восстановления пароля ведет на страницу авторизации
def test_pj_04_tc_018():
    # Нажимаем ссылку "Забыл пароль"
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    # Ждем, пока прогрузится нужный элемент
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.ID, 'reset-back')
        )
    )

    # Нажимаем кнопку "Вернуться назад"
    pytest.driver.find_element(By.ID, 'reset-back').click()

    # Ждем, пока прогрузится страница
    WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//h1[text()="{settings.pauth_h1}"]')
        )
    )

    # Находим заголовок "Авторизация"
    auth = pytest.driver.find_element(By.XPATH, f'//h1[text()="{settings.pauth_h1}"]')

    # Проверяем, что нужный заголовок существует, т.е. мы на странице авторизации
    assert auth
    print('\n')
    print('Проверяем, что кнопка “Вернуться назад” на странице восстановления пароля ведет на страницу авторизации.')
