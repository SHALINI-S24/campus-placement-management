drives = [
    {"id": 1, "company": "ABC Technologies", "role": "Software Developer"},
    {"id": 2, "company": "XYZ Systems", "role": "Data Analyst"},
    {"id": 3, "company": "Tech Solutions", "role": "QA Engineer"}
]

applications = []

def view_drives():
    for drive in drives:
        print(drive)

def apply_for_drive(student, drive_id):
    if any(a["student"] == student and a["drive_id"] == drive_id
           for a in applications):
        print("Already applied.")
        return

    if not any(d["id"] == drive_id for d in drives):
        print("Invalid drive.")
        return

    applications.append({
        "student": student,
        "drive_id": drive_id,
        "status": "Applied"
    })
    print("Application submitted.")

def withdraw_application(student, drive_id):
    for application in applications:
        if (application["student"] == student
                and application["drive_id"] == drive_id
                and application["status"] == "Applied"):
            application["status"] = "Withdrawn"
            print("Application withdrawn.")
            return

    print("No active application found.")

def view_status(student):
    for application in applications:
        if application["student"] == student:
            print(application)

if __name__ == "__main__":
    view_drives()
    apply_for_drive("student1", 1)
    view_status("student1")