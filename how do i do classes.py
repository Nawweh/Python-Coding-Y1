class lecturer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname



    def get_full_name(self):
        self.fullname = self.firstname+self.lastname
        return self.fullname




class session:
    def __init__(self, room, time, Lecturer):
        self.room = room
        self.time = time
        self.Lecturer = Lecturer



    def register(self):
        self.register = self.room + " " + self.time + " " +self.Lecturer
        return self.register




class course:
    def __init__(self):
        self.students=["Bob","Lob","Glob","Some","Guy"]




class Timetable():
    def __init__(self, name, session1, session2, session3):
        self.name=name
        self.sessions=[session1, session2, session3]





def main():
    lecturer1 = lecturer("Olly","Bolly")
    lecturer2 = lecturer("Kate","Late")
    lecturer3 = lecturer("Simon","Jones")

    bob_science = session("G303","9:00","Olly")
    how_to_eat = session("T102","9:00","Hi")
    God = session("Heaven","9:00","God")
    

    print("lecturer 1 =",lecturer1.get_full_name())

    print("lecturer 2 =",lecturer2.get_full_name())

    print("lecturer 3 =",lecturer3.get_full_name())

    print(Timetable("P",God, how_to_eat, bob_science))

main()