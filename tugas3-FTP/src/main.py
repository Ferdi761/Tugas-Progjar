from ftplib import FTP
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class FtpClient:
    # TODO: Initialize FTP client object
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = int(port)
        self.ftp = FTP()

    # TODO: Connect to FTP server & login
    def connect(self):
        print('okok')
        print(type(self.port))
        print('okok')

        # self.port harus dihilangkan
        self.ftp.connect(self.host)  # connect into FTP server
        self.ftp.login(self.user, self.password) # login FTP


    # TODO: Disconnect from FTP server
    def disconnect(self):
        self.ftp.quit()

    # Soal no 1
    # Nama dan versi FTP server
    def getNameAndVersion(self):
        getNameVersion = self.ftp.getwelcome().split('\n')[0].split('-')[1] # get name and version manually
        return getNameVersion

    # Soal no 2
    # Sistem yang diemulasikan FTP server
    def getWelcomeMessage(self):
        welcome = self.ftp.getwelcome()
        return welcome
    
    # Soal no 3
    # Daftar file di FTP server
    def getListOfFiles(self):
        return self.ftp.nlst()
    
    # Soal no 4
    # Mengunggah file ke FTP server
    def uploadFile(self, filename):
        command = 'STOR ' + filename
        file = self.ftp.storbinary(command, open(filename, 'rb'))
        return file

    # Soal no 5
    # Membuat direktori
    def createDirectory(self, dirname):
        directory = self.ftp.mkd(dirname)
        return directory

    # Soal no 6
    # Direktori saat ini di FTP server
    def getCurrentDirectory(self):
        currentDir = self.ftp.pwd()
        return currentDir
    
    # Soal no 7
    # Mengganti nama direktori
    def renameDirectory(self, oldname, newname):
        newDir = self.ftp.rename(oldname, newname)
        return newDir

    # Soal no 8
    # Menghapus direktori
    def removeDirectory(self, dirname):
        rmdir = self.ftp.rmd(dirname)
        return rmdir
        

if __name__ == '__main__':
    # TODO: Read FTP server configuration from ftp.conf
    with open(os.path.join(BASE_DIR, 'ftp.conf')) as config_file:
        config = dict(line.strip().split('=') for line in config_file)

    HOST = config.get('host')
    USER = config.get('user')
    PASS = config.get('pass')
    PORT = config.get('port')

    ftp = FtpClient(HOST, USER, PASS, PORT)
    ftp.connect()

    print(ftp.getNameAndVersion())
    print(ftp.getWelcomeMessage())
    print(ftp.getListOfFiles())
    print(ftp.uploadFile('samplefile.txt'))
    print(ftp.createDirectory('test'))
    print(ftp.getCurrentDirectory())
    print(ftp.renameDirectory('test', 'test2'))
    print(ftp.removeDirectory('test2'))
