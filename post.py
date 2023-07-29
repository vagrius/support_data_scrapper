import smtplib
from email.mime.text import MIMEText


def auto_mailing(date):
    msg = MIMEText(
        f'https://elma365kpi.herokuapp.com/ \n'
        f'Обновление данных в базе было выполнено {date} \n'
        f'Обновленная информация появится через несколько минут'
    )
    msg['Subject'] = 'Автоматическая рассылка с сайта 365 KPI'
    msg['From'] = 'vagrius1@gmail.com'
    msg['To'] = 'n.chudinovskikh@elma-bpm.com'

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('vagrius1@gmail.com', 'password')

    smtpObj.sendmail('vagrius1@gmail.com', msg.as_string())

    smtpObj.quit()
