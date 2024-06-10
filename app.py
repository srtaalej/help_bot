import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.message("help")
def message_hello(message, say):
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("button_click")
def action_button_click(body, ack, respond):
    ack()
    respond(blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Click the button to open the link:"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Open Link"
                        },
                        "url": "https://slack.dev/bolt-python/tutorial/getting-started"
                    }
                ]
            }
        ]
    )
@app.action("4RfTm")
def handle_some_action(ack, body, logger):
    ack()
    logger.info(body)  

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()