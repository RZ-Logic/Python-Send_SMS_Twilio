import os
from typing import Iterable, Union
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")  # your Twilio number


def _get_client() -> Client:
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        raise RuntimeError(
            "Missing Twilio credentials. "
            "Set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables."
        )
    return Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_sms(
    to: Union[str, Iterable[str]],
    body: str,
    from_number: str | None = None,
) -> list[str]:
    """
    Send an SMS to one or many numbers.
    Returns list of message SIDs.
    """
    if not body:
        raise ValueError("SMS body cannot be empty.")

    from_num = from_number or TWILIO_FROM_NUMBER
    if not from_num:
        raise RuntimeError(
            "Missing from number. Set TWILIO_FROM_NUMBER env var "
            "or pass from_number explicitly."
        )

    client = _get_client()
    if isinstance(to, str):
        numbers = [to]
    else:
        numbers = list(to)

    sids: list[str] = []
    for number in numbers:
        try:
            msg = client.messages.create(
                from_=from_num,
                body=body,
                to=number,
            )
            print(f"Sent to {number}: SID={msg.sid}")
            sids.append(msg.sid)
        except TwilioRestException as e:
            # You can inspect e.code to branch on error type.[web:14]
            print(f"Failed to send to {number}: {e}")
    return sids
