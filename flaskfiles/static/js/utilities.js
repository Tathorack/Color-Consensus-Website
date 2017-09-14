function resetpage(){
  $('#process-progress').addClass('progress-bar-info');
  $('#process-progress').removeClass('progress-bar-danger progress-bar-success active');
  $('#process-progress').html("Waiting for search");
  $('#averaged-block').css('background', "#ffffff");
  var hex = "Color as Hex: ";
  $('#hex').text(hex);
  var rgb = "Color as RGB: ";
  $('#rgb').text(rgb);
  $('#search-string').val('');
}
function setpage(data){
  $('#process-progress').removeClass('progress-bar-danger active');
  $('#process-progress').addClass('progress-bar-success');
  $('#process-progress').html("Finished");
  $('#averaged-block').css('background', data.hex);
  var hex = "Color as Hex: " + data.hex;
  $('#hex').text(hex);
  var rgb = "Color as RGB: "+ data.red + ", "+ data.green + ", "+ data.blue;
  $('#rgb').text(rgb);
  if (0.299 * data.red + 0.587 * data.green + 0.114 * data.blue > 128) {
    $('<tr style="background-color:' + data.hex + '; color: #000000; font-weight: bold"><td>' + data.search + '</td></tr>').prependTo( ".table" );
  } else {
    $('<tr style="background-color:' + data.hex + '; color: #FFFFFF; font-weight: bold"><td>' + data.search + '</td></tr>').prependTo( ".table" );
  }
}
