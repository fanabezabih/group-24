def add_reservation(room_number,guest_name,check_in_date):
    reservations={}
    reservation_room=[20,30,21]
    for room in reservation_room:
        if(room == room_number):
            print(f"Room number {room_number}, on {check_in_date}, has a guest named {guest_name}: Booked")
            break
        else:
            print(f"{room_number}: available, you can book it")
            room-=1