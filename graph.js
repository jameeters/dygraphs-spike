if (navigator.appVersion.indexOf("Win") !== -1){
	var file = "https://raw.githubusercontent.com/jameeters/dygraphs-spike/master/test_data2.csv";
}
else{
	var file = "test_data2.csv";
}
g = new Dygraph(
	document.getElementById("graphdiv"),
	file,
	{
		showRoller: true,
		rollPeriod: 10
	}
);

