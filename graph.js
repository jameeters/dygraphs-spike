g = new Dygraph(
	document.getElementById("graphdiv"),
	"https://raw.githubusercontent.com/jameeters/dygraphs-spike/master/test_data2.csv",
	{
		showRoller: true,
		rollPeriod: 10
	}
);

