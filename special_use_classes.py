# this file i made to make and use my own classes which i will make to help me
# save time and effort

import pandas as pd
import numpy as np


class OutlierHandling:
    
    exception_list = []

    # this funciton will work on getting the iqr, lower/upper bounds from a column
    def fit_IQR(self, column: pd.Series):
        c = column.copy()

        try:
            q1 = c.quantile(1 / 4)
            q3 = c.quantile(3 / 4)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            uppoer_bound = q3 + 1.5 * iqr
            return iqr, lower_bound, uppoer_bound
        except Exception as e:
            self.exception_list.append("fit_iqr exception as :", e)
            return None

    def fit_transform_IQR(self, column: pd.series):
        c = column.copy()
        iqr, lower, upper = self.fit_IQR(c)
        c = c[(c > lower) & (c < upper)]
        return c
