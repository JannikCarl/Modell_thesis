def create_date_format(period):
    return "({0}) ({1})".format(period[0].strftime("%Y-%m-%d %H-%M"), period[-1].strftime("%Y-%m-%d %H-%M"))