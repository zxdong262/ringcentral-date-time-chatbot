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

def botJoinPrivateChatAction(bot, groupId, user):
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
  text
):
  """
  bot got group chat message: text
  bot could send some response
  """
  print(text)
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

def userAuthSuccessAction(bot, groupId, userId):
  """
  user auth bot app to access user data success,
  bot would do something
  default: send login success message to chatgroup
  if you only have bot app, it is not needed
  """
  bot.sendMessage(groupId, {
    'text': f'![:Person]({userId}), you have successfully authorized me to access your RingCentral data!'
  })

def userAddGroupInfoAction(bot, user):
  """
  user add group and bot connect info,
  bot or user could do something about it,
  default: do nothing
  if you only have bot app, it is not needed
  """
  return

def userAuthSuccessHtml(user, conf):
  """
  user auth success, would see this html from browser
  if you only have bot app, it is not needed
  """
  return '<div style="text-align: center;font-size: 20px;border: 5px solid #08c;padding: 30px;">You have authorized the bot to access your RingCentral data! Please close this page and get back to Glip</div>'

def userEventAction(
  user,
  eventType,
  event,
  getBot
):
  """
  bot got subscribed user event,
  do something about it
  default: post to chatgroup about the event
  if you only have bot app, it is not needed
  """
  groups = user.groups
  keys = groups.keys()
  for groupId in keys:
    botId = groups[groupId]
    bot = getBot(botId)
    if bot != False and eventType != 'PostAdded':
      bot.sendMessage(groupId, {
        'text': f'![:Person]({user.id}), got event "{eventType}"'
      })
