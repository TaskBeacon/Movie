from psyflow import BlockUnit,StimBank, StimUnit,SubInfo,TaskSettings,TriggerSender
from psyflow import load_config,count_down, initialize_exp, generate_balanced_conditions
import pandas as pd
from psychopy import core
import serial
from src import run_trial




# 1. Load config
cfg = load_config()

# 2. Collect subject info
subform = SubInfo(cfg['subform_config'])
subject_data = subform.collect()

# 3. Load task settings
settings = TaskSettings.from_dict(cfg['task_config'])
settings.add_subinfo(subject_data)

# 4. setup triggers
settings.triggers = cfg['trigger_config']
ser = serial.serial_for_url("loop://", baudrate=115200, timeout=1)
trigger_sender = TriggerSender(
    trigger_func=lambda code: ser.write([1, 225, 1, 0, (code)]),
    post_delay=0,
    on_trigger_start=lambda: ser.open() if not ser.is_open else None,
    on_trigger_end=lambda: ser.close()
)

# 5. Set up window & input
win, kb = initialize_exp(settings)
# 6. Setup stimulus bank
stim_bank = StimBank(win,cfg['stim_config'])\
    .convert_to_voice('instruction_text')\
    .preload_all()
# stim_bank.preview_all() 
settings.save_to_json() # save all settings to json file

StimUnit(win, 'block')\
    .add_stim(stim_bank.get('instruction_text'))\
    .add_stim(stim_bank.get('instruction_text_voice'))\
    .wait_and_continue()
count_down(win, 3)

block = BlockUnit(
        block_id=f"block_0",
        block_idx=0,
        settings=settings,
        window=win,
        keyboard=kb
    ).generate_conditions(func=generate_balanced_conditions)\
    .on_start(lambda b: trigger_sender.send(settings.triggers.get("block_onset")))\
    .on_end(lambda b: trigger_sender.send(settings.triggers.get("block_end")))\
    .run_trial(func=run_trial, stim_bank=stim_bank, trigger_sender=trigger_sender)
    
StimUnit(win, 'block').add_stim(stim_bank.get('good_bye')).wait_and_continue(terminate=True)
    
df = pd.DataFrame(block.get_dict())
df.to_csv(settings.res_file, index=False)
# 10. Close everything
core.quit()



