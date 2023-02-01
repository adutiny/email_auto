import win32com.client

scheduler = win32com.client.Dispatch("Schedule.Service")
scheduler.Connect()

task_def = scheduler.NewTask(0)

# Set a trigger to run the task every 10 seconds
trigger = task_def.Triggers.Create(4)
trigger.Repetition.Interval = "00:00:10"
trigger.Enabled = True

# Set the action to run the Python file
action = task_def.Actions.Create(0)
action.Path = "C:\\Users\\Owners\\pycharmprojects\\pythonproject\\pythonproject1\\aduautoemail\\auto_email.py"

# Save the task
task_def.RegisterTaskDefinition("RunAutoTestingPy", task_def, True, None, None, 3)