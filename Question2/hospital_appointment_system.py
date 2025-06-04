
def check_availability(doctor: Dict, requested_date: str) -> bool:
    return requested_date in doctor["availability"]

def find_matching_doctors(doctors: List[Dict], patient: Dict) -> str:
    available_doctors = []
    if patient["is_emergency"]:
     
        for doctor in doctors:
            if len(doctor["availability"]) > 0:
                available_doctors.append(doctor)
     
        if available_doctors:
            return f"Assigned Emergency Doctor: {available_doctors[0]['name']}"
        return "No doctors available for emergency"
    else:
    
        for doctor in doctors:
            if check_availability(doctor, patient["preferred_date"]):
                available_doctors.append(doctor)
       
        if available_doctors:
            doctor_names = ", ".join(doctor["name"] for doctor in available_doctors)
            return f"Available Doctors for {patient['preferred_date']} at {patient['preferred_time']}: {doctor_names}"
        return "No doctors available for the requested time"

def main():
 
    doctors = [
        {"name": "Dr. Fana", "specialty": "Cardiology", "availability": ["05/27/2025", "05/28/2025"]},
        {"name": "Dr. Daniel", "specialty": "Neurology", "availability": ["05/29/2025", "05/30/2025"]}
    ]

    patient1 = {
        "name": "Hellen",
        "medical_need": "Heart checkup",
        "preferred_time": "10:00",
        "preferred_date": "05/27/2025",
        "appointment_duration": 30,
        "is_emergency": False
    }
    patient2 = {
        "name": "Jennifer",
        "medical_need": "Stroke",
        "preferred_time": "14:00",
        "preferred_date": "05/27/2025",
        "appointment_duration": 60,
        "is_emergency": True
    }
   
    result1 = find_matching_doctors(doctors, patient1)
    result2 = find_matching_doctors(doctors, patient2)
    print(result1)
    print(result2)
if __name__ == "__main__":
    main()









