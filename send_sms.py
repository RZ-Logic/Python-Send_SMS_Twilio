
import sys
from sms_helper import send_sms

def main():
    if len(sys.argv) < 3:
        print("Usage: python send_sms.py <to_number> <message>. Do not include <> symbols. Follow the example")
        print("Example: python send_sms.py +14155551234 \"hello from Twilio\"")
        print("python send_sms.py \"+19059999999 +14155551234 +6471234567\" \"Group alert: Meeting at 5PM!\"")
        print("Numbers: E.164 format (+1XXXXXXXXXX), space-separated for multiples")
        sys.exit(1)

    to_number = sys.argv[1].split()
    message = " ".join(sys.argv[2:])
    send_sms(to_number, message)

if __name__ == "__main__":
    main()
