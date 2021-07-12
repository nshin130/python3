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

    @lname.setter
    def lname(self, lname):
        self.__lname = lname

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def hdate(self):
        return self.__hdate

    @hdate.setter
    def hdate(self, hdate):
        self.__hdate = hdate

    @property
    def joinid(self):
        return self.__joinid

    @joinid.setter
    def joinid(self, joinid):
        self.__joinid = joinid

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self, sal):
        self.__sal = sal

    @property
    def comm(self):
        return self.__comm

    @comm.setter
    def comm(self, comm):
        self.__comm = comm

    @property
    def mgr(self):
        return self.__mgr

    @mgr.setter
    def mgr(self, mgr):
        self.__empno = mgr

    @property
    def deptid(self):
        return self.__deptid

    @deptid.setter
    def deptid(self, deptid):
        self.__deptid = deptid
