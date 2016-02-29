#!/usr/local/bin/expect

set username [lindex $argv 0]
set password [lindex $argv 1]
send_user "$username:$password"

spawn /home/jun/git/LinuxBackup/manual_update.sh 
expect "Username*"
send "$username\r"


expect "@github.com*"
#expect "*https://xianjunzhengbackup@github.com*"
send "$password\r"
#expect eof
interact

