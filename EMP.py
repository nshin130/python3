class EMP:
    def __init__(self, empno, lname, fname, email, phone,
                 hdate, jonid='', sal ='', comm='', mgr='', deptid=''):
        self.__empno = empno
        self.__lname = lname
        self.__fname = fname
        self.__email = email
        self.__phone = phone
        self.__hdate = hdate
        self.__jonid = jonid
        self.__sal = sal
        self.__comm = comm
        self.__mgr = mgr
        self.__deptid = deptid

    def __str__(self):
        result = f'{self.__empno}, {self.__lname}, {self.__fname},' \
                 f' {self.__email}, {self.__phone}, {self.__hdate} '
                 # f'{self.__jonid}, {self.__sal}, {self.__comm}, ' \
                 # f'{self.__mgr}, {self.__deptid}'
        return result

    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self, empno):
        self.__empno = empno

    @property
    def lname(self):
        return self.__lname

    @empno.setter
    def lname(self, lname):
        self.__lname = lname

    @property
    def fname(self):
        return self.__fname

    @empno.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def email(self):
        return self.__email

    @empno.setter
    def email(self, email):
        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @empno.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def hdate(self):
        return self.__hdate

    @empno.setter
    def hdate(self, hdate):
        self.__hdate = hdate

    @property
    def jonid(self):
        return self.__jonid

    @empno.setter
    def jonid(self, jonid):
        self.__jonid = jonid

    @property
    def sal(self):
        return self.__sal

    @empno.setter
    def sal(self, sal):
        self.__sal = sal

    @property
    def comm(self):
        return self.__comm

    @empno.setter
    def comm(self, comm):
        self.__comm = comm

    @property
    def mgr(self):
        return self.__mgr

    @empno.setter
    def mgr(self, mgr):
        self.__empno = mgr

    @property
    def deptid(self):
        return self.__deptid

    @empno.setter
    def deptid(self, deptid):
        self.__deptid = deptid
