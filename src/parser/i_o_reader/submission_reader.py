import re
from pprint import pprint

path = "reference_solutions\solution_9.txt"

def _file_reader(filepath) -> str:
    """This function takes a filepath to a .txt file and turns its content into a string.

    Args:
        filepath (str): path to .txt file

    Returns:
        str: .txt file content
    """
    with open(filepath, "r", encoding="utf-8") as file:
        file_content = file.read()

    return file_content.casefold()


def _task_splitter(regex, task_content) -> dict:
    """This function splits strings at a given regular expression. 
    It returns a dictionairy with the regex as keys and the strings in between as values.

    Args:
        regex (str): splitting point
        task_content (str): string one want to split

    Returns:
        dict: key = regex: value = content in between regex 
    """

    task = dict()

    task_numbers = re.split(regex, task_content)

    for i in range(1, len(task_numbers), 2):
        key = re.sub(r"\s+", "", task_numbers[i])
        value = task_numbers[i+1]
        task.update({key: value})

    return task


def submission_organizer(path) -> dict:
    """This function organizes a submission string and organizes it into the tasks and subtasks.

    Args:
        submission_content (str): whole submission as string

    Returns:
        dict: submission split in tasks and subtasks, 
        the later are dictionairies themselves.
        key = task: value = solution.
    """
    
    submission = _task_splitter(r"((?:^|\n)aufgabe\s*\d+)", _file_reader(path))

    for key in submission:
        value = submission[key]
        try:
            update = _task_splitter(r"((?:^|\n)[a-zA-Z]\)|\d+\.)" ,value)
            if len(update) == 0:
                break
            else:
                submission[key] = update
        except:
            continue

    return submission

sub = (submission_organizer(path))
pprint(sub)

