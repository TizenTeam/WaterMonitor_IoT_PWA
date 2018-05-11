import arrow

utc = arrow.utcnow()
print(utc)
print(utc.to('local'))

