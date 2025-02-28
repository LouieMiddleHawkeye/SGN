# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import datetime
import os


def make_dir(dataset):
    if dataset == "NTU":
        output_dir = os.path.join("./results/NTU/")
    elif dataset == "NTU120":
        output_dir = os.path.join("./results/NTU120/")
    elif dataset == "Football":
        now = datetime.datetime.now()
        output_dir = os.path.join(f"./results/Football/{now}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    return output_dir
