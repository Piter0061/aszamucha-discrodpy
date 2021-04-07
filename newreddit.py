from apscheduler.schedulers.background import BackgroundScheduler

def get_hot():
    return list(r.subreddit("hentai").hot(limit=25))

ref_hot = get_hot() # get base listing for comparison

def fn():
    now_hot = get_hot()
    for post in now_hot:
        if post not in ref_hot:
            print("New post in hot listings")
            print(post.title)
    # set ref_hot to current listings for comparison next pass
    ref_hot = now_hot

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(fn, trigger='cron', second=0)