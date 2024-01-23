import requests
from bs4 import BeautifulSoup


class WebScraperPromedio:
    def __init__(self, url):
        self.url = url
        self.date_input_id = "ctl00_cphContent_rdpDate_dateInput"
        self.dolar_id = "ctl00_cphContent_rgTipoCambio_ctl00__0"
        self.euro_id = "ctl00_cphContent_rgTipoCambio_ctl00__7"

        response = requests.get(self.url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def scrape_date(self):
        try:
            date_input = self.soup.find('input', {'id': self.date_input_id})

            if date_input:
                date_value = date_input.get('value')
                return date_value
            else:
                return "Date input not found on the page."

        except requests.RequestException as e:
            return f"Error during web scraping: {e}"

    def scrape_dolar(self):
        return self._scrape_currency(self.dolar_id)

    def scrape_euro(self):
        return self._scrape_currency(self.euro_id)

    def _scrape_currency(self, currency_id):
        try:
            currency_row = self.soup.find('tr', {'id': currency_id})

            if currency_row:
                #currency_name = currency_row.find('td', {'class': 'APLI_fila3'}).text.strip()
                buy_rate = currency_row.find_all('td', {'class': 'APLI_fila2'})[0].text.strip()
                #sell_rate = currency_row.find_all('td', {'class': 'APLI_fila2'})[1].text.strip()
                return buy_rate
            else:
                return f"Currency with ID {currency_id} not found on the page."

        except requests.RequestException as e:
            return f"Error during web scraping: {e}"


class WebScraperContable:
    def __init__(self, url):
        self.url = url
        self.date_input_id = "ctl00_cphContent_rdpDate_dateInput"
        self.dolar_id_australiano = "ctl00_cphContent_rgTipoCambio_ctl00__2"
        self.dolar_id_boliviano = "ctl00_cphContent_rgTipoCambio_ctl00__4"
        self.dolar_id_canadiense = "ctl00_cphContent_rgTipoCambio_ctl00__7"
        self.dolar_id_franco_suizo = "ctl00_cphContent_rgTipoCambio_ctl00__36"
        self.dolar_id_peso_chileno = "ctl00_cphContent_rgTipoCambio_ctl00__8"
        self.dolar_id_yuan = "ctl00_cphContent_rgTipoCambio_ctl00__9"
        self.dolar_id_peso_colombiano = "ctl00_cphContent_rgTipoCambio_ctl00__11"
        self.dolar_id_corona_danesa = "ctl00_cphContent_rgTipoCambio_ctl00__14"
        self.dolar_id_libra_esterlina = "ctl00_cphContent_rgTipoCambio_ctl00__33"
        self.dolar_id_quetzal = "ctl00_cphContent_rgTipoCambio_ctl00__20"
        self.dolar_id_yen_japones = "ctl00_cphContent_rgTipoCambio_ctl00__24"
        self.dolar_id_peso_mexicano = "ctl00_cphContent_rgTipoCambio_ctl00__26"
        self.dolar_id_corona_noruega = "ctl00_cphContent_rgTipoCambio_ctl00__29"
        self.dolar_id_balboa = "ctl00_cphContent_rgTipoCambio_ctl00__30"
        self.dolar_id_corona_sueca = "ctl00_cphContent_rgTipoCambio_ctl00__35"

        response = requests.get(self.url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def scrape_date(self):
        try:
            date_input = self.soup.find('input', {'id': self.date_input_id})

            if date_input:
                date_value = date_input.get('value')
                return date_value
            else:
                return "Date input not found on the page."

        except requests.RequestException as e:
            return f"Error during web scraping: {e}"

    def scrape_dolar_australiano(self):
        return self._scrape_currency(self.dolar_id_australiano)

    def scrape_dolar_boliviano(self):
        return self._scrape_currency(self.dolar_id_boliviano)

    def scrape_dolar_canadiense(self):
        return self._scrape_currency(self.dolar_id_canadiense)

    def scrape_dolar_franco_suizo(self):
        return self._scrape_currency(self.dolar_id_franco_suizo)

    def scrape_dolar_peso_chileno(self):
        return self._scrape_currency(self.dolar_id_peso_chileno)

    def scrape_dolar_yuan(self):
        return self._scrape_currency(self.dolar_id_yuan)

    def scrape_dolar_peso_colombiano(self):
        return self._scrape_currency(self.dolar_id_peso_colombiano)

    def scrape_dolar_corona_danesa(self):
        return self._scrape_currency(self.dolar_id_corona_danesa)

    def scrape_dolar_libra_esterlina(self):
        return self._scrape_currency(self.dolar_id_libra_esterlina)

    def scrape_dolar_quetzal(self):
        return self._scrape_currency(self.dolar_id_quetzal)

    def scrape_dolar_yen_japones(self):
        return self._scrape_currency(self.dolar_id_yen_japones)

    def scrape_dolar_peso_mexicano(self):
        return self._scrape_currency(self.dolar_id_peso_mexicano)

    def scrape_dolar_corona_noruega(self):
        return self._scrape_currency(self.dolar_id_corona_noruega)

    def scrape_dolar_balboa(self):
        return self._scrape_currency(self.dolar_id_balboa)

    def scrape_dolar_corona_sueca(self):
        return self._scrape_currency(self.dolar_id_corona_sueca)

    def _scrape_currency(self, currency_id):
        try:
            currency_row = self.soup.find('tr', {'id': currency_id})

            if currency_row:
                #currency_name = currency_row.find_all('td', {'class': 'APLI_fila3'})[0].text.strip()
                #currency_description = currency_row.find_all('td', {'class': 'APLI_fila2'})[0].text.strip()
                rate = currency_row.find_all('td', {'class': 'APLI_fila2'})[1].text.strip()
                
                return rate
            else:
                return f"Currency with ID {currency_id} not found on the page."

        except requests.RequestException as e:
            return f"Error during web scraping: {e}"



