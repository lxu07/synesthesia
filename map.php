<!DOCTYPE html>
<html>

<head>
<title>[>>]Synesthesia</title>
<link rel="stylesheet" type="text/css" href="synstyle.css">
<link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet'>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.2.0/dist/leaflet.css"
   integrity="sha512-M2wvCLH6DSRazYeZRIm1JnYyh22purTM+FDB5CsyxtQJYeKq83arPe5wgbNmcFXGqiSH2XR8dT/fJISVA1r/zQ=="
   crossorigin=""/>  
   <!-- Make sure you put this AFTER Leaflet's CSS -->
 <script src="https://unpkg.com/leaflet@1.2.0/dist/leaflet.js"
   integrity="sha512-lInM/apFSqyy1o6s89K4iQUKg6ppXEgsVxT35HbzUupEVRh2Eu9Wdl4tHj7dZO0s1uvplcYGmt3498TtHq+log=="
   crossorigin=""></script>
 <script src="heatmap.js"></script>
 <script src="leaflet-heatmap.js"></script>
 
</head>

<body>
<div id = "header">
<a href = "index.html"><img src="logosilence.png" alt="Synethesia" width="330" height="100"></a>
<h3>Synesthesia: Click an option to view a heat map of a specific property.</h3>
<div>
	<button class="button buttonMap">Temperature</button>
	<button class="button buttonMap">Pedestrian Flow</button>
	<button class="button buttonMap">Pressure</button>
	<button class="button buttonMap">Humidity</button>
	<button class="button buttonMap">Traffic</button>
	<button class="button buttonMap">Audio Level</button>
</div><br>
</div>
 <div id="map" class="leaflet-container leaflet-retina leaflet-fade-anim leaflet-grab leaflet-touch-drag" tabindex="0"><div class="leaflet-pane leaflet-map-pane" style="transform: translate3d(-7px, -29px, 0px);"><div class="leaflet-pane leaflet-tile-pane"><div class="leaflet-layer " style="z-index: 1; opacity: 1;"><div class="leaflet-tile-container leaflet-zoom-animated" style="z-index: 18; transform: translate3d(0px, 0px, 0px) scale(1);"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2723_002.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(56px, -91px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2723_004.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(312px, -91px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2724_004.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(56px, 165px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2724_002.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(312px, 165px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2723_003.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(-200px, -91px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2723.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(568px, -91px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2724_003.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(-200px, 165px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2724.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(568px, 165px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2725_003.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(56px, 421px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2725_002.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(312px, 421px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2725.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(-200px, 421px, 0px); opacity: 1;"><img alt="" role="presentation" src="Quick%20Start%20-%20Leaflet_files/2725_004.png" class="leaflet-tile leaflet-tile-loaded" style="width: 256px; height: 256px; transform: translate3d(568px, 421px, 0px); opacity: 1;"></div></div></div><div class="leaflet-pane leaflet-shadow-pane"></div><div class="leaflet-pane leaflet-overlay-pane"></div><div class="leaflet-pane leaflet-marker-pane"></div><div class="leaflet-pane leaflet-tooltip-pane"></div><div class="leaflet-pane leaflet-popup-pane"></div><div class="leaflet-proxy leaflet-zoom-animated" style="transform: translate3d(1048060px, 697408px, 0px) scale(4096);"></div></div><div class="leaflet-control-container"><div class="leaflet-top leaflet-left"><div class="leaflet-control-zoom leaflet-bar leaflet-control"><a class="leaflet-control-zoom-in" href="#" title="Zoom in" role="button" aria-label="Zoom in">+</a><a class="leaflet-control-zoom-out" href="#" title="Zoom out" role="button" aria-label="Zoom out">−</a></div></div><div class="leaflet-top leaflet-right"></div><div class="leaflet-bottom leaflet-left"></div><div class="leaflet-bottom leaflet-right"><div class="leaflet-control-attribution leaflet-control"><a href="http://leafletjs.com/" title="A JS library for interactive maps">Leaflet</a> | Map data © <a href="http://openstreetmap.org/">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com/">Mapbox</a></div></div></div></div>
</body>

<script> 
	var testData = {
  "data": [
    {
      "lat": "33.74851", 
      "long": "-84.3917", 
      "value": 101903.74899999976
    }, 
    {
      "lat": "33.74818", 
      "long": "-84.3878", 
      "value": 101903.74199999977
    }, 
    {
      "lat": "33.74783", 
      "long": "-84.3904", 
      "value": 101903.81999999967
    }, 
    {
      "lat": "33.74911", 
      "long": "-84.3875", 
      "value": 101903.81899999981
    }, 
    {
      "lat": "33.74921", 
      "long": "-84.3872", 
      "value": 101903.68299999976
    }, 
    {
      "lat": "33.74866", 
      "long": "-84.3916", 
      "value": 101903.86299999959
    }, 
    {
      "lat": "33.75074", 
      "long": "-84.3901", 
      "value": 101903.78199999986
    }, 
    {
      "lat": "33.75078", 
      "long": "-84.3896", 
      "value": 101903.80899999964
    }, 
    {
      "lat": "33.75005", 
      "long": "-84.3883", 
      "value": 101903.80099999973
    }, 
    {
      "lat": "33.74921", 
      "long": "-84.3901", 
      "value": 101903.57699999968
    }, 
    {
      "lat": "33.74962", 
      "long": "-84.3905", 
      "value": 101903.61799999964
    }, 
    {
      "lat": "33.74996", 
      "long": "-84.3886", 
      "value": 101903.83899999969
    }, 
    {
      "lat": "33.74901", 
      "long": "-84.3892", 
      "value": 101903.74999999972
    }, 
    {
      "lat": "33.74961", 
      "long": "-84.3908", 
      "value": 101904.02499999975
    }, 
    {
      "lat": "33.74891", 
      "long": "-84.3895", 
      "value": 101903.58999999975
    }, 
    {
      "lat": "33.74954", 
      "long": "-84.3888", 
      "value": 101903.86599999976
    }
  ], 
  "datatype": "PASCALS^0", 
  "end": "1507969145000", 
  "max": 101904.02499999975, 
  "min": 101903.57699999968, 
  "start": "1507606046000"
}

	
	var cfg = {
  // radius should be small ONLY if scaleRadius is true (or small radius is intended)
  // if scaleRadius is false it will be the constant radius used in pixels
  "radius": 0.0005,
  "maxOpacity": .8, 
  // scales the radius based on map zoom
  "scaleRadius": true, 
  // if set to false the heatmap uses the global maximum for colorization
  // if activated: uses the data maximum within the current map boundaries 
  //   (there will always be a red spot with useLocalExtremas true)
  "useLocalExtrema": false,
  // which field name in your data represents the latitude - default "lat"
  latField: 'lat',
  // which field name in your data represents the longitude - default "lng"
  lngField: 'long',
  // which field name in your data represents the data value - default "value"
  valueField: 'value'
};

	
	var heatmapLayer = new HeatmapOverlay(cfg);

	
	var mymap = L.map('map').setView([33.7490, -84.3880], 14);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 20,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);
  
	heatmapLayer.setData(testData);
	heatmapLayer.addTo(mymap);

</script>  
  
</html>