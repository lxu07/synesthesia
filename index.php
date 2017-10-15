<!DOCTYPE html>

<html>

<head>
<title>Synesthesia</title>
<link rel="stylesheet" type="text/css" href="synstyle.css">
<link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet'>
</head>

<body>
<div id = "header">
	<a href = "https://google.com"><img src="logosilence.png" alt="Synethesia" width="330" height="100"></a>
</div>

<form action="index.html" method="get">
	<h3>Enter the start time, end time, and interval.</h3>
	<div id="questions">
		Start Day (MM/DD/YYYY): <input type="date" name="startDayText" min="1970-01-01" required="true"><br>
		Start Time (HH:MM AM/PM): <input type="time" name="startTimeText" required="true"><br>
		End Day (MM/DD/YYYY): <input type="date" name="endDayText" min="1970-01-01" required="true"><br>
		End Time (HH:MM AM/PM): <input type="time" name="endTimeText" required="true"><br>
		Interval (Hrs): <input type="number" name="intervalText" min="1" required="true"><br>
	</div>
	<h3>Choose the type of data to be visualized.</h3>
	<div id="checkboxes">
		<input type="checkbox" name="option1"> Temperature<br>
		<input type="checkbox" name="option2"> Pedestrian Flow<br>
		<input type="checkbox" name="option3"> Pressure<br>
		<input type="checkbox" name="option4"> Humidity<br>
		<input type="checkbox" name="option5"> Traffic<br>
		<input type="checkbox" name="option5"> Audio Level<br><br>
	</div>

	<input type="submit" value="Submit" onclick="">
	<input type="reset">
</form>
	<div><a href = "map.html"><button>Let's map it!</button></a></div>

</body>

<script>
</script>


</html>