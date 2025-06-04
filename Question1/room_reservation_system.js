
function reservation(roomNumber,guestDetails){
    
    const reservedRooms=[20,30,40,12];
    for(room in reservedRooms){
      
        if(room!=roomNumber){
            const bookRoom={}
             bookRoom[roomNumber]= guestDetails;
        return bookRoom
       
        }
        else{
            console.log("The room is taken")
        }
       
    }
}
const reserve=reservation(20,[{name:"Fana",checkInDetails:"02-03-05"}])
console.log(reserve) 
