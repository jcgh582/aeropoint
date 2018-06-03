import logging
import subprocess

from aeropoint.helpers import write_to_file

OUTPUT_FILENAME = 'output/example.obs'

def _create_bash_command(filenames):
    bash_command = './teqc '
    for filename in filenames:
        bash_command += filename + ' '

    return bash_command

def _log_warning(stderr_):
    for message in [message_ for message_ in stderr_.decode("utf-8").split('\n') if message_ != '']:
        logging.warn(message)

def _handle_error(stderr_, exit_code):
    if exit_code:
        _log_warning(stderr_)
        raise Exception('error running bash command - exit code: {}'.format(exit_code))

    if stderr_:
        _log_warning(stderr_)

def merge(filenames):
    bash_command = _create_bash_command(filenames)
    logging.info('executing merge command {}'.format(bash_command))

    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, stderr_ = process.communicate()
    _handle_error(stderr_, process.returncode)

    write_to_file(output, OUTPUT_FILENAME)
    logging.info('successfully merged files to {}'.format(OUTPUT_FILENAME))