// toggles directions after map has been rendered
function DirectionsToggle(){
  var el = $('#dir-toggle');
  var dir_table = $('#dir-table')
  // check if table has hidden attribute
  if (dir_table.attr("hidden") == "hidden") {
    dir_table.fadeIn() // fade in the table
    dir_table.removeAttr("hidden") // remove the hidden attribute
    el.html('hide <a href="javascript:void(0)" onclick="DirectionsToggle()">here')
  } else { 
    // it's not hidden...
    dir_table.fadeOut() // fade the table out
    dir_table.attr("hidden", "hidden") // click event listener
    el.html('click <a href="javascript:void(0)" onclick="DirectionsToggle()">here') 
  }
}