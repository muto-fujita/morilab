#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Database schema (Table構成)の定義
"""

import sys
sys.path.append('./clive/db/')

from database import Table


class Exp(Table):
    def __init__(self):
        self.tablename = "exp"
        self.items = ["id",
                      "batch_id",
                      "project",
                      "plate_id",
                      "person_id",
                      "medium",
                      "conditions",
                      "h_scan",
                      "dt_start",
                      "pos_scan",
                      "mins_grow",
                      "step_done",
                      "n_death",
                      "pcc",
                      "failure",
                      "note",
                      "in_process"]


class Person(Table):
    def __init__(self):
        self.tablename = "person"
        self.items = ["id",
                      "user",
                      "passwd",
                      "name",
                      "email"]


class Batch(Table):
    def __init__(self):
        self.tablename = "batch"
        self.items = ["id",
                      "project",
                      "person_id",
                      "num_plates",
                      "pos2exp_id",
                      "dt_start",
                      "h_scan",
                      "status"]


class Imgscan(Table):
    def __init__(self):
        self.tablename = "img_scan"
        self.items = ["id",
                      "dt_scan",
                      "scanner_id",
                      "exp_ids",
                      "min_grow"]


class Scanner(Table):
    def __init__(self):
        self.tablename = "scanner"
        self.items = ["id",
                      "batch_id",
                      "person_name",
                      "dt_start",
                      "dt_finish",
                      "exp_ids",
                      "min_grows"]


class Colony(Table):
    def __init__(self):
        self.tablename = "colony"
        self.items = ["id",
                      "exp_id",
                      "col",
                      "row",
                      "location",
                      "areas",
                      "masss",
                      "cmasss"]


class Growth(Table):
    def __init__(self):
        self.tablename = "growth"
        self.items = ["id",
                      "exp_id",
                      "col",
                      "row",
                      "con",
                      "ltg",
                      "mgr",
                      "spg"]


class Ngrowth(Table):
    def __init__(self):
        self.tablename = "ngrowth"
        self.items = ["id",
                      "exp_id",
                      "col",
                      "row",
                      "con",
                      "ltg",
                      "mgr",
                      "spg"]


class PlateSet(Table):
    def __init__(self):
        self.tablename = "plate_set"
        self.items = ["id",
                      "plate1_exp_id",
                      "plate2_exp_id",
                      "plate3_exp_id",
                      "epsilon_done",
                      "sko_exp_id",
                      "conditions",
                      "medium",
                      "note"]


class KeioGeneinfo(Table):
    def __init__(self):
        self.tablename = "keio_geneinfo"
        self.items = ["id",
                      "plate",
                      "column",
                      "row",
                      "bnum",
                      "jw",
                      "gene_name"]


class Epsilon(Table):
    def __init__(self):
        self.tablename = "epsilon"
        self.items = ["id",
                      "exp_id",
                      "sko_exp_id",
                      "query_gene",
                      "target_gene",
                      "media",
                      "conv",
                      "ltg",
                      "mgr",
                      "spg"]


if __name__ == "__main__":
    pass
