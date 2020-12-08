from pathlib import Path
import os


def config_pruefen_und_update_remotes(path, remoteHost):
    config_path = str(path) + os.sep + "config"
    with open(config_path, "rt") as text:
        filecontent = text.read()
        filecontent = filecontent.replace("https://" + remoteHost + "/", "git@" + remoteHost + ":")
        filecontent = filecontent.replace("http://" + remoteHost + "/", "git@" + remoteHost + ":")

    with open(config_path, "wt") as writer:
        writer.write(filecontent)


if __name__ == '__main__':
    mainPfad = "/git"
    remoteHost = raw_input("zu updatender Origin (github.com/srvgit01): ")
    for path in Path(mainPfad).rglob('.git'):
        print("Verarbeite " + str(path))
        config_pruefen_und_update_remotes(path, remoteHost)
