import sys
from subprocess import Popen, PIPE

def usage():
    docs = """
--------------
    Usage:
        $ python celebrity.py <filename.jpg>
--------------
    """
    return docs

def find_person(filename):
    """
    filename -> celebrity
    """
    if not filename:
        raise Exception("No Filename provided! %s" % usage())
    cmd = ['./OnlineFaceRec', 'single', 'testface.jpg']
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    celebrity_id = int(stdout)
    return celebrity_id

def add_person(imgpath, name):
    """
    """
    pass

def log_person(imgpath, first, last, email):
    """
    log incoming user (add to db)
    """
    pass

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    print(find_person(filename))
