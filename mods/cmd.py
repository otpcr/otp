# This file is placed in the Public Domain.


"availalbe commands."


from otp.command import Commands
from otp.object    import keys


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(keys(Commands.cmds))))
