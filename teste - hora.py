import datetime as dt

tm = dt.datetime(2010, 6, 10, 3, 56, 23)

def time_mod(time, delta, epoch=None):
    if epoch is None:
        epoch = dt.datetime(1970, 1, 1, tzinfo=time.tzinfo)
    return (time - epoch) % delta

def time_round(time, delta, epoch=None):
    mod = time_mod(time, delta, epoch)
    if mod < (delta / 2):
       return time - mod
    return time + (delta - mod)



def main():


    print(time_round(tm, dt.timedelta(minutes=10)))

main()