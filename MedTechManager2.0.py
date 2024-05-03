from datetime import datetime

patients = []
doctors = []
appointments = []
medical_records = []

# Function to validate date format
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to validate age as integer
def validate_age(age_str):
    try:
        age = int(age_str)
        if age <= 0:
            raise ValueError("Age must be a positive integer.")
        return age
    except ValueError:
        return False

# Function to add a patient
def add_patient():
    while True:
        try:
            patient_id = int(input("Enter patient ID: "))
            name = input("Enter patient name: ")
            if not isinstance(name, str):
                raise ValueError("Name must be a string.")
            age = input("Enter patient age: ")
            validated_age = validate_age(age)
            if not validated_age:
                raise ValueError("Invalid age. Please enter a valid age.")
            gender = input("Enter patient gender: ")
            if not isinstance(gender, str):
                raise ValueError("Gender must be a string.")
            contact = input("Enter patient contact number: ")
            break  # If all inputs are valid, break out of the loop
        except ValueError as e:
            print("Input error:", e)
            print("Please enter correct data.")

    patient = {
        "patient_id": patient_id,
        "name": name,
        "age": validated_age,
        "gender": gender,
        "contact": contact
    }
    patients.append(patient)
    print("Patient added successfully!")

# Function to add a doctor
def add_doctor():
    while True:
        try:
            doctor_id = int(input("Enter doctor ID: "))
            name = input("Enter doctor name: ")
            if not isinstance(name, str):
                raise ValueError("Name must be a string.")
            specialization = input("Enter doctor specialization: ")
            contact = input("Enter doctor contact number: ")
            break  # If all inputs are valid, break out of the loop
        except ValueError:
            print("Input error. Please enter correct data.")

    doctor = {
        "doctor_id": doctor_id,
        "name": name,
        "specialization": specialization,
        "contact": contact
    }
    doctors.append(doctor)
    print("Doctor added successfully!")

# Function to view patient details by ID
def view_patient_by_id(patient_id):
    for patient in patients:
        if patient["patient_id"] == patient_id:
            print("Patient ID:", patient["patient_id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Contact:", patient["contact"])
            return
    print("Patient with ID", patient_id, "not found.")

# Function to view doctor details by ID
def view_doctor_by_id(doctor_id):
    for doctor in doctors:
        if doctor["doctor_id"] == doctor_id:
            print("Doctor ID:", doctor["doctor_id"])
            print("Name:", doctor["name"])
            print("Specialization:", doctor["specialization"])
            print("Contact:", doctor["contact"])
            return
    print("Doctor with ID", doctor_id, "not found.")

# Function to view appointments by patient ID
def view_appointments_by_patient_id(patient_id):
    patient_appointments = [appointment for appointment in appointments if appointment["patient_id"] == patient_id]
    if patient_appointments:
        print("Appointments for Patient ID:", patient_id)
        for appointment in patient_appointments:
            print("Appointment ID:", appointment["appointment_id"])
            print("Doctor ID:", appointment["doctor_id"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            print()
    else:
        print("No appointments found for Patient ID:", patient_id)

# Function to view medical records by patient ID
def view_medical_records_by_patient_id(patient_id):
    patient_records = [record for record in medical_records if record["patient_id"] == patient_id]
    if patient_records:
        print("Medical Records for Patient ID:", patient_id)
        for record in patient_records:
            print("Record ID:", record["record_id"])
            print("Doctor ID:", record["doctor_id"])
            print("Diagnosis:", record["diagnosis"])
            print("Prescription:", record["prescription"])
            print()
    else:
        print("No medical records found for Patient ID:", patient_id)

# Function to schedule an appointment
def schedule_appointment():
    while True:
        try:
            appointment_id = int(input("Enter appointment ID: "))
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            if not validate_date(date):
                raise ValueError("Invalid date format. Please enter date in YYYY-MM-DD format.")
            time = input("Enter appointment time: ")
            break  # If all inputs are valid, break out of the loop
        except ValueError as e:
            print("Input error:", e)
            print("Please enter correct data.")

    appointment = {
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }
    appointments.append(appointment)
    print("Appointment scheduled successfully!")

# Function to create a medical record
def create_medical_record():
    while True:
        try:
            record_id = int(input("Enter medical record ID: "))
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            diagnosis = input("Enter diagnosis: ")
            prescription = input("Enter prescription details: ")
            break  # If all inputs are valid, break out of the loop
        except ValueError:
            print("Input error. Please enter correct data.")

    medical_record = {
        "record_id": record_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": diagnosis,
        "prescription": prescription
    }
    medical_records.append(medical_record)
    print("Medical record created successfully!")

# Function to cancel an appointment
def cancel_appointment(appointment_id):
    global appointments
    appointments = [appointment for appointment in appointments if appointment["appointment_id"] != appointment_id]
    print("Appointment with ID", appointment_id, "cancelled successfully.")

# Function to update a medical record
def update_medical_record(record_id, new_diagnosis, new_prescription):
    for record in medical_records:
        if record["record_id"] == record_id:
            record["diagnosis"] = new_diagnosis
            record["prescription"] = new_prescription
            print("Medical record with ID", record_id, "updated successfully.")
            return
    print("Medical record ID not found.")

# Function to display all records
def display_all_records():
    print("\nPatients:")
    for patient in patients:
        print("Patient ID:", patient["patient_id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Contact:", patient["contact"])
        print()

    print("\nDoctors:")
    for doctor in doctors:
        print("Doctor ID:", doctor["doctor_id"])
        print("Name:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Contact:", doctor["contact"])
        print()

    print("\nAppointments:")
    for appointment in appointments:
        print("Appointment ID:", appointment["appointment_id"])
        print("Patient ID:", appointment["patient_id"])
        print("Doctor ID:", appointment["doctor_id"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print()

    print("\nMedical Records:")
    for record in medical_records:
        print("Record ID:", record["record_id"])
        print("Patient ID:", record["patient_id"])
        print("Doctor ID:", record["doctor_id"])
        print("Diagnosis:", record["diagnosis"])
        print("Prescription:", record["prescription"])
        print()

# Menu loop
while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. View Patient by ID")
    print("4. View Doctor by ID")
    print("5. View Appointments by Patient ID")
    print("6. View Medical Records by Patient ID")
    print("7. Schedule Appointment")
    print("8. Create Medical Record")
    print("9. Cancel Appointment")
    print("10. Update Medical Record")
    print("11. Display All Records")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        patient_id = int(input("Enter patient ID: "))
        view_patient_by_id(patient_id)
    elif choice == "4":
        doctor_id = int(input("Enter doctor ID: "))
        view_doctor_by_id(doctor_id)
    elif choice == "5":
        patient_id = int(input("Enter patient ID: "))
        view_appointments_by_patient_id(patient_id)
    elif choice == "6":
        patient_id = int(input("Enter patient ID: "))
        view_medical_records_by_patient_id(patient_id)
    elif choice == "7":
        schedule_appointment()
    elif choice == "8":
        create_medical_record()
    elif choice == "9":
        appointment_id = int(input("Enter appointment ID to cancel: "))
        cancel_appointment(appointment_id)
    elif choice == "10":
        record_id = int(input("Enter medical record ID to update: "))
        new_diagnosis = input("Enter new diagnosis: ")
        new_prescription = input("Enter new prescription details: ")
        update_medical_record(record_id, new_diagnosis, new_prescription)
    elif choice == "11":
        display_all_records()
    elif choice == "12":
        break
    else:
        print("Invalid choice. Please try again.")

# Displaying data
print("\nAll Records:")
display_all_records()
