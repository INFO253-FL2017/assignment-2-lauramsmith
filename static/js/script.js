function validateForm() {
	var contactForm= document.getElementById("contactForm");
	var subj = contactForm["subject"].value;
	var name = contactForm["name"].value;
	var message = contactForm["message"].value;
	var result = "";
	if (subj == "") {
		result += " subject";
	}
	if (name == "") {
		result += " name";
	}
	if (message == "") {
		result += " message";
	}
	var div = document.getElementById("alert");
	if (result !=""){
		div.innerHTML = "Please fill in the following fields: " + result;
		return false;
	}
	return true;
}
