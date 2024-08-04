def detetime_creator(text):
    from re import match
    from datetime import datetime

    # dd.mm hh:mm/dd hh:mm/hh:mm
    if match(r"\d{2}\.\d{2}", text):
        return datetime.strptime(text, "%d.%m %H:%M"), 1
    elif match(r"(\d{2}:\d{2})(?:/(\d{2}\.\d{2})", text):
        pass

     # (\d{2}:\d{2}))?(?:/(\d{2}:\d{2}))?'


print(detetime_creator("02.08 20:11"))
