from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from pade.acl.messages import ACLMessage
from pade.behaviours.protocols import FipaRequestProtocol
from sys import argv

class ComportamentoVendedor(FipaRequestProtocol):
    def __init__(self, agent):
        super(ComportamentoVendedor, self).__init__(agent=agent, message=None, is_initiator=False)

        self.produtos = 'TV 55', 'Notebook', 'Microondas'

    def handle_request(self, message):
        super(ComportamentoVendedor, self).handle_request(message)
        display_message(self.agent.aid.localname, 'Recebi a requisição')
        resposta = message.create_reply()
        resposta.set_performative(ACLMessage.INFORM)
        resposta.set_content(self.produtos)
        self.agent.send(resposta)