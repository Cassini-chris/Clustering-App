var full_text = [];
var table = [];
var rows = [];
var cells = [];


function handleFiles(files) {
  // Max Size Upload
  if(files[0].size > 10971520){
     alert("File is too big! Max size: 10MB.");
     return;
  };


  if (window.FileReader) {
      // FileReader are supported.
      getAsText(files[0]);
  } else {
      alert('FileReader are not supported in this browser.');
  }
}

function getAsText(fileToRead) {
  var reader = new FileReader();
  // Read file into memory as UTF-8
  reader.readAsText(fileToRead);
  // Handle errors load
  reader.onload = loadHandler;
  reader.onerror = errorHandler;
}

function loadHandler(event) {
  var csv = event.target.result;


  var heading_table = document.createElement("h5");
  var table = document.createElement("table");
  var rows = event.target.result.split("\n");
  for (var i = 0; i < rows.length; i++) {
      var cells = rows[i].split(",");
    //  alert("Cell: " + cells);
          //  alert(cells.length);
      if (cells.length >= 1) {

          var row = table.insertRow(-1);
        if (i < 5)  {
            //  alert("Row: " + row);
          for (var j = 0; j < cells.length; j++) {
              var cell = row.insertCell(-1);
              cell.innerHTML = cells[j];

          }
        }


      }
  }
  var dvCSV = document.getElementById("dvCSV");
  dvCSV.innerHTML = "";
  heading_table.innerHTML = "Table Snapshot - 5 Rows";
  dvCSV.appendChild(heading_table);
  dvCSV.appendChild(table);
  table.setAttribute("class", "table table-dark");
  table.setAttribute('id', 'output_table');
  processData(csv);}

function processData(csv) {
    var allTextLines = csv.split(/\r\n|\n/);
    var lines = [];
    for (var i=0; i<allTextLines.length; i++) {
        var data = allTextLines[i].split(';');
            var tarr = [];
            for (var j=0; j<data.length; j++) {
                tarr.push(data[j]);
            }
            lines.push(tarr);
    }
    //console.log(lines);
    //alert(lines);
    full_text= lines;
    var run_button = document.getElementById('run_button');
    run_button.style.display = 'block';



}

function errorHandler(evt) {
  if(evt.target.error.name == "NotReadableError") {
      alert("Cannot read file !");
  }
}
