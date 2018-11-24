"""
sample config module
run "cp config.sample.py config.py" to create local config
edit config.py functions to override default bot behavior
"""

from datetime import datetime

__name__ = 'localConfig'
__package__ = 'ringcentral_bot_framework'

def helpMsg(botId):
  return f'''Hello, I am a date/time chatbot. Please reply "@![:Person]({botId}) **cmd**" if you want to talk to me.

**cmd** list

**date** -- show current date
**time** -- show current time
  '''

def botJoinPrivateChatAction(bot, groupId, user, dbAction):
  """
  bot join private chat event handler
  bot could send some welcome message or help, or something else
  """
  text = helpMsg(bot.id)
  bot.sendMessage(
    groupId,
    {
      'text': text
    }
  )

def botGotPostAddAction(
  bot,
  groupId,
  creatorId,
  user,
  text,
  dbAction
):
  """
  bot got group chat message: text
  bot could send some response
  """
  if text == f'![:Person]({bot.id}) date':
    date = str(datetime.now().strftime('%Y-%m-%d'))
    bot.sendMessage(
      groupId,
      {
        'text': f'![:Person]({creatorId}), current date is {date}'
      }
    )
  elif text == f'![:Person]({bot.id}) time':
    time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    bot.sendMessage(
      groupId,
      {
        'text': f'![:Person]({creatorId}), current time is {time}'
      }
    )
  elif f'![:Person]({bot.id})' in text:
    bot.sendMessage(
      groupId,
      {
        'text': helpMsg(bot.id)
      }
    )

