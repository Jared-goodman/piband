from speech import say
import apiai

def chatbot(arg):
	CLIENT_ACCESS_TOKEN = 'f1f4bd11d9b84401aa53684d6f8833d0'

        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request = ai.text_request()

        request.lang = 'en'  # optional, default value equal 'en'

        request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

        request.query = arg

        response = request.getresponse()

        rope = str(response.read())

        rope = rope[rope.index("speech")+10:]

        rope = rope[0:rope.index("\"")]

        print rope
        say(rope)
