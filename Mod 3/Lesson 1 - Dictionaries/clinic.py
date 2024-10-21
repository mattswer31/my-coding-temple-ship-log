def add_patient(patient_id, name, age):
    if patient_id not in patient_records:
        patient_records[patient_id] = {"Name" : name, "Age" : age, "Visits" : []}
        print(f"Patient {name} added with id: {patient_id}.")
    else:
        print(f"Patient {name} with id: {patient_id} already in system.")

def remove_patient(patient_id):
    if patient_id in patient_records:
        del patient_records[patient_id]
        print(f"Patient with ID: {patient_id} removed.")
    else:
        print(f"Patient ID: {patient_id} not found.")

def record_visit(patient_id, date, notes):
    if patient_id in patient_records:
        patient_records[patient_id]["Visits"].append({"Date" : date, "Notes" : notes})
        print(f"Visit on {date} recorded for patient ID: {patient_id}.")
    else:
        print(f"Patient with ID: {patient_id} not found.")

def display_patient(patient_id):
    pass

def display_patients():
    for patient_id in patient_records:
        current = patient_records[patient_id]
        print(f"Patient ID: {patient_id}\nName: {current["Name"]}\nAge: {current["Age"]}\nVisits:")
        for visit in current["Visits"]:
            print(f"    Date: {visit['Date']}, Notes: {visit['Notes']}")

patient_records = {"SVK100" : 
                  {"Name" : "Matt Song", "Age" : 28, "Visits" : 
                  [{"Date" : "10/21/24", "Notes" : "Regular Check up"}]}}
add_patient("ABC200", "Alice Bobber" , 29)
remove_patient("ABC200")
add_patient("ABC200", "Alice Bobber" , 29)
record_visit("SVK100", "11/23/24", "poopin")
display_patients()