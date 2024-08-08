import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from vk_api import VkApi
session = VkApi(token="vk1.a.LboZWmWyx9t-MUM3STtp-kqu37-b5qzaDm01_IWPB6qBjHMpywrra9kyqpB0qhrMB_6CieKIXsBIpu1K2H-_ZBiAPmXbzgmlATfQ0kE_mQgj8ev2ZgaegXjORZeqUDSLLbN_nf8mE2E9pA3Di-kMrs2o7UFsGZtpLXqkrbrI7Dvevk4bIGQK3nbAUC06n_09VUvlZezWrkQ4oiN56iE8A")
session_api = session.get_api()
longpoll = VkLongPoll(session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f"Сообщение пришло в: {str(datetime.now())}")
            print(f"Текст сообщения: {str(event.text)}")
            responce = event.text.lower()
            if event.from_user and not event.from_me:
                if responce.find('привет')>= 0 or responce.find("здравствуй") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "И тебе привет!",
                            "random_id": 0,
                        },
                    )
                elif responce.find('как дела')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "stiker_id": 63,
                            "random_id": 0,
                        },
                    )
                elif responce.find('музыка')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "audio-2001691380_118691380",
                            "random_id": 0,
                        },
                    )
                elif responce.find('ава')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "photo855205288_457239018",
                            "random_id": 0,
                        },
                    )
                elif responce.find('видео')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "video236926726_456239116",
                            "random_id": 0,
                        },
                    ) 