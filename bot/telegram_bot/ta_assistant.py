import datetime

import requests

from bot.bot_details import token


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

    def log_time(self, chat_id):
        self.send_message(chat_id, 'Specify the task')
        last_update = self.get_last_update()
        # new_offset = last_update_id + 1
        # bot_assistant.get_updates(new_offset)
        issue_to_log = self.get_last_update()
        self.send_message(chat_id, "I'm faster")
        self.send_message(chat_id, '{}'.format(issue_to_log))


bot_assistant = BotHandler(token)
greetings = ('hi', 'hello')
bot_tasks = ('log_time', 'get_report', 'run_tests')
now = datetime.datetime.now()


def main():
    new_offset = None

    while True:
        bot_assistant.get_updates(new_offset)

        last_update = bot_assistant.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings:
            bot_assistant.send_message(last_chat_id, 'Hi, {}.\nCould you please specify where my assistance is needed'.
                                       format(last_chat_name))

        elif last_chat_text.lower() == 'log_time':
            bot_assistant.log_time(last_chat_id)

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()


# n coroutines > packaged in futures > called in while True