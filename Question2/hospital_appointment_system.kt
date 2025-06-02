fun main() {
    val hospital = Hospital()
    hospital.makeAppointment("Alice", "10:00", false)  // Normal case
    hospital.makeAppointment("Bob", "10:00", false)    // Normal case
    hospital.makeAppointment("Charlie", null, true)     // Emergency case
}
class Doctor(val name: String) {
    var availableTimes = mutableListOf("9:00", "10:00", "11:00", "14:00", "15:00")
    fun isAvailable(time: String): Boolean {
        return availableTimes.contains(time)
    }
    fun bookAppointment(time: String): Boolean {
        return if (isAvailable(time)) {
            availableTimes.remove(time)
            println("Appointment booked with Dr. $name at $time")
            true
        } else {
            println("Dr. $name is not available at $time")
            false
        }
    }
}
class Hospital {
    private val doctors = listOf(Doctor("Smith"), Doctor("Johnson"))
    fun makeAppointment(patientName: String, time: String?, isEmergency: Boolean) {
        if (isEmergency) {
            // Automatically assign the first available doctor
            for (doctor in doctors) {
                if (doctor.availableTimes.isNotEmpty()) {
                    val autoTime = doctor.availableTimes[0]
                    doctor.bookAppointment(autoTime)
                    println("$patientName has been assigned to Dr. ${doctor.name} for an emergency at $autoTime")
                    return
                }
            }
            println("No doctors available for emergency cases.")
        } else {
            // Normal case
            for (doctor in doctors) {
                if (doctor.bookAppointment(time!!)) {
                    println("$patientName has an appointment with Dr. ${doctor.name} at $time")
                    return
                }
            }
            println("No doctors available at the requested time.")
        }
    }
}






