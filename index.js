const addNewMeetingButton = document.querySelector(".addNewMeeting")
const newMeetingInfoDiv = document.querySelector(".newMeetingInfoBox")
addNewMeetingButton.addEventListener("click", addNewMeeting)
function addNewMeeting() {
    const header2 = document.createElement("h4")
    header2.textContent = "New Meeting Info"
    newMeetingInfoDiv.appendChild(header2);
    newMeetingInfoDiv.style.backgroundColor = "grey"
    newMeetingInfoDiv.style.width = "450px"
    newMeetingInfoDiv.style.height = "490px"
    newMeetingInfoDiv.style.borderRadius = "15px"


}