class Alumno:

    def start(self, name, grade):
        self.name = name
        self.grade = grade
    def show(self):
        print("Name: ",self.name)
        print("Grade: ", self.grade)
    def is_approve(self):
        if self.grade >= 5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")

alumno = Alumno()
alumno.start("Claudia", 10)
alumno.show()
alumno.is_approve()