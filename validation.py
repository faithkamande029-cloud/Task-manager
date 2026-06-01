from datetime import datetime

TITLE_MIN_LENGTH = 3      # title must be at least 3 characters
TITLE_MAX_LENGTH = 100    # title can be at most 100 characters
DESCRIPTION_MAX_LENGTH = 500 

def parse_date(date_text):
    accepted_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]

    for date_format in accepted_formats:
        try:
            return datetime.strptime(date_text.strip(), date_format)
        except ValueError:
            continue
    return None

def validate_task_title(title):
    errors = []

    title = title.strip()

    while True:
        if not title:
            errors.append("Tittle cannot be empty") 
        elif len(title) < TITLE_MIN_LENGTH:
            errors.append(f"Tittle is too short. Minmum {TITLE_MIN_LENGTH} characters.")
        elif len(title) > TITLE_MAX_LENGTH:
            errors.append(f"Tittle is too long. Maximum {TITLE_MAX_LENGTH} characters.")
        else:
            errors.append("Title has invalid characters. Use only letters, numbers, and: . , ! ? - _ & ( )")

    
def validate_task_description(description):
    errors = []

    description = description.strip()

    if description == "" and description != description:
        pass

    if len(description) > DESCRIPTION_MAX_LENGTH:
        errors.append(f"Description is too long. Maximum {DESCRIPTION_MAX_LENGTH} characters")



def validate_due_date(due_date):
    errors = []

    due_date = due_date.strip()

    if not due_date:
        errors.append("Due date cannot be empty.")
        return{"is_valid": False, "value": "", "errors": errors}
    
    parsed_date = parse_date(due_date)

    if parsed_date is None:
        errors.append(
            f"'{due_date}' is not a valid date. "
            "Accepted formats: YYYY-MM-DD, DD/MM/YYYY, MM/DD/YYYY."
            )