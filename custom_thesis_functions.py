def create_pickle_path(contentstring, period, pickle_loc):
    date_stamp = "({0}) ({1})".format(period[0].strftime("%Y-%m-%d %H-%M"),
                                  period[-1].strftime("%Y-%m-%d %H-%M"))
    return pickle_loc + contentstring + " " + date_stamp + ".pickle"