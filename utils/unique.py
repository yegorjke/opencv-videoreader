import uuid


def generate_unique_id() -> str:
    """Generates a unique string by uuid.uuid1() function.

    Returns:
        str -- unique string
    """
    return uuid.uuid1().hex
