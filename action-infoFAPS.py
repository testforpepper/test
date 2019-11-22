#!/usr/bin/env python3

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology.dialogue.intent import IntentMessage


CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


class infoFAPS(object):
    """Class used to wrap action code with mqtt connection
       Please change the name referring to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except Exception:
            self.config = None

        # start listening to MQTT
        self.start_blocking()


    @staticmethod
    def intent_1_callback(hermes: Hermes, intent_message: IntentMessage):
        # terminate the session first if not continue

        # action code goes here...
        intentname = intent_message.intent.intent_name
        if intentname == "atesfa:info":
            hermes.publish_end_session(intent_message.session_id, "Faps steht für den Lehrstuhl für Fertigungsautomatisierung und Produktionssystematik. Der Lehrstuhl wird von Herrn Professor Franke geleitet und hat Standorte in Erlangen und Nürnberg. Hier am Lehrstuhl gibt es sechs verschiedene Forschungsbereiche. Die Elektronikproduktion, den Elektromaschinenbau, die Bordnetze, Effiziente Systeme, die Hausautomatisierung und natürlich meinen Lieblingsbereich die Biomechatronik. Das ist nämlich der Bereich in dem auch ich erforscht werde.Faps steht für den Lehrstuhl für Fertigungsautomatisierung und Produktionssystematik. Der Lehrstuhl wird von Herrn Professor Franke geleitet und hat Standorte in Erlangen und Nürnberg. Hier am Lehrstuhl gibt es sechs verschiedene Forschungsbereiche. Die Elektronikproduktion, den Elektromaschinenbau, die Bordnetze, Effiziente Systeme, die Hausautomatisierung und natürlich meinen Lieblingsbereich die Biomechatronik. Das ist nämlich der Bereich in dem auch ich erforscht werde.")

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.intent_1_callback) \
            .loop_forever()


if __name__ == "__main__":
    infoFAPS()
