

def show_status(message):
    status_container = document.createElement("div")
    status_container.className = "status"
    status_container.innerText = message
    document.body.appendChild(status_container)

def submit_contact_form():
    show_status("Thanks! Your message has been sent.")

show_status("Welcome to Benjie's Music Store!")


