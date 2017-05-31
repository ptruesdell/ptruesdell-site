function togglePGPBlock() {
	if (document.getElementById('pgpPublic').style.display == "none") {
		document.getElementById('pgpPublic').style.display = "block";
		document.getElementById('hideKeyButton').style.display = "block";
		document.getElementById('showKeyButton').style.display = "none";
	}
	else {
		document.getElementById('pgpPublic').style.display = "none";
		document.getElementById('showKeyButton').style.display = "block";
		document.getElementById('hideKeyButton').style.display = "none";
	}
	
}