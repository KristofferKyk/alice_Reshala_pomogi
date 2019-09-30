import json


class AliceRequest(object):
    def __init__(self, request_dict):
        self._request_dict = request_dict

    @property
    def version(self):
        return self._request_dict['version']

    @property
    def original_utterance(self):
        return self._request_dict['request']['original_utterance']

    @property
    def session(self):
        return self._request_dict['session']

    @property
    def markup(self):
        return self._request_dict['request']['markup']

    @property
    def danger(self):
        return self.markup['dangerous_context']
    
    @property
    def user_id(self):
        return self.session['user_id']

    @property
    def is_new_session(self):
        return bool(self.session['new'])
    
    @property
    def command(self):
        return self._request_dict['request']['command']

    @property
    def nlu(self):
        return self._request_dict['request']['nlu']

    @property
    def tokens(self):
        return self.nlu['tokens']
    
    def __str__(self):
        return str(self._request_dict)
    

class AliceResponse(object):
    def __init__(self, alice_request):
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "end_session": False
            }
        }
        

    def dumps(self):
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2
        )

    def set_text(self, text):
        self._response_dict['response']['text'] = text[:1024]

    def set_buttons(self, buttons):
        self._response_dict['response']['buttons'] = buttons

    def end(self,flag):
        self._response_dict["response"]["end_session"] = flag

    def set_tts(self, tts):
        self._response_dict['response']['tts']=tts[:1024]

    def __str__(self):
        return self.dumps()
