// Windows and Linux can't use the same file path, so yeah...
if (navigator.appVersion.indexOf("Win") !== -1){
	var data_file = "https://raw.githubusercontent.com/jameeters/dygraphs-spike/master/test_data.csv";
}
else{
	var data_file = "test_data.csv";
}


g = new Dygraph(
	document.getElementById("graphdiv"),
	data_file,
	{
		showRoller: true,
		rollPeriod: 10,
		delimiter: ';',
		title: 'USGS 05406500 BLACK EARTH CREEK AT BLACK EARTH, WI',
	}
);

