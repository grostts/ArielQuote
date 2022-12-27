import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from AuthorizationData import ariel_password
from AuthorizationData import ariel_login
from selenium.webdriver.common.keys import Keys

start_time = time.time()


# Using Selenium
url = 'https://account.arielcorp.com/Identity/Account/Login'

# set webdriver options
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": "C:\\Users\\hp\\GitHubProjects\\ArielQuote\\Downloads"}
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
# headless mode
# chromeOptions.headless = True
driver = webdriver.Chrome(options=chromeOptions)


def login_ariel(ariel_login, ariel_password):
    # Open and login Ariel website
    print('Login Ariel Website...', '----------------------', sep='\n')
    driver.get(url=url)
    driver.implicitly_wait(10)

    # entering a email
    print('Entering a email.')
    email_input = driver.find_element(By.ID, 'Input_UserName')
    email_input.clear()
    email_input.send_keys(ariel_login)
    driver.implicitly_wait(10)

    # entering a password
    print('Entering a password.')
    password_input = driver.find_element(By.ID, 'Input_Password')
    password_input.clear()
    password_input.send_keys(ariel_password)
    driver.implicitly_wait(10)

    # press login button
    print('Press login button.')
    login_button = driver.find_element(By.XPATH, '//button[contains(@class, "")]')
    login_button.click()

    # entering validation code
    validation_code = input('Enter a validation code: ')
    valid_code_input = driver.find_element(By.XPATH,
                                   '//input[contains(@placeholder, "Verification")]')
    valid_code_input.clear()
    valid_code_input.send_keys(validation_code)

    # press Verify Login With Code button
    code_button = driver.find_element(By.XPATH, '//button[contains(@class, "btn")]')
    code_button.click()
    print('----------------------')
    driver.implicitly_wait(40)
    time.sleep(10)
    print('')


def create_new_quote():
    # Open ariel parts page and press create new quote button
    print('Creating new quote...', '----------------------', sep='\n')
    print('Open ariel parts page.')
    driver.get(url='https://www.arielcorp.com/parts/portal/')
    driver.implicitly_wait(10)
    time.sleep(10)
    # -----------------------------------------------------------------------------------------------------------------
    print('Press create new quote button.')
    new_quote = driver.find_element(By.ID, 'button-1482-btnIconEl')
    new_quote.click()
    driver.implicitly_wait(10)
    time.sleep(3)
    # -----------------------------------------------------------------------------------------------------------------
    # Choose the shipping address
    print('Choose the shipping address.')
    # click the shipping address button, choose the shipping address, click accept button
    select_shipping_address_button = driver.find_elements(By.XPATH,
                                                          '//a[contains(@class, "x-btn x-unselectable x-box-item x-toolbar-item x-btn-blue-toolbar-small")]')
    select_shipping_address_button[1].click()
    driver.implicitly_wait(10)
    time.sleep(3)
    # -----------------------------------------------------------------------------------------------------------------
    # Find search field
    shipping_company_name = input('Enter a shipping company name: ')
    search_shipping_address = driver.find_element(By.ID,
                                                   'textfield-1663-inputEl')
    search_shipping_address.clear()
    search_shipping_address.send_keys(shipping_company_name)
    driver.implicitly_wait(15)
    time.sleep(3)
    # Choose nearest name
    choose_company_name = driver.find_elements(By.XPATH,
                                         '//td[contains(@class, "x-grid-cell x-grid-td x-grid-cell-gridcolumn-1657 x-unselectable")]')
    choose_company_name[0].click()
    # -----------------------------------------------------------------------------------------------------------------
    accept_button = driver.find_elements(By.XPATH,
                                         '//span[contains(@class, "x-btn-inner x-btn-inner-blue-toolbar-small")]')
    accept_button[5].click()
    driver.implicitly_wait(5)
    time.sleep(3)
    # -----------------------------------------------------------------------------------------------------------------
    # Fill the end user field
    print('Fill tha end user data:')
    end_user_name = input('Enter end user name: ')
    end_user = driver.find_element(By.XPATH,
                                   '//input[contains(@placeholder, "Full")]')
    end_user.send_keys(end_user_name)
    driver.implicitly_wait(20)
    # -----------------------------------------------------------------------------------------------------------------
    print('Choose the country from the list:')
    country_dict = {'A': ['Afghanistan', 'Albania', 'Algeria', 'Amer.Virgin Is.', 'Andorran', 'Angola', 'Anguilla',
                          'Antarctica', 'Antigua/Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria',
                          'Azerbaijan'],
                    'B': ['Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
                          'Bermuda', 'Bhutan', 'Blue', 'Bolivia', 'Bosnia-Herz.', 'Botswana', 'Bouvet Islands',
                          'Brazil', 'Brit.Ind.Oc.Ter', 'Brit.Virgin Is.', 'Brunei Daruss.', 'Bulgaria', 'Burkina Faso',
                          'Burma', 'Burundi'],
                    'C': ['Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'CAR', 'Cayman Islands', 'Chad', 'Chile',
                          'China', 'Christmas Islnd', 'Coconut Islands', 'Colombia', 'Comoros', 'Cook Islands',
                          'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic'],
                    'D': ['Dem. Rep. Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Rep.', 'Dutch Antilles'],
                    'E': ['East Timor', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guin', 'Eritrea',
                          'Estonia', 'Ethiopia', 'European Union'],
                    'F': ['Falkland Islnds', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'Frenc.Polynesia',
                          'French Guayana', 'French S.Territ'],
                    'G': ['Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland',
                          'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana'],
                    'H': ['Haiti', 'Heard/McDon.Isl', 'Honduras', 'Hong Kong', 'Hungary'],
                    'I': ['Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy'],
                    'J': ['Jamaica', 'Japan', 'Jordan'],
                    'K': ['Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan'],
                    'L': ['Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
                          'Luxembourg'],
                    'M': ['Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                          'Marshall Islnds', 'Martinique', 'Mauretania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia',
                          'Minor Outl.Isl.', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco',
                          'Mozambique'],
                    'N': ['N.Mariana Islnd', 'Namibia', 'NATO', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia',
                          'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Islands', 'North Korea',
                          'Norway'],
                    'O': ['Oman', 'Orange'],
                    'P': ['Pakistan', 'Palau', 'Palestine', 'Panama', 'Pap. New Guinea', 'Paraguay', 'Peru',
                          'Philippines', 'Pitcairn Islnds', 'Poland', 'Portugal', 'Puerto Rico'],
                    'Q': ['Qatar'],
                    'R': ['Rep.of Congo', 'Reunion', 'Romania', 'Russian Fed.', 'Rwanda'],
                    'S': ['S. Sandwich Ins', 'S.Tome,Principe', 'Saint Helena', 'Samoa', 'Samoa, America', 'San Marino',
                          'Saudi Arabia', 'Senegal', 'Serbia', 'Serbia/Monten.', 'Seychelles', 'Sierra Leone',
                          'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
                          'South Korea', 'Spain', 'Sri Lanka', 'St Kitts&Nevis', 'St. Lucia', 'St. Vincent',
                          'St.Pier,Miquel.', 'Sudan', 'Suriname', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland',
                          'Syria'],
                    'T': ['Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tokelau Islands', 'Tonga',
                          'Trinidad,Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turksh Caicosin', 'Tuvalu'],
                    'U': ['Uganda', 'Ukraine', 'United Kingdom', 'United Nations', 'Uruguay', 'USA', 'Utd.Arab Emir.',
                          'Uzbekistan'], 'V': ['Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam'],
                    'W': ['Wallis,Futuna', 'West Sahara'],
                    'X': [], 'Y': ['Yemen'],
                    'Z': ['Zambia', 'Zimbabwe']}
    print('----------------------')
    for key, val in country_dict.items():
        if val:
            print(key)
            print(*val)
    print('----------------------')
    # -----------------------------------------------------------------------------------------------------------------
    # enter your country name
    selected_country = input('Enter the country name: ')
    country = driver.find_element(By.XPATH,
                                  '//input[contains(@placeholder, "Please select a country")]')
    country.send_keys(selected_country)
    time.sleep(10)
    driver.implicitly_wait(5)
    country.send_keys(Keys.ENTER)
    time.sleep(10)
    driver.implicitly_wait(5)
    # # create_quote_button
    print('Press create quote button.')
    create_quote_button = driver.find_elements(By.XPATH,
                                               '//span[contains(@class, "x-btn-inner x-btn-inner-blue-toolbar-small")]')
    create_quote_button[3].click()
    driver.implicitly_wait(50)
    time.sleep(10)
    print('----------------------')
    print()


def working_with_new_quote():
    # quote menu button
    print('Working with new quote...')
    print('----------------------')
    print('Press quote menu button.')
    quote_menu_button = driver.find_element(By.XPATH, '//span[contains(text(), "Quote Menu")]')
    quote_menu_button.click()
    driver.implicitly_wait(10)
    time.sleep(10)

    # press import quote button
    print('Press import spare parts list button.')
    import_quote_button = driver.find_element(By.XPATH, '//span[contains(text(), "Import parts")]')
    import_quote_button.click()
    driver.implicitly_wait(10)

    # import spare parts list
    print('Import spare parts list.')
    file = driver.find_elements(By.XPATH, '//input[contains(@class, " x-form-file-input")]')[1]
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'ArielQuoteImportTemplate.xlsx')
    file.send_keys(file_path)
    driver.implicitly_wait(10)

    # click upload button
    print('Press upload button.')
    upload_button = driver.find_elements(By.XPATH, '//span[contains(text(), "Upload")]')
    upload_button[2].click()
    driver.implicitly_wait(10)
    time.sleep(15)

    print('Press quote menu button.')
    quote_menu_button.click()
    driver.implicitly_wait(10)
    time.sleep(5)

    print('Press replace all not for sale parts button.')
    replace_button = driver.find_element(By.XPATH, '//span[contains(text(), "Replace All Not For Sale Parts")]')
    replace_button.click()
    driver.implicitly_wait(10)
    time.sleep(5)

    print('Press confirm.')
    confirm_button = driver.find_element(By.XPATH, '//span[contains(text(), "Confirm")]')
    confirm_button.click()
    driver.implicitly_wait(10)
    time.sleep(10)

    print('Press quote menu button.')
    quote_menu_button.click()
    driver.implicitly_wait(10)
    time.sleep(5)

    print('Press export quote to excel button.')
    export_button = driver.find_element(By.XPATH, '//span[contains(text(), "Export Quote to Excel")]')
    export_button.click()
    driver.implicitly_wait(10)
    time.sleep(10)

    print('Press export.')
    confirm_button = driver.find_elements(By.XPATH, '//span[contains(text(), "Export")]')
    confirm_button[-1].click()
    driver.implicitly_wait(10)
    time.sleep(10)


try:
    login_ariel(ariel_login, ariel_password)

    create_new_quote()

    working_with_new_quote()

    print('New quote successfully downloaded!!!')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
