import uuid


def generate_uuid():
    with open("client_id.txt", "x") as f:
        f.write(str(uuid.uuid4()))
    return f


def get_uuid():
    try:
        f = open("client_id.txt", "r")
    except FileExistsError or FileNotFoundError:
        f = generate_uuid()
    return f.read()
