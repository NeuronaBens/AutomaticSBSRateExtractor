from datetime import datetime, timedelta

class DateServiceImp:
    def getCorrectDate(self):
        # se obtiene la fecha actual
        current_date = datetime.now()

        # se valida si es sábado o domingo y ajusta la fecha al viernes
        if current_date.weekday() == 5:  # sábado
            current_date -= timedelta(days=1)
        elif current_date.weekday() == 6:  # domingo
            current_date -= timedelta(days=2)

        # se valida si es después de las 6 p.m. y ajusta la fecha al día siguiente
        if current_date.hour < 18:
            current_date -= timedelta(days=1)

        # se formatea la fecha (DD/MM/YYYY)
        formatted_date = current_date.strftime('%d/%m/%Y')

        return formatted_date


