function checkAvailability(doctorAvailability, requestedDate) {
        return doctorAvailability.includes(requestedDate);
    }
    function findMatchingDoctors(doctors, requestedDate, isEmergency) {
        const availableDoctors = [];
        if (isEmergency) {
            for (const doctor of doctors) {
                if (doctor.availability.length > 0) {
                  availableDoctors.push(doctor);
                }
            }
        } else {
            for (const doctor of doctors) {
                if (checkAvailability(doctor.availability, requestedDate)) {
                   availableDoctors.push(doctor);
                }
            }
        }
        return availableDoctors;
    }
        const doctors = [
        { name: "Dr. Fana",  specialty: "Cardiology", availability: ["05/27/2025", "05/28/2025"] },
        { name: "Dr. Daniel", specialty: "Neurology", availability: ["05/29/2025", "05/30/2025"] },
    ];
    const patient1 = { name: "Hellen", requestedDate: "05/27/2025", isEmergency: false };
    const patient2 = { name: "Jennifer", requestedDate: "05/27/2025", isEmergency: true };
    const matchingDoctorsForPatient1 = findMatchingDoctors(doctors, patient1.requestedDate, patient1.isEmergency);
    const matchingDoctorsForPatient2 = findMatchingDoctors(doctors, patient2.requestedDate, patient2.isEmergency);
    console.log(matchingDoctorsForPatient1);
    console.log(matchingDoctorsForPatient2);