family_files['mgp'] = 'https://mzh.moegirl.org.cn/api.php'
family_files['commons'] = 'https://commons.moegirl.org.cn/api.php'
family_files['enmgp'] = 'https://en.moegirl.org.cn/api.php'
mylang = 'mgp'
family = 'mgp'
# Your username here
usernames['*']['*'] = 'Lihaohong'
password_file = "user-password.py"

# Slow down the robot such that it never requests a second page within
# 'minthrottle' seconds. This can be lengthened if the server is slow,
# but never more than 'maxthrottle' seconds. However - if you are running
# more than one bot in parallel the times are lengthened.
#
# 'maxlag' is used to control the rate of server access (see below).
# Set minthrottle to non-zero to use a throttle on read access.
minthrottle = 5
maxthrottle = 20

# Slow down the robot such that it never makes a second page edit within
# 'put_throttle' seconds.
put_throttle = 20  # type: Union[int, float]

# Sometimes you want to know when a delay is inserted. If a delay is larger
# than 'noisysleep' seconds, it is logged on the screen.
noisysleep = 3.0
