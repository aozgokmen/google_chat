import requests
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
import json

load_dotenv()

def load_phone_numbers():
    with open('phone.json', 'r') as file:
        data = json.load(file)
    return data["users"]


api_key = os.getenv('OPSGENIE_API_KEY')
schedule_identifier = os.getenv('SCHEDULE_IDENTIFIER')


schedule_url_today = f'https://api.opsgenie.com/v2/schedules/{schedule_identifier}/on-calls'
users_base_url = 'https://api.opsgenie.com/v2/users/'


google_chat_webhook_url = os.getenv('GOOGLE_CHAT_WEBHOOK_URL')

def send_message_to_google_chat(webhook_url, message):
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    data = {"text": message}
    response = requests.post(webhook_url, json=data, headers=headers)
    return response.status_code

def adjust_current_time_based_on_rotation(api_key, schedule_identifier):
    url = f'https://api.opsgenie.com/v2/schedules/{schedule_identifier}/rotations'
    headers = {'Authorization': f'GenieKey {api_key}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        rotation_type = response_json['data'][0]['type']

       
        current_time = datetime.now(timezone.utc)

        if rotation_type == 'daily':
            new_time = current_time + timedelta(days=1)
        elif rotation_type == 'weekly':
            new_time = current_time + timedelta(days=7)
        elif rotation_type == 'monthly':
            new_time = current_time + timedelta(days=30)
        else:
            new_time = current_time

        formatted_new_time = new_time.strftime('%d.%m.%Y')
        return formatted_new_time
    else:
        print('Rotation API çağrısında bir hata oluştu:', response.text)
        return None

def main():
    
    phone_numbers = load_phone_numbers()

    new_time = adjust_current_time_based_on_rotation(api_key, schedule_identifier)
    current_time = datetime.now(timezone.utc).isoformat()
    
    date_obj = datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%S.%f%z')
    today_date = date_obj.strftime('%d.%m.%Y')

    headers = {'Authorization': f'GenieKey {api_key}'}
    response = requests.get(schedule_url_today, headers=headers)
    if response.status_code == 200:
        on_calls_info_today = response.json()
        user_id_today = on_calls_info_today['data']['onCallParticipants'][0]['id']

        user_info_url = f'{users_base_url}{user_id_today}'
        response_user = requests.get(user_info_url, headers=headers)
        if response_user.status_code == 200:
            user_info = response_user.json()
            full_name = user_info['data']['fullName']
            
            phone_number = next((user['phoneNumber'] for user in phone_numbers if user['fullName'] == full_name), None)

            if phone_number:

                message_to_send = f"""
                Nöbetçi kullanıcı bilgileri

                👤 İsim: {full_name}
                📞 Telefon Numarası: {phone_number}
                🗓️ Nöbet Başlangıcı: {today_date}
                🏁 Nöbet Bitişi: {new_time}    
                """
                
                send_message_to_google_chat(google_chat_webhook_url, message_to_send)
                
            else:
                print('Bugünkü nöbetçi kullanıcı bilgilerini alırken bir hata oluştu:', response_user.text)
        else:
            print('Bugünkü nöbetçi kullanıcı ID bilgisini alırken bir hata oluştu:', response.text)

if __name__ == '__main__':
    main()
