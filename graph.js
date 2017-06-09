g1 = new Dygraph(document.getElementById("graphdiv1"), "test_data2.csv", {});

g2 = new Dygraph(
	document.getElementById("graphdiv2"),
	"test_data2.csv",
	{
		showRoller: true,
		rollPeriod: 3
	}
);

