fun main() {
    contentReservation(23, "Fiona", "2025-05-14")
    println(reservationForRoom(23))
}

val reservations = mutableMapOf<Int, Pair<String, String>>()

fun contentReservation(roomNumber: Int, guestName: String, checkinDate: String) {
    reservations[roomNumber] = Pair(guestName, checkinDate)
}

fun reservationForRoom(roomNumber: Int): String {
    return reservations[roomNumber]?.let { "Guest: ${it.first}, Check-in: ${it.second}" }
        ?: "the room is taken"
}
