#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 15:21:12 2025

@author: alexandermikhailov
"""

import io

from config import DATA_DIR, FILE_NAME
import pandas as pd


def make_dataset() -> pd.DataFrame:
    with (
        DATA_DIR
        .joinpath('raw')
        .joinpath(FILE_NAME)
        .open(encoding='ascii')
    ) as f:
        df = pd.read_json(io.StringIO(f.read()), lines=True)

    columns = ['file', 'category', 'vessel', 'imo', 'date']
    return df.dropna(subset=columns)
