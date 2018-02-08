# Hospital Assignments

class Patient(object):
    def __init__ (self, id_num, name, allergies, bed_num = None):
        self.id_num = id_num
        self.name = name
        self.allergies = allergies
        self.bed_num = bed_num

class Hospital(object):
    def __init__ (self, hos_name, capacity):
        self.hos_name = hos_name
        self.capacity = capacity
        self.patients = []
    
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print ("The hospital is full!")
        else:
            patient_info = {"ID" : patient.id_num, "Name" : patient.name, "Allergies" : patient.allergies, "Bed Number" : patient.bed_num}
            self.patients.append(patient_info)
            print ("Admitted {}, they are in bed number {}.".format(patient.name, patient.bed_num))
        return self

    def discharge(self, name):
        for paciente in self.patients:
            if paciente['Name'] == name:
                self.patients.remove(paciente)
                print ("Discharged {}! We'll see him soon enough!".format(name))

def  main ():
    p0 = Patient(000, "Patient Zero", "BS", 00)
    p1 = Patient(101, "Patient One", "Birds", 1)
    p2 = Patient(202, "Patient Two", "Dogs", 2)
    p3 = Patient(303, "Patient Three", "Cats", 3)
    p4 = Patient(404, "Patient Four", "Cows", 4)
    p5 = Patient(505, "Patient Five", "Water", 5)
    p6 = Patient(606, "Patient Six", "Earth", 6)
    p7 = Patient(707, "Patient Seven", "Sunlight", 7)
    p8 = Patient(808, "Patient Eight", "Dust", 8)
    p9 = Patient(909, "Patient Nine", "Fire", 9)
    hospital = Hospital("Best Hospital Ever", 3).admit(p0).admit(p1).admit(p2).admit(p5).discharge("Patient Zero")
main()

# END