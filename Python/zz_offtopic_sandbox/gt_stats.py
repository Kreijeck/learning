"""
Author: Andreas Finkler
Created: 10.01.2021
"""
from datetime import datetime

from granturismo_stats import api
import os

week_number = datetime.now().isocalendar()[1]
save_folder = "daily"
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

for mode in (api.SportsMode.DAILY_A, api.SportsMode.DAILY_B, api.SportsMode.DAILY_C):
    event_details = api.get_event_details(mode)
    json_file = f"event_details_daily{mode.value}_week{week_number}.json"
    csv_file = f"leaderboard_daily{mode.value}_week{week_number}.csv"

    event_details.dump_json(os.path.join(save_folder, json_file))

    leaderboard = api.get_event_leaderboard(mode)
    leaderboard.to_csv(os.path.join(save_folder, csv_file))