from ubuntu:18.04
run apt-get update && apt-get install -y xinetd libssl1.0.0 openssl libssl-dev
# only for testing
# run apt-get update && apt-get install -y netcat.openbsd wget curl nano file python

# create "ooo" user
run adduser --system --no-create-home --group ooo

# state and token are only readable by ooo user, flag is world readable
run mkdir /etc/ooobash && chown ooo:ooo /etc/ooobash && chmod 755 /etc/ooobash
copy data/state /etc/ooobash/state
copy data/token /etc/ooobash/token
copy data/flag /etc/ooobash/flag
run chmod 400 /etc/ooobash/state && chown ooo:ooo /etc/ooobash/state
run chmod 400 /etc/ooobash/token && chown ooo:ooo /etc/ooobash/token
run chmod 444 /etc/ooobash/flag && chown ooo:ooo /etc/ooobash/flag

copy ooobash.conf /etc/xinetd.d/ooobash.conf
run chmod 440 /etc/xinetd.d/ooobash.conf
copy banner_fail /

copy wrapper /opt/wrapper
run chmod 555 /opt/wrapper
copy schitzo /opt/schitzo
run chmod 555 /opt/schitzo
run chmod 551 /opt

# custom bash runs is setuid (owned by ooo user)
# it drops privileges as soon as token/state are read
# option -p is patched out
copy ooobash /bin/bash
run chown ooo:ooo /bin/bash && chmod 4755 /bin/bash

# disable /proc access
# NOTE: this doesn't work, see the "cmd" below
run chmod 550 /proc

run chmod 773 /tmp/

# TODO drop ptrace capabilities
# NOTE: it seems you can't ptrace a setuid binary...

expose 5000
# cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/etc/xinetd.d/ooobash.conf"]
cmd chmod 550 /proc && /usr/sbin/xinetd -filelog - -dontfork -f /etc/xinetd.d/ooobash.conf
