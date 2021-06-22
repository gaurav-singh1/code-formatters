import re
from datetime import datetime

import numpy as np
import pandas as pd


def date_converter(_col, cfg):
    date_formats = cfg["date_formats"]
    min_date = cfg["min_date"]
    max_date = cfg["max_date"]
    _col = _col.str.strip()

    def date_handler(dt_str):
        if dt_str is None:
            return np.nan
        dates = np.nan
        for dt_regex in date_formats.keys():
            pattern = re.compile(dt_regex)
            if pattern.match(dt_str):
                for _, dt_pattern in enumerate(date_formats[dt_regex]):
                    try:
                        print("matched regex is. = ", dt_regex)
                        converted_date = datetime.strptime(dt_str, dt_pattern)
                        if (
                            converted_date is not None
                            and converted_date.year >= min_date
                            and converted_date.year <= max_date
                        ):
                            dates = converted_date.strftime("%Y-%m-%d")
                            print(
                                "date format selected is  = ",
                                date_formats[dt_regex],
                            )
                            return dates
                    except Exception as e:
                        print("error while converting =. ", dt_pattern, str(e))
                        continue
        return dates

    converted_date = _col.apply(lambda x: date_handler(x))
    return pd.Series(converted_date)
