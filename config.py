import json
import os

class Config:
    def __init__(self, json_file='config.json'):
        self.json_file = json_file
        self._load_from_json()

    def _load_from_json(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                data = json.load(f)
                self.TWITTER_API_KEY = data.get('TWITTER_API_KEY', '')
                self.TWITTER_API_SECRET = data.get('TWITTER_API_SECRET', '')
                self.TWITTER_ACCESS_TOKEN = data.get('TWITTER_ACCESS_TOKEN', '')
                self.TWITTER_ACCESS_TOKEN_SECRET = data.get('TWITTER_ACCESS_TOKEN_SECRET', '')
                self.OPENAI_API_KEY = data.get('OPENAI_API_KEY', '')
                self.prompt = data.get('PROMPT', "")
                self.persona = data.get('PERSONA', "witty, cool")
                self.use_behaviour = data.get('USE_BEHAVIOUR', "1 or 2 emojis")
                self.avoid_behaviour = data.get('AVOID_BEHAVIOUR', "repeating things similar to previous replies")
                self.use_history_context_option = int(data.get('USE_HISTORY_CONTEXT_OPTION', 1))
                self.schedule_frequency = data.get('SCHEDULE_FREQUENCY', 'daily')
                self.schedule_day = data.get('SCHEDULE_DAY', 'MON')
                self.schedule_time = data.get('SCHEDULE_TIME', '9:00')
                self.exe_in_root = data.get('EXE_IN_ROOT', 'False') == 'True'
        else:
            self._set_default_values()

    def _set_default_values(self):
        default_config = {
            'TWITTER_API_KEY': '',
            'TWITTER_API_SECRET': '',
            'TWITTER_ACCESS_TOKEN': '',
            'TWITTER_ACCESS_TOKEN_SECRET': '',
            'OPENAI_API_KEY': '',
            'PROMPT': "Say a fun fact",
            'PERSONA': "not robotic",
            'USE_BEHAVIOUR': "friendly, maybe an emoji or 2",
            'AVOID_BEHAVIOUR': "sounding robotic",
            'USE_HISTORY_CONTEXT_OPTION': 1,
            'SCHEDULE_FREQUENCY': 'daily',
            'SCHEDULE_DAY': 'MON',
            'SCHEDULE_TIME': '9:00',
            'EXE_IN_ROOT': "True"
        }
        with open(self.json_file, 'w') as f:
            json.dump(default_config, f, indent=4)
        self._load_from_json()

    def update_json(self, **kwargs):
        with open(self.json_file, 'r') as f:
            data = json.load(f)

        for key, value in kwargs.items():
            if key in data:
                data[key] = value
                setattr(self, key, value)

        with open(self.json_file, 'w') as f:
            json.dump(data, f, indent=4)
