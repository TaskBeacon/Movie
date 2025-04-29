from psyflow import TaskSettings
from psyflow import SubInfo
from psyflow import StimBank
from psyflow import BlockUnit
from psyflow import StimUnit
from psyflow import TriggerSender
from psyflow import TriggerBank
from psyflow import generate_balanced_conditions, count_down

from psychopy.visual import Window
from psychopy.hardware import keyboard
from psychopy import logging, core

from functools import partial
import yaml
import sys
import serial

from src import run_trial
import pandas as pd



# 1. Load config
with open('config/config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 2. collect subject info
subform_config = {
    'subinfo_fields': config.get('subinfo_fields', []),
    'subinfo_mapping': config.get('subinfo_mapping', {})
}

subform = SubInfo(subform_config)
subject_data = subform.collect()
if subject_data is None:
    print("Participant cancelled — aborting experiment.")
    sys.exit(0)


# 3. Load task settings
# Flatten the config
task_config = {
    **config.get('window', {}),
    **config.get('task', {}),
    **config.get('timing', {})  # ← don't forget this!
}

settings = TaskSettings.from_dict(task_config)
settings.add_subinfo(subject_data)


# 4. Set up window & input
win = Window(size=settings.size, fullscr=settings.fullscreen, screen=1,
             monitor=settings.monitor, units=settings.units, color=settings.bg_color,
             gammaErrorPolicy='ignore')
kb = keyboard.Keyboard()
logging.setDefaultClock(core.Clock())
logging.LogFile(settings.log_file, level=logging.DATA, filemode='a')
logging.console.setLevel(logging.INFO)
settings.frame_time_seconds =win.monitorFramePeriod
settings.win_fps = win.getActualFrameRate()
settings.save_path = './data'

# 5. Setup stimulus bank
stim_bank = StimBank(win)
# Preload all for safety

stim_config={
    **config.get('stimuli', {})
}
stim_bank.add_from_dict(stim_config)
stim_bank.preload_all()
# stim_bank.preview_all()
# 6. Setup trigger
trigger_config = {
    **config.get('triggers', {})
}
trigger_bank = TriggerBank(trigger_config)
ser = serial.serial_for_url("loop://", baudrate=115200, timeout=1)
trigger_sender = TriggerSender(
    trigger_func=lambda code: ser.write([1, 225, 1, 0, (code)]),
    post_delay=0,
    on_trigger_start=lambda: ser.open() if not ser.is_open else None,
    on_trigger_end=lambda: ser.close()
)

StimUnit(win, 'block').add_stim(stim_bank.get('general_instruction')).wait_and_continue()
count_down(win, 3)

block = BlockUnit(
        block_id=f"block_0",
        block_idx=0,
        settings=settings,
        window=win,
        keyboard=keyboard
    ).generate_conditions(func=generate_balanced_conditions)\
    .on_start(lambda b: trigger_sender.send(trigger_bank.get("block_onset")))\
    .on_end(lambda b: trigger_sender.send(trigger_bank.get("block_end")))\
    .run_trial(partial(run_trial, stim_bank=stim_bank, trigger_sender=trigger_sender, trigger_bank=trigger_bank))
    
StimUnit(win, 'block').add_stim(stim_bank.get('good_bye')).wait_and_continue(terminate=True)
    

df = pd.DataFrame(block.get_dict())
df.to_csv(settings.res_file, index=False)



