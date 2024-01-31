def load_mail() -> List[Dict[str, str]]:
    """
    Loads the mail from the json file.

    Returns:
        list: A list of dictionaries representing the mail entries.
    """
    try:
        return json.loads(thisdir.joinpath('mail_db.json').read_text())
    except FileNotFoundError:
        return []

def save_mail(mail: List[Dict[str, str]]) -> None:
    """
    Saves the mail to the json file.

    Args:
        mail (list): A list of dictionaries representing the mail entries.

    Returns:
        None
    """
    thisdir.joinpath('mail_db.json').write_text(json.dumps(mail, indent=4))

def add_mail(mail_entry: Dict[str, str]) -> str:
    """
    Adds a new mail entry to the json file.

    Args:
        mail_entry (dict): A dictionary representing the mail entry.

    Returns:
        str: The id of the new mail entry.
    """
    mail = load_mail()
    mail.append(mail_entry)
    mail_entry['id'] = str(uuid.uuid4())  # generate a unique id for the mail entry
    save_mail(mail)
    return mail_entry['id']

def delete_mail(mail_id: str) -> bool:
    """
    Deletes a mail entry from the json file.

    Args:
        mail_id (str): The id of the mail entry to delete.

    Returns:
        bool: True if the mail was deleted, False otherwise.
    """
    mail = load_mail()
    for i, entry in enumerate(mail):
        if entry['id'] == mail_id:
            mail.pop(i)
            save_mail(mail)
            return True

    return False

def get_mail(mail_id: str) -> Optional[Dict[str, str]]:
    """
    Gets a mail entry from the json file.

    Args:
        mail_id (str): The id of the mail entry to get.

    Returns:
        dict: A dictionary representing the mail entry if it exists, None otherwise.
    """
    mail = load_mail()
    for entry in mail:
        if entry['id'] == mail_id:
            return entry

    return None

def get_inbox(recipient: str) -> List[Dict[str, str]]:
    """
    Gets all mail entries for a recipient from the json file.

    Args:
        recipient (str): The recipient of the mail.

    Returns:
        list: A list of dictionaries representing the mail entries.
    """
    mail = load_mail()
    inbox = []
    for entry in mail:
        if entry['recipient'] == recipient:
            inbox.append(entry)

    return inbox

def get_sent(sender: str) -> List[Dict[str, str]]:
    """
    Gets all mail entries sent by a sender from the json file.

    Args:
        sender (str): The sender of the mail.

    Returns:
        list: A list of dictionaries representing the mail entries sent by the sender.
    """
    mail = load_mail()
    sent = []
    for entry in mail:
        if entry['sender'] == sender:
            sent.append(entry)

    return sent
