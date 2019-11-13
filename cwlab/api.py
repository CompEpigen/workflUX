# collect usefull functions for external usage:
from .exec.exec import create_job, exec_runs, get_run_info, terminate_runs, \
    read_run_log, read_run_yaml, delete_job
from .general_use import get_path, get_job_ids, get_run_ids, get_job_name_from_job_id, \
    db_commit, get_job_templates, import_cwl
from . import db, app
config = app.config