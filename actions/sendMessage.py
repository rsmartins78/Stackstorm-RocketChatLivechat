from sender.rc_livechat_sendMessage import RocketChatLiveChatMessages
from st2common.runners.base_action import Action

class RCLiveChatSendMessageAction(Action):
    def run(self, visitor_token, name, platform, username, message):
        livechat = RocketChatLiveChatMessages(api_url=self.config['api_url'],visitor_token=visitor_token,platform=platform)
        rid = livechat.create_visitor_get_room(name=name,username=username,platform=platform)
        m = livechat.send_message(rid=rid,message=message)
        return m