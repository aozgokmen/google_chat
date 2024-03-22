kubectl create secret generic opsgenie-secret --from-literal=OPSGENIE_API_KEY=ad2acbe3-'5ac2-43c3-8d3c-0fb5cb6e8df0'
kubectl create secret generic schedule-secret --from-literal=SCHEDULE_IDENTIFIER='420fff69-6a99-4bfa-b442-7a7931b374f9'
kubectl create secret generic google-chat-secret --from-literal=GOOGLE_CHAT_WEBHOOK_URL= 'https://chat.googleapis.com/v1/spaces/AAAA62gx8E4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4RMRAmOyLduL4dVY8kj8yhQD834mD_4X4SLbFUN3N2s'
