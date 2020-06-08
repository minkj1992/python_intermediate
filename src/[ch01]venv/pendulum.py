import pendulum
import pprint
from datetime import datetime

pst = pendulum.timezone('America/New_York')
ist = pendulum.timezone('Asia/Seoul')

# pprint.pprint(pendulum.timezones)

# 타입 출력
print(*map(type,[pst,ist]),sep=", ")

# 시간 출력
print(*map(datetime.now,[pst,ist]),sep=", ")