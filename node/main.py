import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

linesToUpload = []


def read_lines(file, last_line_number_uploaded, next_line_number_to_upload):
    lines_in_file = file.readlines()

    number_of_lines_in_file = len(lines_in_file)
    index_of_last_line_in_file = number_of_lines_in_file - 1

    if last_line_number_uploaded == 0:
        next_line_number_to_upload = index_of_last_line_in_file

    is_next_line_number_to_upload_in_bounds = next_line_number_to_upload <= index_of_last_line_in_file

    if next_line_number_to_upload > last_line_number_uploaded and is_next_line_number_to_upload_in_bounds:
        linesToUpload.append(lines_in_file[next_line_number_to_upload])
        last_line_number_uploaded = next_line_number_to_upload
        next_line_number_to_upload = last_line_number_uploaded + 1

    return last_line_number_uploaded, next_line_number_to_upload


def read_lines_from_geth():
    geth_file_name = "C:\\Users\\richa\\a.txt"
    geth_last_line_number_uploaded = 0
    geth_next_line_number_to_upload = 0
    while True:
        geth_file = open(geth_file_name, 'r')
        geth_last_line_number_uploaded, geth_next_line_number_to_upload = read_lines(geth_file,
                                                                                     geth_last_line_number_uploaded,
                                                                                     geth_next_line_number_to_upload)
        geth_file.close()


def read_lines_from_prysm():
    prysm_file_name = "C:\\Users\\richa\\Downloads\\ethereum\\consensus\\b.txt"
    prysm_last_line_number_uploaded = 0
    prysm_next_line_number_to_upload = 0
    while True:
        prysm_file = open(prysm_file_name, 'r')
        prysm_last_line_number_uploaded, prysm_next_line_number_to_upload = read_lines(prysm_file,
                                                                                       prysm_last_line_number_uploaded,
                                                                                       prysm_next_line_number_to_upload)
        prysm_file.close()


def upload_lines_to_firebase():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate("C:\\Users\\richa\\Downloads\\geth-fyi-firebase-adminsdk-cllge-4ce5b074d2.json")

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://geth-fyi-default-rtdb.firebaseio.com'
    })

    # As an admin, the app has access to read and write all data, regardless of Security Rules
    ref = db.reference('lines')
    print(ref.get())

    while True:
        if len(linesToUpload) > 0:
            line_to_upload = linesToUpload.pop(0)
            ref.push({
                "line": line_to_upload
            })
            print(line_to_upload)


if __name__ == "__main__":
    gethFileName = "C:\\Users\\richa\\a.txt"
    prysmFileName = "C:\\Users\\richa\\Downloads\\ethereum\\consensus\\b.txt"

    t1 = threading.Thread(target=read_lines_from_geth)
    t2 = threading.Thread(target=read_lines_from_prysm)
    t3 = threading.Thread(target=upload_lines_to_firebase)
    t1.start()
    t2.start()
    t3.start()
